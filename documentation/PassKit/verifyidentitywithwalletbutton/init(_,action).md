# init(_:action:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Creates a verify identity button that starts the identity authorization flow.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
nonisolated
init(_ label: VerifyIdentityWithWalletButtonLabel = .verifyIdentity, action: @escaping () -> Void)
```

Available when `Fallback` is `EmptyView`.

## Parameters

- `label`: The button’s label.
- `action`: The action to perform when a person taps the button.

## See Also

### Creating the button
- [init(VerifyIdentityWithWalletButtonLabel, request: PKIdentityRequest, onCompletion: (Result<PKIdentityDocument, any Error>) -> Void)](./init%28_,request,oncompletion%29.md)
  Creates a verify identity button that starts the identity authorization flow, with a completion handler.
- [init(VerifyIdentityWithWalletButtonLabel, request: PKIdentityRequest, onCompletion: (Result<PKIdentityDocument, any Error>) -> Void, fallback: () -> Fallback)](./init%28_,request,oncompletion,fallback%29.md)
  Creates a verify identity button that starts the identity authorization flow, with a fallback view to use if the app can’t start the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/verifyidentitywithwalletbutton/init(_:action:))*