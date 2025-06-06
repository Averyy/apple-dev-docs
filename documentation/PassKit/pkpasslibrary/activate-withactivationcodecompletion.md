# activate(_:withActivationCode:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Activates a payment pass using the provided activation code.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
func activate(_ paymentPass: PKPaymentPass, withActivationCode activationCode: String, completion: ((Bool, any Error) -> Void)? = nil)
```

#### Discussion

You can only activate a provisioned pass, and it must be in the [`PKPaymentPassActivationState.requiresActivation`](pkpaymentpassactivationstate/requiresactivation.md) state.

> ❗ **Important**:  Activating payment passes requires a special entitlement from Apple. For more information about requesting this entitlement, see [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

 Activating payment passes requires a special entitlement from Apple. For more information about requesting this entitlement, see [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

## Parameters

- `paymentPass`: The payment pass to activate.
- `activationCode`: The activation code.
- `completion`: This block takes the following parameters:

## See Also

- [func activate(PKPaymentPass, withActivationData: Data, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationdata:completion:).md)
  Activates a payment pass using the provided activation code.
- [func canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](pkpasslibrary/canaddpaymentpass(withprimaryaccountidentifier:).md)
  A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.
- [class func isPaymentPassActivationAvailable() -> Bool](pkpasslibrary/ispaymentpassactivationavailable-swift.type.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func isPaymentPassActivationAvailable() -> Bool](pkpasslibrary/ispaymentpassactivationavailable-swift.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func present(PKPaymentPass)](pkpasslibrary/present(_:)-67jce.md)
  Presents the payment pass for use in-store.
- [func remotePaymentPasses() -> [PKPaymentPass]](pkpasslibrary/remotepaymentpasses.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/activate(_:withactivationcode:completion:))*