# isPaymentPassActivationAvailable()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the device supports adding payment passes.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`isSecureElementPassActivationAvailable`](./issecureelementpassactivationavailable.md) instead.

## Declaration

```swift
class func isPaymentPassActivationAvailable() -> Bool
```

```objc
+ (BOOL) isPaymentPassActivationAvailable;
```

## Return Value

[`true`](../../Swift/true.md) if the device supports adding payment passes.

## See Also

### Deprecated Methods
- [func activate(PKPaymentPass, withActivationCode: String, completion: ((Bool, any Error) -> Void)?)](./activate%28_,withactivationcode,completion%29.md)
  Activates a payment pass using the provided activation code.
- [func activate(PKPaymentPass, withActivationData: Data, completion: ((Bool, any Error) -> Void)?)](./activate%28_,withactivationdata,completion%29.md)
  Activates a payment pass using the provided activation code.
- [func canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](./canaddpaymentpass%28withprimaryaccountidentifier%29.md)
  A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.
- [func isPaymentPassActivationAvailable() -> Bool](./ispaymentpassactivationavailable%28%29-swift.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func present(PKPaymentPass)](./present%28_%29-67jce.md)
  Presents the payment pass for use in-store.
- [func remotePaymentPasses() -> [PKPaymentPass]](./remotepaymentpasses%28%29.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/ispaymentpassactivationavailable()-swift.type.method)*