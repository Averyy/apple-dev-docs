# type

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether the line item is final or pending.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
ApplePayLineItemType type;
```

#### Discussion

See [`ApplePayLineItemType`](../applepaylineitemtype.md) for valid values.

The default value is `final`.

Note that if a line item’s [`type`](./type.md) is `pending`, the Apple Pay payment sheet doesn’t display the value in [`amount`](./amount.md), and instead displays “pending”.

If a line item’s [`type`](./type.md) is `final`, the payment sheet displays the value in [`amount`](./amount.md).

## Topics

### Line Item Type
- [ApplePayLineItemType](../applepaylineitemtype.md)
  A type that indicates whether a line item is final or pending.

## See Also

### Setting line item properties
- [label](./label.md)
  A required value that’s a short, localized description of the line item.
- [amount](./amount.md)
  A required value that’s the monetary amount of the line item.
- [ApplePayLineItemType](../applepaylineitemtype.md)
  A type that indicates whether a line item is final or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaylineitem/type)*