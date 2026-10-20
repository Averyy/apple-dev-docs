# trialBilling

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

The trial billing cycle for the recurring payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
ApplePayLineItem trialBilling;
```

#### Discussion

The trial billing cycle is optional; use it if the recurring payment has a trial period.

> **Note**:  Set the [`paymentTiming`](../applepaylineitem/paymenttiming.md) property of the line item to `"recurring"` to avoid an error.

## See Also

### Setting the payment summary items
- [regularBilling](./regularbilling.md)
  The regular billing cycle for the recurring payment, including start and end dates, an interval, and an interval count.
- [ApplePayLineItem](../applepaylineitem.md)
  A line item in a payment request—for example, total, tax, discount, or grand total.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrecurringpaymentrequest/trialbilling)*