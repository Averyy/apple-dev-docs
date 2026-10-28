# canAddPaymentPass(withPrimaryAccountIdentifier:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.

**Availability**:
- iOS 9.0+ - Deprecated in 27.2
- iPadOS 9.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.12+
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`canAddSecureElementPass(primaryAccountIdentifier:)`](./canaddsecureelementpass%28primaryaccountidentifier%29.md) instead.

## Declaration

```swift
func canAddPaymentPass(withPrimaryAccountIdentifier primaryAccountIdentifier: String) -> Bool
```

```objc
- (BOOL) canAddPaymentPassWithPrimaryAccountIdentifier:(NSString *) primaryAccountIdentifier;
```

## Return Value

[`true`](../../Swift/true.md) if PassKit can add the pass.

## Discussion

Adding payment passes requires a special entitlement from Apple. If the entitlement isn’t present, this method returns [`false`](../../Swift/false.md).  For more information about requesting this entitlement, see [developer.apple.com/apple-pay/](https://developer.apple.com/apple-pay/).

## Parameters

- `primaryAccountIdentifier`: A unique identifier for the underlying funding primary account number (PAN). This isn’t the PAN itself.

## See Also

### Deprecated Methods
- [func activate(PKPaymentPass, withActivationCode: String, completion: ((Bool, any Error) -> Void)?)](./activate%28_,withactivationcode,completion%29.md)
  Activates a payment pass using the provided activation code.
- [func activate(PKPaymentPass, withActivationData: Data, completion: ((Bool, any Error) -> Void)?)](./activate%28_,withactivationdata,completion%29.md)
  Activates a payment pass using the provided activation code.
- [class func isPaymentPassActivationAvailable() -> Bool](./ispaymentpassactivationavailable%28%29-swift.type.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func isPaymentPassActivationAvailable() -> Bool](./ispaymentpassactivationavailable%28%29-swift.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func present(PKPaymentPass)](./present%28_%29-67jce.md)
  Presents the payment pass for use in-store.
- [func remotePaymentPasses() -> [PKPaymentPass]](./remotepaymentpasses%28%29.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/canaddpaymentpass(withprimaryaccountidentifier:))*