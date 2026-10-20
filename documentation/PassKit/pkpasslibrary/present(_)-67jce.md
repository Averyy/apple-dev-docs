# present(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Presents the payment pass for use in-store.

**Availability**:
- iOS 10.0+ - Deprecated in 27.2
- iPadOS 10.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.12+
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`present(_:)`](./present%28_%29-9467u.md) instead.

## Declaration

```swift
func present(_ pass: PKPaymentPass)
```

```objc
- (void) presentPaymentPass:(PKPaymentPass *) pass;
```

#### Discussion

You can use [`present(_:)`](./present%28_%29-67jce.md)  to present your payment pass for use in-store.  Your app must have the proper entitlement to see the payment pass that you present. Therefore, this method is mostly relevant to a bank or merchant app that presents its own payment method for use in-store.

## Parameters

- `pass`: The pass to present.

## See Also

### Deprecated Methods
- [func activate(PKPaymentPass, withActivationCode: String, completion: ((Bool, any Error) -> Void)?)](./activate%28_,withactivationcode,completion%29.md)
  Activates a payment pass using the provided activation code.
- [func activate(PKPaymentPass, withActivationData: Data, completion: ((Bool, any Error) -> Void)?)](./activate%28_,withactivationdata,completion%29.md)
  Activates a payment pass using the provided activation code.
- [func canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](./canaddpaymentpass%28withprimaryaccountidentifier%29.md)
  A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.
- [class func isPaymentPassActivationAvailable() -> Bool](./ispaymentpassactivationavailable%28%29-swift.type.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func isPaymentPassActivationAvailable() -> Bool](./ispaymentpassactivationavailable%28%29-swift.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func remotePaymentPasses() -> [PKPaymentPass]](./remotepaymentpasses%28%29.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/present(_:)-67jce)*