# payWithApplePayButtonStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func payWithApplePayButtonStyle(_ style: PayWithApplePayButtonStyle) -> some View
```

## See Also

- [@MainActor @preconcurrency struct PayWithApplePayButton<Fallback> where Fallback : View](../PassKit/PayWithApplePayButton.md)
- [@MainActor @preconcurrency struct AddPassToWalletButton<Fallback> where Fallback : View](../PassKit/AddPassToWalletButton.md)
- [@MainActor @preconcurrency struct VerifyIdentityWithWalletButton<Fallback> where Fallback : View](../PassKit/VerifyIdentityWithWalletButton.md)
  A view that displays a button for identity verification.
- [func addOrderToWalletButtonStyle(AddOrderToWalletButtonStyle) -> some View](view/addordertowalletbuttonstyle(_:).md)
  Sets the button’s style.
- [func addPassToWalletButtonStyle(AddPassToWalletButtonStyle) -> some View](view/addpasstowalletbuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PKAddPassButtonStyle`).
- [func onApplePayCouponCodeChange(perform: (String) async -> PKPaymentRequestCouponCodeUpdate) -> some View](view/onapplepaycouponcodechange(perform:).md)
  Called when a user has entered or updated a coupon code. This is required if the user is being asked to provide a coupon code.
- [func onApplePayPaymentMethodChange(perform: (PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate) -> some View](view/onapplepaypaymentmethodchange(perform:).md)
  Called when a payment method has changed and asks for an update payment request. If this modifier isn’t provided Wallet will assume the payment method is valid.
- [func onApplePayShippingContactChange(perform: (PKContact) async -> PKPaymentRequestShippingContactUpdate) -> some View](view/onapplepayshippingcontactchange(perform:).md)
  Called when a user selected a shipping address. This is required if the user is being asked to provide a shipping contact.
- [func onApplePayShippingMethodChange(perform: (PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate) -> some View](view/onapplepayshippingmethodchange(perform:).md)
  Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.
- [func payLaterViewAction(PayLaterViewAction) -> some View](view/paylaterviewaction(_:).md)
  Sets the action on the PayLaterView. See `PKPayLaterAction`.
- [func payLaterViewDisplayStyle(PayLaterViewDisplayStyle) -> some View](view/paylaterviewdisplaystyle(_:).md)
  Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.
- [func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle) -> some View](view/verifyidentitywithwalletbuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [@MainActor @preconcurrency struct AsyncShareablePassConfiguration<Content> where Content : View](../PassKit/AsyncShareablePassConfiguration.md)
- [func transactionTask(CredentialTransaction.Configuration?, action: (CredentialTransaction) async -> Void) -> some View](view/transactiontask(_:action:).md)
  Provides a task to perform before this view appears


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/paywithapplepaybuttonstyle(_:))*