# regularBilling

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

The regular billing cycle for the recurring payment, including start and end dates, an interval, and an interval count.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
required ApplePayLineItem regularBilling;
```

#### Discussion

This line item applies to a regular billing cycle for a recurring payment.

> **Note**:  Set the [`paymentTiming`](../applepaylineitem/paymenttiming.md) property of the line item to `"recurring"` to avoid an error.

## See Also

### Setting the payment summary items
- [trialBilling](./trialbilling.md)
  The trial billing cycle for the recurring payment.
- [ApplePayLineItem](../applepaylineitem.md)
  A line item in a payment request—for example, total, tax, discount, or grand total.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrecurringpaymentrequest/regularbilling)*