# init(_:request:onCompletion:fallback:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a verify identity button that starts the identity authorization flow, with a fallback view to use if the app can’t start the flow.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
nonisolated
init(_ label: VerifyIdentityWithWalletButtonLabel = .verifyIdentity, request: PKIdentityRequest, onCompletion: @escaping (Result<PKIdentityDocument, any Error>) -> Void, @ViewBuilder fallback: () -> Fallback)
```

## Parameters

- `label`: The button’s label.
- `request`: The identity request to make when a person taps the button.
- `onCompletion`: The completion handler the framework calls when finishing the authorization flow.
- `fallback`: A view to display if the app can’t perform an identity request.

## See Also

- [init(VerifyIdentityWithWalletButtonLabel, action: () -> Void)](verifyidentitywithwalletbutton/init(_:action:).md)
  Creates a verify identity button that starts the identity authorization flow.
- [init(VerifyIdentityWithWalletButtonLabel, request: PKIdentityRequest, onCompletion: (Result<PKIdentityDocument, any Error>) -> Void)](verifyidentitywithwalletbutton/init(_:request:oncompletion:).md)
  Creates a verify identity button that starts the identity authorization flow, with a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/verifyidentitywithwalletbutton/init(_:request:oncompletion:fallback:))*