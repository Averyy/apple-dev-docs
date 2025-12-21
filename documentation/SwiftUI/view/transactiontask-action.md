# transactionTask(_:action:)

**Framework**: SwiftUI  
**Kind**: method

Provides a task to perform before this view appears

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
nonisolated
func transactionTask(_ configuration: CredentialTransaction.Configuration?, action: @escaping (CredentialTransaction) async -> Void) -> some View
```

#### Discussion

This task provides an instance of a `CredentialTransaction` to be used to perform transactions.

A typical client should use the APIs in the following sequence:

1. `acquirePresentmentIntentAssertion()` prior to showing any proprietary payment UI
2. `relinquish()` the assertion before invoking the transaction API
3. `configuration.invalidate()` after presenting the credential
4. Optionally, `acquirePresentmentIntentAssertion()` to finish up any proprietary payment UI
5. `relinquish()` the assertion

For example:

```swift
 struct TransactionView: View {
     @State private var configuration: CredentialTransaction.Configuration?
     private var assertion: PresentmentIntentAssertion // acquirePresentmentIntentAssertion() before transitioning into this view (step 1)
     private var activeSession: CredentialSession
     private var selectedCredential: Credential

     var body: some View {
         VStack {
             Button("Perform Transaction") {
                 guard let configuration else {
                    configuration = activeSession.configuration()
                    return
                 }

                 configuration.invalidate() // step 3
                 // Optional
                 assertion = try await session.acquirePresentmentIntentAssertion() // step 4
                 // handle any proprietary UI
                 try await assertion.relinquish() // step 5
                 // Optional end
             }
             .transactionTask(configuration) { transaction in
                 do {
                     try await assertion.relinquish() // step 2
                     try await transaction.performTransaction(using: selectedCredential)
                 } catch {
                     // code to handle error
                 }
             }
         }
     }
 }
```

## Parameters

- `configuration`: A configuration containing information about the transaction task.   When the task is completed or an error is encountered while performing the task,   the system invalidates this configuration, and the   is invalidated.
- `action`: A closure that will be called when   is  .   It provides a   instance that can be used to perform transactions.

## See Also

- [struct PayWithApplePayButton](../PassKit/PayWithApplePayButton.md)
  A type that provides a button to pay with Apple pay.
- [struct AddPassToWalletButton](../PassKit/AddPassToWalletButton.md)
  A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [struct VerifyIdentityWithWalletButton](../PassKit/VerifyIdentityWithWalletButton.md)
  A type that displays a button to present the identity verification flow.
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
- [func payWithApplePayButtonStyle(PayWithApplePayButtonStyle) -> some View](view/paywithapplepaybuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle) -> some View](view/verifyidentitywithwalletbuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [struct AsyncShareablePassConfiguration](../PassKit/AsyncShareablePassConfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/transactiontask(_:action:))*