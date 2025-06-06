# total

**Framework**: Applepayontheweb  
**Kind**: property

A line item that represents the total for the payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required ApplePayLineItem total;
```

## Mentions

- [Apple Pay on the Web Version 4 Release Notes](apple-pay-on-the-web-version-4-release-notes.md)

#### Discussion

See [`ApplePayLineItem`](applepaylineitem.md).

The [`amount`](applepaylineitem/amount.md) of the `total` must be greater than or equal to zero and the [`label`](applepaylineitem/label.md) must be non-empty to pass validation.

Provide a business name in the [`label`](applepaylineitem/label.md) field. Use the same business name people see when they look for the charge on their bank or credit card statement, for example, `“COMPANY, INC."`.

```javascript
"total": {
    "label": "COMPANY, INC.",
    "type": "final",
    "amount": "38.06"
}
```

> **Note**:  In versions of Apple Pay JS prior to version 4, the `amount` of the `total` must be greater than zero. Check for version availability using [`supportsVersion`](applepaysession/supportsversion.md) before setting a zero `amount`.

## See Also

- [lineItems](applepaypaymentrequest/lineitems.md)
  A set of line items that explain recurring payments and additional charges and discounts.
- [ApplePayLineItem](applepaylineitem.md)
  A line item in a payment request—for example, total, tax, discount, or grand total.
- [ApplePayLineItemType](applepaylineitemtype.md)
  A type that indicates whether a line item is final or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb/applepaypaymentrequest/total)*