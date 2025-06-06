# init(label:amount:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Initializes and returns a summary item with the given label and amount.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(label: String, amount: NSDecimalNumber)
```

#### Return Value

A summary item with the given label and amount. The resulting item has a [`PKPaymentSummaryItemType.final`](pkpaymentsummaryitemtype/final.md) type.

## Parameters

- `label`: A short, localized description of the summary item.
- `amount`: The amount associated with the summary item.

## See Also

- [convenience init(label: String, amount: NSDecimalNumber, type: PKPaymentSummaryItemType)](pkpaymentsummaryitem/init(label:amount:type:).md)
  Initializes and returns a summary item with the given label, amount, and type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/init(label:amount:))*