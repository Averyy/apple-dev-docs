# PKIdentityRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents a request for identity information from a Wallet pass.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class PKIdentityRequest
```

## Mentions

- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)

#### Overview

A request consists of a [`PKIdentityDocumentDescriptor`](pkidentitydocumentdescriptor.md), a [`nonce`](pkidentityrequest/nonce.md), and a [`merchantIdentifier`](pkidentityrequest/merchantidentifier.md). A [`PKIdentityDocumentDescriptor`](pkidentitydocumentdescriptor.md) describes the document an app requests.

You use a [`nonce`](pkidentityrequest/nonce.md) to verify a request is only made once. It’s up to the app and its server to generate the [`nonce`](pkidentityrequest/nonce.md) before making the request, and to verify the [`nonce`](pkidentityrequest/nonce.md) when the server receives the response.

The [`merchantIdentifier`](pkidentityrequest/merchantidentifier.md) maps to an identifier you configure in the developer portal. Payment and identitity requests share the same identifier, so it’s important that the name of the property matches the equivalent [`PKPaymentRequest`](pkpaymentrequest.md), if necessary.

## Topics

### Configuring an identity request
- [var descriptor: (any PKIdentityDocumentDescriptor)?](pkidentityrequest/descriptor.md)
  The description of the document the app requests.
- [var nonce: Data?](pkidentityrequest/nonce.md)
  An arbitrary number that the signed response playload includes.
- [var merchantIdentifier: String?](pkidentityrequest/merchantidentifier.md)
  A value that represents the merchant that makes the request.
### Instance Properties
- [var usageDescriptionKey: String?](pkidentityrequest/usagedescriptionkey.md)
  A key in the NSIdentityUsageDescriptionDictionary field of the app’s Info.plist file.

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

- [class PKIdentityAuthorizationController](pkidentityauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to allow a request for identity information.
- [class PKIdentityDocument](pkidentitydocument.md)
  An object that represents the response to a request.
- [class PKIdentityElement](pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.
- [class PKIdentityButton](pkidentitybutton.md)
  An object that displays a button to trigger the identity verification flow.
- [struct VerifyIdentityWithWalletButton](verifyidentitywithwalletbutton.md)
  A type that displays a button to present the identity verification flow.
- [struct VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md)
  A type that represents the label you use with a verify identity button.
- [struct VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md)
  A type that represents the style you use with a verify identity button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityrequest)*