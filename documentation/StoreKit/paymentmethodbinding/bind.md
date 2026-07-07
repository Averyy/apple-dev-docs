# bind()

**Framework**: StoreKit  
**Kind**: method

Asks the user to confirm whether to add the payment method to their Apple payment methods.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- visionOS 1.0+

## Declaration

```swift
func bind() async throws
```

#### Discussion

> ❗ **Important**:  This method displays a system prompt that asks users to authenticate with their Apple Account. Call this method only after an explicit user action, like tapping or clicking a button.

This method displays an Apple sheet that asks the user to confirm whether to add the payment method associated with the in-app binding ID ([`id`](paymentmethodbinding/id.md)). If the user confirms adding the payment method, it becomes the user’s primary payment method for media purchases and subscriptions from Apple.

The binding succeeds if this method doesn’t throw an error.

This method throws an error in any of the following conditions:

- The user cancels the sheet and doesn’t confirm the payment method update.
- The in-app binding ID (`id`) is invalid or expired.
- The user isn’t eligible.
- The app isn’t entitled to use this API.

For more information about the errors, see [`PaymentMethodBinding.PaymentMethodBindingError`](paymentmethodbinding/paymentmethodbindingerror.md) and [`StoreKitError.userCancelled`](storekiterror/usercancelled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/paymentmethodbinding/bind())*