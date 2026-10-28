# paymentData

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The payment data as a UTF-8 encoded serialization of a JSON dictionary.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var paymentData: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * paymentData;
```

## Discussion

Send this data to your e-commerce back-end system, where it can be decrypted and submitted to your payment processor.

For the format of the payment data, see [Payment Token Format Reference](https://developer.apple.com/library/archive/documentation/PassKit/Reference/PaymentTokenJSON/PaymentTokenJSON.html#//apple_ref/doc/uid/TP40014929).

## See Also

### Related Documentation
- [Wallet Developer Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195)
### Working with payment tokens
- [var paymentMethod: PKPaymentMethod](./paymentmethod.md)
  Information about the card used in the transaction.
- [class PKPaymentMethod](../pkpaymentmethod.md)
  An object that contains information about payment methods.
- [var transactionIdentifier: String](./transactionidentifier.md)
  A unique identifier for this payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttoken/paymentdata)*