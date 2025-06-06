# lineItems

**Framework**: Apple Pay on the Web  
**Kind**: property

A set of line items that explain recurring payments and additional charges and discounts.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <ApplePayLineItem> lineItems;
```

#### Discussion

See [`ApplePayLineItem`](applepaylineitem.md).

Use [`lineItems`](applepaypaymentrequest/lineitems.md) to explain additional charges, discounts, and pending costs. Provide the total separately, in the [`total`](applepaypaymentrequest/total.md) property. Line items aren’t required in a [`ApplePayPaymentRequest`](applepaypaymentrequest.md), but can’t be empty if they’re present.

The following listing shows line items that include a subtotal, free shipping, and estimated tax.

```javascript
"lineItems": [
    {
        "label": "Bag Subtotal",
        "type": "final",
        "amount": "35.00"
    },
    {
        "label": "Free Shipping",
        "amount": "0.00",
        "type": "final"
    },
    {
        "label": "Estimated Tax",
        "amount": "3.06",
        "type": "final"
    }
]
```

The resulting payment sheet looks like:

![An Apple Pay payment sheet that shows card and billing information, shipping information, a shipping method, contact information, and the three line items shown in the related code listing which include a Bag Subtotal of $35, Free Shipping, and Estimated Tax of $3.06. The total is $38.06.](https://docs-assets.developer.apple.com/published/1fa91fd144f00a52f69d21dadb96de2a/media-2936386%402x.png)

## See Also

- [total](applepaypaymentrequest/total.md)
  A line item that represents the total for the payment.
- [ApplePayLineItem](applepaylineitem.md)
  A line item in a payment request—for example, total, tax, discount, or grand total.
- [ApplePayLineItemType](applepaylineitemtype.md)
  A type that indicates whether a line item is final or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/lineitems)*