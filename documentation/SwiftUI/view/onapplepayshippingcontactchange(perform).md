# onApplePayShippingContactChange(perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Called when a user selected a shipping address. This is required if the user is being asked to provide a shipping contact.

**Availability**:
- iOS 15.5+
- iPadOS 15.5+
- Mac Catalyst 15.5+
- macOS 12.5+
- watchOS 8.5+

## Declaration

```swift
nonisolated
func onApplePayShippingContactChange(perform action: @escaping (PKContact) async -> PKPaymentRequestShippingContactUpdate) -> some View
```

## Return Value

An update to the payment request shipping methods.

## See Also

### Accessing Apple Pay and Wallet
- [struct PayWithApplePayButton](../../PassKit/paywithapplepaybutton.md)
  A type that provides a button to pay with Apple pay.
- [struct AddPassToWalletButton](../../PassKit/addpasstowalletbutton.md)
  A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [struct VerifyIdentityWithWalletButton](../../PassKit/verifyidentitywithwalletbutton.md)
  A type that displays a button to present the identity verification flow.
- [func addOrderToWalletButtonStyle(AddOrderToWalletButtonStyle) -> some View](./addordertowalletbuttonstyle%28_%29.md)
  Sets the button’s style.
- [func addPassToWalletButtonStyle(AddPassToWalletButtonStyle) -> some View](./addpasstowalletbuttonstyle%28_%29.md)
  Sets the style to be used by the button. (see `PKAddPassButtonStyle`).
- [func onApplePayCouponCodeChange(perform: (String) async -> PKPaymentRequestCouponCodeUpdate) -> some View](./onapplepaycouponcodechange%28perform%29.md)
  Called when a user has entered or updated a coupon code. This is required if the user is being asked to provide a coupon code.
- [func onApplePayPaymentMethodChange(perform: (PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate) -> some View](./onapplepaypaymentmethodchange%28perform%29.md)
  Called when a payment method has changed and asks for an update payment request. If this modifier isn’t provided Wallet will assume the payment method is valid.
- [func onApplePayShippingMethodChange(perform: (PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate) -> some View](./onapplepayshippingmethodchange%28perform%29.md)
  Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.
- [func payLaterViewAction(PayLaterViewAction) -> some View](./paylaterviewaction%28_%29.md)
  Sets the action on the PayLaterView. See `PKPayLaterAction`.
- [func payLaterViewDisplayStyle(PayLaterViewDisplayStyle) -> some View](./paylaterviewdisplaystyle%28_%29.md)
  Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.
- [func payWithApplePayButtonDisableCardArt() -> some View](./paywithapplepaybuttondisablecardart%28%29.md)
  Sets the features that should be allowed to show on the payment buttons.
- [func payWithApplePayButtonStyle(PayWithApplePayButtonStyle) -> some View](./paywithapplepaybuttonstyle%28_%29.md)
  Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle) -> some View](./verifyidentitywithwalletbuttonstyle%28_%29.md)
  Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [struct AsyncShareablePassConfiguration](../../PassKit/asyncshareablepassconfiguration.md)
- [func transactionTask(CredentialTransaction.Configuration?, action: (CredentialTransaction) async -> Void) -> some View](./transactiontask%28_,action%29.md)
  Provides a task to perform before this view appears


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onapplepayshippingcontactchange(perform:))*