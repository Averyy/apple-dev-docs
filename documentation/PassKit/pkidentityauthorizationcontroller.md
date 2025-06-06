# PKIdentityAuthorizationController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that presents a sheet that prompts the user to allow a request for identity information.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class PKIdentityAuthorizationController
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)

#### Overview

Use this class to request [`PKIdentityElement`](pkidentityelement.md) objects from a mobile driver’s license or state identification card. When you request identity information, the system prompts the user for approval.

```swift
// Create an authorization controller.
let controller = PKIdentityAuthorizationController()

// Describe the elements you request.
let descriptor = PKIdentityDriversLicenseDescriptor()
descriptor.addElements([.age(atLeast: 18)], 
                        intentToStore: .willNotStore)
descriptor.addElements([.givenName, .portrait], 
                        intentToStore: .mayStore(days: 30))

// Create the request.
let request = PKIdentityRequest()
request.descriptor = descriptor
request.merchantIdentifier = // A merchant identifier you configure in the developer portal.
request.nonce = // Generate a nonce to verify a request is only made once.

// Prompt the user for approval.
controller.requestDocument(request) { document, error in
    // Handle the document response or error, if necessary.
}
```

The system returns response data as an encoded concise binary object representation (CBOR) blob; CBOR is a binary format similar to JSON. You must decrypt the response on your server.

For design guidance, see [`Human Interface Guidelines > Technologies > Wallet`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/technologies/wallet/introduction).

> ❗ **Important**:  This API only works on iPhone and returns an error if you access it on iPad. This framework requires a special entitlement from Apple. This entitlement is not yet available.

 This API only works on iPhone and returns an error if you access it on iPad. This framework requires a special entitlement from Apple. This entitlement is not yet available.

## Topics

### Describing a document
- [class PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md)
  An object for requesting information from a user’s driver’s license or equivalent document.
- [class PKIdentityIntentToStore](pkidentityintenttostore.md)
  An object that represents your intention to store an identity element or values derived from an identity element.
- [protocol PKIdentityDocumentDescriptor](pkidentitydocumentdescriptor.md)
  A type that describes the structure and behavior of an identity document.
### Requesting a document
- [func checkCanRequestDocument(any PKIdentityDocumentDescriptor, completion: (Bool) -> Void)](pkidentityauthorizationcontroller/checkcanrequestdocument(_:completion:).md)
  Returns whether an identity document is available to request.
- [func requestDocument(PKIdentityRequest, completion: (PKIdentityDocument?, (any Error)?) -> Void)](pkidentityauthorizationcontroller/requestdocument(_:completion:).md)
  Prompts the user to approve the request to get the identity information.
### Cancelling a request
- [func cancelRequest()](pkidentityauthorizationcontroller/cancelrequest.md)
  Cancels a request in progress.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)
  Decrypt and verify an in-app presentment request on your server.
- [class PKIdentityRequest](pkidentityrequest.md)
  An object that represents a request for identity information from a Wallet pass.
- [class PKIdentityDocument](pkidentitydocument.md)
  An object that represents the response to a request.
- [class PKIdentityElement](pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.
- [class PKIdentityButton](pkidentitybutton.md)
  An object that displays a button to trigger the identity verification flow.
- [struct VerifyIdentityWithWalletButton](verifyidentitywithwalletbutton.md)
  A view that displays a button for identity verification.
- [struct VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md)
  A type that represents the label you use with a verify identity button.
- [struct VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md)
  A type that represents the style you use with a verify identity button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityauthorizationcontroller)*