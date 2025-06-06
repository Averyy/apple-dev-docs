# PKPaymentSummaryItemType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Constants that describe the type of the payment summary item, such as final or pending.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum PKPaymentSummaryItemType
```

## Topics

### Payment summary item types
- [PKPaymentSummaryItemType.final](pkpaymentsummaryitemtype/final.md)
  A summary item that represents a known, final cost.
- [PKPaymentSummaryItemType.pending](pkpaymentsummaryitemtype/pending.md)
  A summary item that represents an estimated or unknown cost.
### Initializers
- [init?(rawValue: UInt)](pkpaymentsummaryitemtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var label: String](pkpaymentsummaryitem/label.md)
  A short, localized description of the item.
- [var amount: NSDecimalNumber](pkpaymentsummaryitem/amount.md)
  The summary item’s amount.
- [var type: PKPaymentSummaryItemType](pkpaymentsummaryitem/type.md)
  The summary item’s type that indicates whether the amount is final.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitemtype)*