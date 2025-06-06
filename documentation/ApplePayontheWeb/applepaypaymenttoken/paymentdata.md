# paymentData

**Framework**: Apple Pay on the Web  
**Kind**: property

An object containing the encrypted payment data.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
JSON paymentData;
```

#### Discussion

This data is used by your e-commerce back-end system, which decrypts it and submits it to your payment processor.

For the format of the payment data, see [`Payment token format reference`](https://developer.apple.com/documentation/PassKit/payment-token-format-reference).

## See Also

- [paymentMethod](applepaypaymenttoken/paymentmethod.md)
  Information about the card used in the transaction.
- [transactionIdentifier](applepaypaymenttoken/transactionidentifier.md)
  A unique identifier for this payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymenttoken/paymentdata)*