# Implementing as an identity document provider

**Framework**: IdentityDocumentServices  
**Role**: Article

Add your app as an option for mobile document web presentment.

## Overview

The Identity Document Provider APIs in `IdentityDocumentServices` and `IdentityDocumentServicesUI` enable your app to participate in web presentment activated through the Digital Credentials API. By implementing the identity document provider APIs into your app, your app appears as an option for the person to select during a presentment. If the person selects your app, then an authorization UI that you provide appears for them to review.

Integrating the identity document provider requires two steps: registering your available documents with iOS and adding the Identity Document Provider app extension to your app to build the authorization UI you show to the person.

## Add the entitlement

Before your app can provide identity documents, you must add the entitlement for each kind of document your app provides.

The Identity Document Services APIs support two kinds of identity documents:

- Mobile documents (mdocs), defined in the ISO/IEC 18013-5 standard. Add the [`Digital Credentials API - Mobile Document Provider`](../BundleResources/entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types.md) entitlement, and specify which mobile document types your app intends to provide.
- SD-JWT VCs, defined in the IETF SD-JWT VC specification. Add the [`Digital Credentials API - Verifiable Credential Provider`](../BundleResources/entitlements/com.apple.developer.identity-document-services.document-provider.verifiable-credential-types.md) entitlement, and specify which verifiable credential types your app intends to provide.

Your app can register and provide only the document types listed in its entitlements. To maximize interoperability, follow the appropriate standard for each type it provides. For mobile documents, use the standard that defines the namespaces and elements for that document type. For SD-JWT VCs, use the specification that defines the claims for that credential type. After you add the entitlements, register the documents your app provides.

## Register your documents

To help iOS know when to offer your app, register information about the documents your app contains. For a consistent user experience, register your documents as soon as the system creates a document within your app.

### Add a registration

Register identity documents using the [`IdentityDocumentProviderRegistrationStore`](./identitydocumentproviderregistrationstore.md). The registration store supports mdocs as defined in ISO/IEC 18013-5, and SD-JWT VCs as defined in the IETF SD-JWT VC specification. A registration describes a document that your app stores; it doesn’t contain the document itself.

The following code shows an example of how to register a mobile driver’s license (mDL):

```swift
let store = IdentityDocumentProviderRegistrationStore()
do {
    let storedDocument = /* Document from your app's storage */
    let registration = MobileDocumentRegistration(
        mobileDocumentType: "org.iso.18013.5.1.mDL",
        supportedIssuerKeyIdentifiers: [Data([0x01, 0x02, 0x03])],
        supportedAuthorityKeyIdentifiers: [Data([0x04, 0x05, 0x06])],
        documentIdentifier: storedDocument.identifier,
        invalidationDate: storedDocument.invalidationDate
    )
    try await store.addRegistration(registration)
} catch {
    // Handle the error.
}
```

When registering an mdoc, you provide the following information:

- **`mobileDocumentType`**: The standardized `docType` string that identifies the type of mobile document. You can only register document types that are listed in your entitlement.
- **`supportedIssuerKeyIdentifiers`**: A list of X.509 authority key identifiers that correspond to the document signer certificate chain for the mdoc. A relying party can specify the issuer certificates it accepts in its request. A *relying party* is the website, app, or service that asks to see that information and then relies on it to make a decision, such as confirming a person’s age or identity. If the request lists issuer key identifiers and none of them match an identifier in this list, then your app doesn’t appear as an option for that document. If the request doesn’t list any issuer key identifiers, then any document signer certificate is acceptable. The list can contain at most 1,000 identifiers, and each identifier can be at most 64 bytes.
- **`supportedAuthorityKeyIdentifiers`**: A list of authority key identifiers. These identifiers allow your app to enforce a signing requirement. If the incoming request is signed by a certificate issued by a root certificate that has a subject key identifier matching an authority key identifier in this list, then your app appears as an option to respond to the request. If there’s no certificate on the request, the system hides your app, because the app can’t successfully respond to the request. If you provide an empty array in this field, then your app can’t enforce a signing requirement for this document type.
- **`documentIdentifier`**: The identifier you use to associate a document identifier with your registration. You can use this identifier to link a registration to a document stored in your database. Your app later uses this identifier to remove registrations. If you don’t provide a document identifier, then one is automatically generated by the API.
- **`invalidationDate`**: An optional date that indicates when the mdoc isn’t valid. If the current date is past the invalidation date, then your app no longer considers this document as an option for a presentment until it refreshes the registration with a newer date.

The following code shows an example of how to register an SD-JWT VC:

```swift
let store = IdentityDocumentProviderRegistrationStore()
do {
    let storedCredential = /* A credential from your app's storage */
    let registration = VerifiableCredentialRegistration(
        verifiableCredentialTypes: ["urn:eudi:pid:1"],
        supportedIssuerKeyIdentifiers: [Data([0x01, 0x02, 0x03])],
        supportedAuthorityKeyIdentifiers: [Data([0x04, 0x05, 0x06])],
        documentIdentifier: storedCredential.identifier,
        invalidationDate: storedCredential.invalidationDate
    )
    try await store.addRegistration(registration)
} catch {
    // Handle the error.
}
```

When registering an SD-JWT VC, you provide the following information:

- **`verifiableCredentialTypes`**: The verifiable credential types that the credential can satisfy. A request matches the registration if any type it requests appears in this list. You can only register types that are listed in your entitlement. The list must contain between 1 and 100 types, and each type can be at most 512 characters.
- **`supportedIssuerKeyIdentifiers`**: A list of X.509 authority key identifiers that correspond to the issuer certificate chain for the credential. A relying party can specify the issuers it accepts in its request. If the request lists issuer key identifiers and none of them match an identifier in this list, then your app doesn’t appear as an option for that credential. If the request doesn’t list any issuer key identifiers, or this list is empty, then the credential is offered regardless of its issuer. The list can contain at most 1,000 identifiers, and each identifier can be at most 64 bytes.
- **`supportedAuthorityKeyIdentifiers`**: A list of authority key identifiers that correspond to relying party authorizers your app trusts. If the incoming request is signed by a certificate chain that includes a certificate issued by one of these authorities, then your app appears as an option to respond to the request. If the request isn’t signed, the system hides your app for this credential. If you provide an empty array, the system doesn’t filter by authority, which lets your app respond to relying parties whose identity isn’t established through an X.509 certificate chain.
- **`documentIdentifier`**: The identifier you use to associate a credential with your registration. Your app later uses this identifier to remove the registration. If you don’t provide one, the API generates one automatically.
- **`invalidationDate`**: An optional date that indicates when the credential isn’t valid. If the current date is past the invalidation date, then your app no longer appears as an option for this credential until it refreshes the registration with a newer date.

### Remove a registration

When a document in your app is no longer available for use, it’s important to remove its registration from the iOS. This helps enable the best user experience. Use the appropriate document identifier to remove the registration.

If you provide a document identifier, then you can determine the correct identifier based on your app’s logic. If you don’t provide a document identifier, you can query your app’s stored registrations to determine the document identifier. The following code shows an example of removing document registration:

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
    
    try await store.removeRegistration(forDocumentIdentifier: documentIdentifier)
} catch {
    // Handle the error.
}
```

## Create your authorization UI

Add the Identity Document Provider app extension to create your app UI. You can use the template available in Xcode.

The generated template gives you a place to fill in SwiftUI code:

```swift
@main
struct DocumentProviderExtension: IdentityDocumentProvider {
    var body: some IdentityDocumentRequestScene {
        ISO18013MobileDocumentRequestScene { context in
            // Insert your view here.
            Text("Hello, world!")
        }

        OpenID4VPRawRequestScene { context in
            // Insert your view here.
            Text("Hello, world!")
        }
    }
}
```

Each scene handles one kind of request. Include a scene for each request format your app can respond to:

- **`ISO18013MobileDocumentRequestScene`**: Handles ISO/IEC 18013-7 mobile document requests. The system parses the request for you, and only releases the full request to your app after someone authorizes it.
- **`ISO18013MobileDocumentRawRequestScene`**: Handles ISO/IEC 18013-7 mobile document requests, and provides the full request to your app up front, so your app can parse it itself. If your app provides both ISO/IEC 18013 scenes, the system uses [`ISO18013MobileDocumentRequestScene`](../IdentityDocumentServicesUI/iso18013mobiledocumentrequestscene.md).
- **`OpenID4VPRawRequestScene`**: Handles OpenID for Verifiable Presentations (OpenID4VP) requests, which can ask for mobile documents, SD-JWT verifiable credentials, or both. Your app receives the full request and is responsible for parsing and validating it.

The `ISO18013MobileDocumentRequestScene` provides an  [`ISO18013MobileDocumentRequestContext`](../IdentityDocumentServicesUI/iso18013mobiledocumentrequestcontext.md) which contains the information needed to build your UI:

- **`requestingWebsiteOrigin`**: The origin URL of the requesting website.
- **`request`**: A parsed version of the incoming request. This contains information about the documents requested, including the issuer certificates the relying party accepts with [`issuerKeyIdentifiers`](./iso18013mobiledocumentrequest/documentrequest/issuerkeyidentifiers.md), and any certificates attached to the request.
- **`sendResponse`**: A function that allows your app to return a built document response. This function also allows your app to receive the raw ISO/IEC 18013 request. Only call this function after a person explicitly authorizes the release of their document in your UI.
- **`cancel`**: A function that allows your app to cancel out of the current presentment.

The `ISO18013MobileDocumentRawRequestScene` provides an  [`ISO18013MobileDocumentRawRequestContext`](../IdentityDocumentServicesUI/iso18013mobiledocumentrawrequestcontext.md) which contains the following information to build your UI:

- **`requestingWebsiteOrigin`**: The origin URL of the requesting website, if present.
- **`requestData`**: The incoming request, JSON encoded according to the ISO/IEC 18013-7 request profile.
- **`sendResponse(_:)`**: A function that returns your document response. Only call this function after the person explicitly authorizes the release of their document in your UI.
- **`cancel()`**: A function that cancels the current presentment.

The `OpenID4VPRawRequestScene` provides an  [`OpenID4VPRawRequestContext`](../IdentityDocumentServicesUI/openid4vprawrequestcontext.md) which contains the following information to build your UI:

- **`requestingWebsiteOrigin`**: The origin URL of the requesting website, if present.
- **`exchangeProtocol`**: The OpenID4VP exchange protocol the request uses, an [`OpenID4VPExchangeProtocolIdentifier`](./openid4vpexchangeprotocolidentifier.md) value of [`OpenID4VPExchangeProtocolIdentifier.unsignedV1`](./openid4vpexchangeprotocolidentifier/unsignedv1.md), [`OpenID4VPExchangeProtocolIdentifier.signedV1`](./openid4vpexchangeprotocolidentifier/signedv1.md), or [`OpenID4VPExchangeProtocolIdentifier.multisignedV1`](./openid4vpexchangeprotocolidentifier/multisignedv1.md).
- **`requestData`**: The incoming request, encoded according to its exchange protocol.
- **`sendResponse(_:)`**: A function that returns your OpenID4VP Authorization Response as an `OpenID4VPRawRequestContext/Response`. Only call this function after the person explicitly authorizes the release of their credentials in your UI.
- **`cancel()`**: A function that cancels the current presentment.

## Handle incoming requests

The incoming request your app needs to handle is defined in ISO/IEC 18013-7 Annex C and ISO/IEC 18013-5, or OpenID for Verifiable Presentations (OpenID4VP). These request types contain complex structures, as well as signatures to help your document provider app authenticate the requesting website.

Due to the nature of these requests and the fact that the website is potentially untrusted, the browser can’t provide the full request to the system components, such as your app, until the person performs an interaction. However, components of the request are necessary in order to build the authorization UI.

### Handle mobile document requests

To provide the best user experience while protecting your app’s security, the [`ISO18013MobileDocumentRequestScene`](../IdentityDocumentServicesUI/iso18013mobiledocumentrequestscene.md) provides two requests to your app. When your app receives the first request, a system sandbox validates the signatures of the incoming request, and parses out the information necessary to build a UI. This is the [`ISO18013MobileDocumentRequest`](./iso18013mobiledocumentrequest.md) type that is available on the `ISO18013MobileDocumentRequestContext` received by your app.

After the person approves the presentment in your authorization UI, the system releases the raw ISO/IEC 18013-7 Annex C request to your app. Your app receives it in a closure when it calls the send response function:

```swift
// The context received from the request scene.
let context: ISO18013MobileDocumentRequestContext

try await context.sendResponse { rawRequest in
    // Your app now has access to the raw request.
}
```

When your app has access to both requests, perform the following procedure:

1. Compare the consistency of the parsed request on [`ISO18013MobileDocumentRequestContext`](../IdentityDocumentServicesUI/iso18013mobiledocumentrequestcontext.md) against the received `rawRequest`.
2. Validate the signatures in the raw request to confirm that it originated from a source that your app trusts. Your app needs to also confirm that the request is signed by a certificate that your app trusts. Even though the sandboxed system process checks these signatures, it’s important that your app checks them before releasing its document.
3. If both checks pass, build and encrypt your document response according to ISO/IEC 18013-7 Annex C and ISO/IEC 18013-5.
4. Return your document response from the closure.

The following code illustrates the steps your app performs:

```swift
    try await context.sendResponse { rawRequest in
        // App-specific logic to validate the two requests.
        try await validateConsistency(request: context.request, rawRequest: rawRequest)

        // Validate the signatures of the incoming request.
        try await validateRawRequest(rawRequest: rawRequest)

        // App-specific logic to build and encrypt the response.
        let responseData = try await buildAndEncryptResponse(rawRequest: rawRequest)

        return ISO18013MobileDocumentResponse(responseData: responseData)
    }
```

Some apps require the raw request at the time of building the authorization UI, such as for handling and displaying components from request extensions.

You can use the [`ISO18013MobileDocumentRawRequestScene`](../IdentityDocumentServicesUI/iso18013mobiledocumentrawrequestscene.md), which immediately provides the raw ISO/IEC 18013-7 Annex C request through the [`ISO18013MobileDocumentRawRequestContext`](../IdentityDocumentServicesUI/iso18013mobiledocumentrawrequestcontext.md) when drawing the authorization UI.

Because the system gives your app the raw request up front, validate it as soon as the scene appears. Use your app’s validation to check the request’s signatures and parse it into an [`ISO18013MobileDocumentRequest`](./iso18013mobiledocumentrequest.md), and show your authorization UI only if validation succeeds:

```swift
ISO18013MobileDocumentRawRequestScene { context in
    
    if validateRequest(context) {
        // Your SwiftUI authorization view.
        AuthorizationView(
            request: context.requestData,
            onApprove: {
                // Your app-specific logic to build and encrypt the response.
                let responseData = try await buildAndEncryptResponse(for: context.requestData)

                context.sendResponse(responseData)
            }, onDeny: {
                context.cancel()
            }
        )
    } else {
        // Your SwiftUI error view.
        ErrorView(onCancel: {
            context.cancel()
        })
    }
}
```

To meet the same security standard and satisfy user interaction when presenting this scene, the system first shows a picker screen before it displays your app’s authorization screen. Your app must parse the request and validate its signatures itself before releasing a document.

### Handle OpenID4VP requests

To respond to requests in an OpenID4VP format, add the [`OpenID4VPRawRequestScene`](../IdentityDocumentServicesUI/openid4vprawrequestscene.md) to your extension’s body. This scene provides the request data directly in an [`OpenID4VPRawRequestContext`](../IdentityDocumentServicesUI/openid4vprawrequestcontext.md). As with [`ISO18013MobileDocumentRawRequestScene`](../IdentityDocumentServicesUI/iso18013mobiledocumentrawrequestscene.md), the system shows a picker screen before displaying your app’s authorization UI.

When your app receives an OpenID4VP request, validate its signatures and confirm that your app trusts the signer before showing your authorization UI. After the user approves, build and encrypt the response as the request specifies, and send it:

```swift
OpenID4VPRawRequestScene { context in
    
    // Your app's logic that validates `context.requestData` with the raw request validator.
    if validateRequest(context) {
        // Your SwiftUI authorization view.
    } else {
        // Your SwiftUI error view.
    }
}
```

The rest of the flow matches the ISO18013MobileDocument example above.

## Respond to someone’s authorization

Before your app can register documents, the person must authorize your app to provide documents.

The first time your app calls the [`addRegistration(_:)`](./identitydocumentproviderregistrationstore/addregistration%28_%29.md) API on [`IdentityDocumentProviderRegistrationStore`](./identitydocumentproviderregistrationstore.md), the system shows the person a display prompt. The person can choose to approve your app in the prompt, and then your app’s document registration continues.

If the person doesn’t approve your app, then the [`addRegistration(_:)`](./identitydocumentproviderregistrationstore/addregistration%28_%29.md) call throws an error. The person can later turn on your app again through your app’s page in Settings. After the person approves, the system notifies your app through the `performRegistrationUpdates` function on your app extension.

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

Your app can also query the person’s current authorization status through the status API on [`IdentityDocumentProviderRegistrationStore`](./identitydocumentproviderregistrationstore.md):

```swift
let store = IdentityDocumentProviderRegistrationStore()
let status = await store.status
```

## See Also

### Essentials
- [Requesting a mobile document on the web](./requesting-a-mobile-document-on-the-web.md)
  Send a request for mobile document information for apps installed on a device.
- [Verifying a mobile document from a passport](./verifying-a-mobile-document-from-a-passport.md)
  Validate a response from mobile document information derived from a passport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/implementing-as-an-identity-document-provider)*