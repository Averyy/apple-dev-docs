# paymentMethod

**Framework**: Apple Pay on the Web  
**Kind**: property

The card used to complete a payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
readonly attribute ApplePayPaymentMethod paymentMethod;
```

#### Discussion

See [`ApplePayPaymentMethod`](applepaypaymentmethod.md). For privacy reasons, only the `type` property ([`ApplePayPaymentMethodType`](applepaypaymentmethodtype.md)) is provided in most cases before the user authorizes the transaction.

This attribute is contained by the [`onpaymentmethodselected`](applepaysession/onpaymentmethodselected.md) event. Access this attribute using the event parameter in the callback function; for example, `var myPaymentMethod = event.paymentMethod;`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodselectedevent/paymentmethod)*