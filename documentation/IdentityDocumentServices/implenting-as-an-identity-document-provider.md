# Implementing as an identity document provider

**Framework**: IdentityDocumentServices

Add your app as an option for mobile document web presentment.

#### Overview

The Identity Document Provider APIs in `IdentityDocumentServices` and `IdentityDocumentServicesUI` enable your app to participate in web presentment activated through the Digital Credentials API. By implementing the identity document provider APIs into your app, your app appears as an option for the user to select during a presentment. If the user selects your app, then an authorization UI that you provide appears for them to review.

Integrating the identity document provider requires two steps: registering your available documents with iOS and adding the Identity Document Provider app extension to your app to build the authorization UI you show to the user.

#### Add the Entitlement

Before your app can provide identity documents, you must add the [`Digital Credentials API - Mobile Document Provider`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types) entitlement to your app.

The API enables you to provide mobile documents (mdocs), defined in the ISO/IEC 18013-5 standard. Your app must specify which types of mobile documents it intends to provide in the entitlement. To maximize interoperability, your app needs to follow the appropriate standard that defines the namespaces and elements for a given mobile document type.

#### Registering Your Document

In order for iOS to know when to surface your app, register information about the documents your app contains. For a consistent user experience, register your documents as soon as the system creates a document within your app.

##### Add a Registration

Identity document registrations happen through the [`IdentityDocumentProviderRegistrationStore`](identitydocumentproviderregistrationstore.md) type. The registration store supports registering mdocs as defined in ISO/IEC 18013-5.

The following code shows an example of how to register a mobile driver’s license (mDL):

```swift
let store = IdentityDocumentProviderRegistrationStore()

do {
  let storedDocument = /* Document from your app's storage */
  let registration = MobileDocumentRegistration(
    mobileDocumentType: "org.iso.18013.5.1.mDL",
    supportedAuthorityKeyIdentifiers: [Data([0x01, 0x02, 0x03])],
    documentIdentifier: storedDocument.identifier,
    invalidationDate: storedDocument.invalidationDate
  )

  try await store.addRegistration(registration)
} catch {
  // Handle the error.
}
```

When registering an mdoc, you provide the following information:

##### Remove a Registration

When a document in your app is no longer available for use, it’s important to remove its registration from the iOS. This helps enable the best user experience. Use the appropriate document identifier to remove the registration.

If you provide a document identifier, then you can determine the correct identifier based on your app’s logic. If don’t provide a document identifier, you can query your app’s stored registrations to determine the document identifier. Here’s an example:

```swift
let store = IdentityDocumentProviderRegistrationStore()

do {
    let storedRegistrations = try await store.registrations
    
    let matchingRegistration = storedRegistrations.first { storedRegistration in
        // Your app logic to determine which registration to remove.
    }
    
    guard let documentIdentifier = matchingRegistration?.documentIdentifier else {
        // Throw an error.
    }
    
    try await registrationStore.removeRegistration(forDocumentIdentifier: documentIdentifier)
} catch {
    // Handle the error.
}
```

#### Create Your Authorization Ui

Add the Identity Document Provider app extension to create your app UI. You can use the template available in Xcode.

The generated template gives you a place to fill in SwiftUI code:

```swift

@main
struct DocumentProviderExtension: IdentityDocumentProvider {

    var body: some IdentityDocumentRequestScene {
        ISO18013MobileDocumentRequestScene { context in
            // SwiftUI view goes here.
            Text("Hello, world!")
        }
    }

}
```

The `ISO18013MobileDocumentRequestContext` provided in `IdentityDocumentServicesUI` contains the information needed to build your UI:

#### Handling the Parsed and Raw Request

The incoming request your app needs to handle is the request defined in ISO/IEC 18013-7 Annex C and ISO/IEC 18013-5. These request types contain complex structures, as well as signatures to help your document provider app authenticate the requesting website.

Due to the complex nature of this request and the fact that the website is potentially untrusted, the browser can’t provide the full request to the system components, such as your app, until the user performs an interaction. However, components of the request are necessary in order to build the authorization UI.

To provide the best user experience while protecting your app’s security, the `ISO18013MobileDocumentRequestScene` provides two requests to your app. When your app receives the first  request, a system sandbox validates the signatures of the incoming request, and parses out the information necessary to build a UI. This is the `ISO18013MobileDocumentRequest` type that is available on the `ISO18013MobileDocumentRequestContext` received by your app.

After the user approves the presentment within your app’s authorization UI, then they perform a user interaction. This means that the raw ISO/IEC 18013-7 Annex C request is ready for release to your app. This raw request releases within a closure when your app calls the send response function:

```swift
// The context received from the request scene.
let context: ISO18013MobileDocumentRequestContext

try await context.sendResponse { rawRequest in
    // Your app now has access to the raw request.
}
```

Now that your app has access to both requests, perform the following procedure:

1. Compare the consistency of the parsed request on `ISO18013MobileDocumentRequestContext` against the received `rawRequest`.
2. Validate the signatures in the raw request to confirm that it originated from a source that your app trusts. Your app needs to also confirm that the request is signed by a certificate that your app trusts. Even though the sandboxed system process checks these signatures, it’s important that your app checks them before releasing its document.
3. If both checks passed, then build and encrypt your document response according to ISO/IEC 18013-7 Annex C and ISO/IEC 18013-5.
4. Return your document response from the closure.

The following code illustrates the steps your app performs:

```swift
    try await context.sendResponse { rawRequest in
        // App specific logic to validate the two requests.
        try await validateConsistency(request: context.request, rawRequest: rawRequest)

        // Validate the signatures of the incoming request.
        try await validateRawRequest(rawRequest: rawRequest)

        // App specific logic to build and encrypt the response.
        let responseData = try await buildAndEncryptResponse(rawRequest: rawRequest)

        return ISO18013MobileDocumentResponse(responseData: responseData)
    }
```

#### Responding to User Authorization

Your app becomes eligible to register documents after the user authorizes your app to provide documents during a web presentment.

The first time your app calls the `addRegistration` API on `IdentityDocumentProviderRegistrationStore`, the system shows the user a display prompt. The user can choose to approve your app in the prompt, and then your app’s document registration continues.

If the user doesn’t approve your app, then the `addRegistration` call throws an error. The user can later enable your app again in your app’s page in `Settings`. After the user approves, the system notifies your app through the `performRegistrationUpdates` function on your app extension.

When you call this function, your app needs to ensure that all documents stored in your app are registered with iOS:

```swift
@main
struct DocumentProviderExtension: IdentityDocumentProvider {

    func performRegistrationUpdates() async {
        let store = IdentityDocumentProviderRegistrationStore()
        
        do {
            let storedRegistrations = try await store.registrations
            
            // Determine which documents in your app haven't yet been registered.
            
            // Register each document through the `addRegistration` API.
        } catch {
            // Handle the error.
        }
    }

}
```

Your app can also query the current user’s authorization status through the status API on `IdentityDocumentProviderRegistrationStore`:

```swift
let store = IdentityDocumentProviderRegistrationStore()
let status = await store.status
```

## See Also

- [Requesting a mobile document on the web](requesting-a-mobile-document-on-the-web.md)
  Send a request for mobile document information for apps installed on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/implenting-as-an-identity-document-provider)*