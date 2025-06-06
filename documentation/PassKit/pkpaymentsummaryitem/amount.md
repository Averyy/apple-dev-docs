# amount

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The summary item’s amount.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var amount: NSDecimalNumber { get set }
```

#### Discussion

The amount’s currency is specified at the payment level by setting a value for the [`currencyCode`](pkpaymentrequest/currencycode.md) property on [`PKPaymentRequest`](pkpaymentrequest.md).

## See Also

- [var label: String](pkpaymentsummaryitem/label.md)
  A short, localized description of the item.
- [var type: PKPaymentSummaryItemType](pkpaymentsummaryitem/type.md)
  The summary item’s type that indicates whether the amount is final.
- [enum PKPaymentSummaryItemType](pkpaymentsummaryitemtype.md)
  Constants that describe the type of the payment summary item, such as final or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/amount)*