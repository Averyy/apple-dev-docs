# addOrderToWalletButtonStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the button’s style.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
@MainActor
@preconcurrency func addOrderToWalletButtonStyle(_ style: AddOrderToWalletButtonStyle) -> some View
```

#### Discussion

(See `AddOrderToWalletButtonStyle`).

## See Also

- [struct PayWithApplePayButton](../PassKit/PayWithApplePayButton.md)
  A type that provides a button to pay with Apple pay.
- [struct AddPassToWalletButton](../PassKit/AddPassToWalletButton.md)
  A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [struct VerifyIdentityWithWalletButton](../PassKit/VerifyIdentityWithWalletButton.md)
  A type that displays a button to present the identity verification flow.
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
- [func payWithApplePayButtonStyle(PayWithApplePayButtonStyle) -> some View](view/paywithapplepaybuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle) -> some View](view/verifyidentitywithwalletbuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [struct AsyncShareablePassConfiguration](../PassKit/AsyncShareablePassConfiguration.md)
- [func transactionTask(CredentialTransaction.Configuration?, action: (CredentialTransaction) async -> Void) -> some View](view/transactiontask(_:action:).md)
  Provides a task to perform before this view appears


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/addordertowalletbuttonstyle(_:))*