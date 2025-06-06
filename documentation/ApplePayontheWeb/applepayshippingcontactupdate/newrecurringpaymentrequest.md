# newRecurringPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: property

An updated request for a recurring payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayRecurringPaymentRequest newRecurringPaymentRequest;
```

#### Discussion

Provide this object to update the [`recurringPaymentRequest`](applepaypaymentrequest/recurringpaymentrequest.md) value in the original [`ApplePayPaymentRequest`](applepaypaymentrequest.md), if necessary, after the user updated their shipping contact information.

## See Also

- [ApplePayRecurringPaymentRequest](applepayrecurringpaymentrequest.md)
  A dictionary that represents a request to set up a recurring payment, typically a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingcontactupdate/newrecurringpaymentrequest)*