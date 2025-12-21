# Requesting identity data from a Wallet pass

**Framework**: PassKit (Apple Pay and Wallet)

Initiate a request for identity information by prompting a user for permission and decrypting a response payload.

#### Overview

The Wallet app allows people to store an identification card, for example, a mobile driver’s license (mDL), or national identification card from a government issuing authority, or a digital ID issued by Apple.

Beginning on iPhone with iOS 16, you can request information from IDs in Wallet to verify a person’s age or identity. If a person accepts the request, the system gets the information from their issuing authority and your app receives a payload. After decryption, the payload contains data that follows the ISO 18013-5 specification. To use the elements your app requests, send the payload to your server for verification.

For design guidance, see [`Human Interface Guidelines > Technologies > Wallet`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/technologies/wallet/introduction).

> ❗ **Important**:  Building an app with this entitlement requires macOS 13 or later. For more information about the entitlement, see [`Getting started with the Verify with Wallet API`](https://developer.apple.comhttps://developer.apple.com/wallet/get-started-with-verify-with-wallet/).

##### Create an Identity Document Descriptor

Before you request information from an ID in Wallet, you create an object to describe the elements you need. Your app can only request the elements your entitlement grants. There are a few identity document descriptor options:

For each element, you specify your intent to store the resulting data by using [`mayStore(days:)`](pkidentityintenttostore/maystore(days:).md), [`mayStore`](pkidentityintenttostore/maystore.md), or [`willNotStore`](pkidentityintenttostore/willnotstore.md). Upon request, the system presents the information for a person to review in a system sheet.

The framework allows for requesting the Boolean [`age(atLeast:)`](pkidentityelement/age(atleast:).md) element for any age between `1` and `125` only if the issuer includes it. If an app requests [`age(atLeast:)`](pkidentityelement/age(atleast:).md) and the `age_over_XX` element isn’t present in the mobile driver’s license, the framework falls back to a request for the age element.

An app can’t include both an [`age(atLeast:)`](pkidentityelement/age(atleast:).md) element and an [`age`](pkidentityelement/age.md) element in the same request.

The following code shows how you create the different identity document descriptors:

To check whether the identity document you describe is available to request, create a [`PKIdentityAuthorizationController`](pkidentityauthorizationcontroller.md) and call [`checkCanRequestDocument(_:completion:)`](pkidentityauthorizationcontroller/checkcanrequestdocument(_:completion:).md). If the document exists, show a [`PKIdentityButton`](pkidentitybutton.md) to allow the user to begin the authorization request.

```swift
let controller = PKIdentityAuthorizationController()
controller.checkCanRequestDocument(descriptor) { canRequest in
    // Show or hide the identity button.
}
```

##### Create a Request

To create an identity request, you need the merchant identifier you configure in the developer portal. A merchant identifier never expires, and you can use the same one that you use for Apple Pay.

A request also needs a [`nonce`](pkidentityrequest/nonce.md) to prevent your server from using a response document more than once. Your server needs the [`nonce`](pkidentityrequest/nonce.md) to decrypt the response document, so generate it there and associate it with the user’s session.

```swift
let request = PKIdentityRequest()
request.descriptor = descriptor
request.merchantIdentifier = // The merchant identifier.
request.nonce = // The nonce your server generates.
```

Your app’s `Info.plist` file needs to provide a message for the `NSIdentityUsageDescription` key. If this key is missing, any attempt to request a document fails.

##### Request the Document

When requesting a document, the system presents a sheet to the user to confirm the request before retrieving any data. If the user rejects the request, your app receives a [`PKIdentityError.Code.cancelled`](pkidentityerror-swift.struct/code/cancelled.md) error.

```swift
do {
    let document = try await controller.requestDocument(request)
} catch {
    // Handle the error.
}
```

When you receive a [`PKIdentityDocument`](pkidentitydocument.md), you’re ready to verify the request payload. The data in the [`encryptedData`](pkidentitydocument/encrypteddata.md) property isn’t readable on the device, so you need to send it to your server for verification.

The elements in the descriptors map this way in their responses:

- [`PKIdentityDriversLicenseDescriptor`](pkidentitydriverslicensedescriptor.md) maps to a set of elements in the ISO and American Association of Motor Vehicle Administrators (AAMVA) namespaces.
- [`PKIdentityPhotoIDDescriptor`](pkidentityphotoiddescriptor.md) maps to a set of elements in the ISO.
- [`PKIdentityNationalIDCardDescriptor`](pkidentitynationalidcarddescriptor.md) maps to a set of elements in the ISO and JP namespace.
- See [`PKIdentityDriversLicenseDescriptor`](pkidentitydriverslicensedescriptor.md), [`PKIdentityPhotoIDDescriptor`](pkidentityphotoiddescriptor.md), and [`PKIdentityNationalIDCardDescriptor`](pkidentitynationalidcarddescriptor.md) for a list of elements.

> **Note**:  Only one request can be in progress at a time. Otherwise, the system returns a [`PKIdentityError.Code.requestAlreadyInProgress`](pkidentityerror-swift.struct/code/requestalreadyinprogress.md) error.

To learn more about verifying identity requests, see [`Verifying Wallet identity requests`](verifying-wallet-identity-requests.md).

##### Test the Implementation

Even if you don’t live in an area that supports IDs in Wallet, you can test your implementation through the iPhone simulator or by downloading a developer profile on your local device. When you request a document, you receive a mock mDL that’s similar to a real ID. When you test with the simulator, the response doesn’t include a real issuing authority or device signature. The developer test profile produces a real device signature, but not a real issuer signature. A mock mDL isn’t visible in the Wallet app, so don’t treat it as real. To activate a mock mDL on your device, download the Wallet identity developer profile from [`Profiles and Logs`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/).

## See Also

- [Pass Type IDs Entitlement](../BundleResources/Entitlements/com.apple.developer.pass-type-identifiers.md)
  A list of identifiers that specify pass types that your app can access in Wallet.
- [Merchant IDs Entitlement](../BundleResources/Entitlements/com.apple.developer.in-app-payments.md)
  A list of merchant IDs your app uses for Apple Pay support.
- [com.apple.developer.in-app-identity-presentment](../BundleResources/Entitlements/com.apple.developer.in-app-identity-presentment.md)
  An entitlement that verifies age or identity.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)
  Decrypt and verify an in-app presentment request on your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/requesting-identity-data-from-a-wallet-pass)*