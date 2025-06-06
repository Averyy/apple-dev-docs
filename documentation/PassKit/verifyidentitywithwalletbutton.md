# VerifyIdentityWithWalletButton

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

A view that displays a button for identity verification.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct VerifyIdentityWithWalletButton<Fallback> where Fallback : View
```

## Topics

### Creating the button
- [init(VerifyIdentityWithWalletButtonLabel, action: () -> Void)](verifyidentitywithwalletbutton/init(_:action:).md)
  Creates a verify identity button that starts the identity authorization flow.
- [init(VerifyIdentityWithWalletButtonLabel, request: PKIdentityRequest, onCompletion: (Result<PKIdentityDocument, any Error>) -> Void)](verifyidentitywithwalletbutton/init(_:request:oncompletion:).md)
  Creates a verify identity button that starts the identity authorization flow, with a completion handler.
- [init(VerifyIdentityWithWalletButtonLabel, request: PKIdentityRequest, onCompletion: (Result<PKIdentityDocument, any Error>) -> Void, fallback: () -> Fallback)](verifyidentitywithwalletbutton/init(_:request:oncompletion:fallback:).md)
  Creates a verify identity button that starts the identity authorization flow, with a fallback view to use if the app can’t start the flow.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)
  Decrypt and verify an in-app presentment request on your server.
- [class PKIdentityAuthorizationController](pkidentityauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to allow a request for identity information.
- [class PKIdentityRequest](pkidentityrequest.md)
  An object that represents a request for identity information from a Wallet pass.
- [class PKIdentityDocument](pkidentitydocument.md)
  An object that represents the response to a request.
- [class PKIdentityElement](pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.
- [class PKIdentityButton](pkidentitybutton.md)
  An object that displays a button to trigger the identity verification flow.
- [struct VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md)
  A type that represents the label you use with a verify identity button.
- [struct VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md)
  A type that represents the style you use with a verify identity button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/verifyidentitywithwalletbutton)*