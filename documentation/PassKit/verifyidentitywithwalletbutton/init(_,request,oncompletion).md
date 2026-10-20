# init(_:request:onCompletion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Creates a verify identity button that starts the identity authorization flow, with a completion handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
nonisolated
init(_ label: VerifyIdentityWithWalletButtonLabel = .verifyIdentity, request: PKIdentityRequest, onCompletion: @escaping (Result<PKIdentityDocument, any Error>) -> Void)
```

Available when `Fallback` is `EmptyView`.

## Parameters

- `label`: The button’s label.
- `request`: The identity request to make when a person taps the button.
- `onCompletion`: The completion handler the framework calls when finishing the authorization flow.

  - **`result`**: A result that contains an identity document, if successful; otherwise, an error.

## See Also

### Creating the button
- [init(VerifyIdentityWithWalletButtonLabel, action: () -> Void)](./init%28_,action%29.md)
  Creates a verify identity button that starts the identity authorization flow.
- [init(VerifyIdentityWithWalletButtonLabel, request: PKIdentityRequest, onCompletion: (Result<PKIdentityDocument, any Error>) -> Void, fallback: () -> Fallback)](./init%28_,request,oncompletion,fallback%29.md)
  Creates a verify identity button that starts the identity authorization flow, with a fallback view to use if the app can’t start the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/verifyidentitywithwalletbutton/init(_:request:oncompletion:))*