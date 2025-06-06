# label

**Framework**: Apple Pay on the Web  
**Kind**: property

A required value that’s a short, localized description of the line item.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString label;
```

#### Discussion

Provide the label in title case—for example, VAT Tax, Gift Wrap and Card, or Discount. The label can’t be empty.

Omit any punctuation and whitespace after the label. The framework formats the label for display.

## See Also

- [amount](applepaylineitem/amount.md)
  A required value that’s the monetary amount of the line item.
- [type](applepaylineitem/type.md)
  A value that indicates whether the line item is final or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaylineitem/label)*