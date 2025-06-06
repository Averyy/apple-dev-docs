# automaticReloadBilling

**Framework**: Apple Pay on the Web  
**Kind**: property

A line item that contains the reload amount and balance threshold for the automatic reload payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required ApplePayLineItem automaticReloadBilling;
```

#### Discussion

This line item describes an automatic reload payment.

Set the [`automaticReloadPaymentThresholdAmount`](applepaylineitem/automaticreloadpaymentthresholdamount.md) to indicate the balance that the account drops below before the merchant applies the automatic reload amount. Set the [`amount`](applepaylineitem/amount.md) object to specify the reload amount.

> **Note**:  Set the [`paymentTiming`](applepaylineitem/paymenttiming.md) property of the line item to `"automaticReload"` to avoid an error.

 Set the [`paymentTiming`](applepaylineitem/paymenttiming.md) property of the line item to `"automaticReload"` to avoid an error.

## See Also

- [ApplePayLineItem](applepaylineitem.md)
  A line item in a payment request—for example, total, tax, discount, or grand total.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayautomaticreloadpaymentrequest/automaticreloadbilling)*