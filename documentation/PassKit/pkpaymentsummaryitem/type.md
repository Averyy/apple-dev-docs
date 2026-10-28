# type

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The summary item’s type that indicates whether the amount is final.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var type: PKPaymentSummaryItemType { get set }
```

```objc
@property (nonatomic, assign) PKPaymentSummaryItemType type;
```

## Discussion

This property defaults to a [`PKPaymentSummaryItemType.final`](../pkpaymentsummaryitemtype/final.md) type. See [`PKPaymentSummaryItemType`](../pkpaymentsummaryitemtype.md) for other values.

## See Also

### Describing summary items
- [var label: String](./label.md)
  A short, localized description of the item.
- [var amount: NSDecimalNumber](./amount.md)
  The summary item’s amount.
- [enum PKPaymentSummaryItemType](../pkpaymentsummaryitemtype.md)
  Constants that describe the type of the payment summary item, such as final or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/type)*