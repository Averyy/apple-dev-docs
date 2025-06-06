# amount

**Framework**: Apple Pay on the Web  
**Kind**: property

A required value that’s the monetary amount of the line item.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString amount;
```

#### Discussion

This number must follow the regular expression `-?[0-9]+(\.[0-9][0-9])?`. The amount is required and can’t be empty.

You specify the currency for the entire transaction including line items by setting the [`currencyCode`](applepaypaymentrequest/currencycode.md) property in [`ApplePayPaymentRequest`](applepaypaymentrequest.md).

If the payment request is for an automatic reload payment, the `amount` indicates the reload payment amount authorized when the account drops below the ``/ApplePayontheWeb/ApplePayLineItem/automaticReloadPaymentThresholdAmount```.`

## See Also

- [label](applepaylineitem/label.md)
  A required value that’s a short, localized description of the line item.
- [type](applepaylineitem/type.md)
  A value that indicates whether the line item is final or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaylineitem/amount)*