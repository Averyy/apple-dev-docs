# payment

**Framework**: Apple Pay on the Web  
**Kind**: property

The authorized payment information for this transaction.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
readonly attribute ApplePayPayment payment;
```

#### Discussion

This attribute is contained by the [`onpaymentauthorized`](applepaysession/onpaymentauthorized.md) event. Access this attribute using the event parameter in the callback function; for example, `var payinfo = event.payment;`.

[`ApplePayPayment`](applepaypayment.md)  contains `billingContact` and `shippingContact` if they were requested, and it also contains [`ApplePayPaymentToken`](applepaypaymenttoken.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentauthorizedevent/payment)*