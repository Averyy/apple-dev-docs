# label

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A short, localized description of the item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var label: String { get set }
```

#### Discussion

Provide the label in title case—for example, VAT Tax, Gift Wrap and Card, or Discount.

Omit any punctuation and whitespace after the label. The label is formatted for display by the framework.

## See Also

- [var amount: NSDecimalNumber](pkpaymentsummaryitem/amount.md)
  The summary item’s amount.
- [var type: PKPaymentSummaryItemType](pkpaymentsummaryitem/type.md)
  The summary item’s type that indicates whether the amount is final.
- [enum PKPaymentSummaryItemType](pkpaymentsummaryitemtype.md)
  Constants that describe the type of the payment summary item, such as final or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/label)*