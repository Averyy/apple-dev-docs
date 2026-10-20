# activate(_:withActivationData:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Activates a payment pass using the provided activation code.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.12+
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`activate(_:activationData:completion:)`](./activate%28_,activationdata,completion%29.md) instead.

## Declaration

```swift
func activate(_ paymentPass: PKPaymentPass, withActivationData activationData: Data, completion: ((Bool, any Error) -> Void)? = nil)
```

```objc
- (void) activatePaymentPass:(PKPaymentPass *) paymentPass withActivationData:(NSData *) activationData completion:(void (^)(BOOL success, NSError *error)) completion;
```

#### Discussion

You can only activate a provisioned pass, and it must be in the [`PKPaymentPassActivationState.requiresActivation`](../pkpaymentpassactivationstate/requiresactivation.md) state.

> ❗ **Important**:  Activating payment passes requires a special entitlement issued from Apple. For more information, see [developer.apple.com/apple-pay/](https://developer.apple.com/apple-pay/).

## Parameters

- `paymentPass`: The payment pass to activate.
- `activationData`: The one-time cryptographic password.

  PassKit encodes the data as Base64 and then sends it to the payment network. The framework treats this data as an opaque value.
- `completion`: The completion block that PassKit calls after activation.

  This block takes the following parameters:

  - **`success`**: [`true`](../../Swift/true.md) if the authorization succeeds; otherwise, [`false`](../../Swift/false.md).
  - **`error`**: If `success` is [`false`](../../Swift/false.md), a description of the error.

## See Also

### Deprecated Methods
- [func activate(PKPaymentPass, withActivationCode: String, completion: ((Bool, any Error) -> Void)?)](./activate%28_,withactivationcode,completion%29.md)
  Activates a payment pass using the provided activation code.
- [func canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](./canaddpaymentpass%28withprimaryaccountidentifier%29.md)
  A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.
- [class func isPaymentPassActivationAvailable() -> Bool](./ispaymentpassactivationavailable%28%29-swift.type.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func isPaymentPassActivationAvailable() -> Bool](./ispaymentpassactivationavailable%28%29-swift.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func present(PKPaymentPass)](./present%28_%29-67jce.md)
  Presents the payment pass for use in-store.
- [func remotePaymentPasses() -> [PKPaymentPass]](./remotepaymentpasses%28%29.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/activate(_:withactivationdata:completion:))*