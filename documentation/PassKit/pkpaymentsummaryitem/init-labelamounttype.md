# init(label:amount:type:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Initializes and returns a summary item with the given label, amount, and type.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(label: String, amount: NSDecimalNumber, type: PKPaymentSummaryItemType)
```

#### Return Value

A summary item with the given label, amount, and type.

#### Discussion

When creating summary items for estimates or charges whose final value isn’t yet known, use a [`PKPaymentSummaryItemType.pending`](pkpaymentsummaryitemtype/pending.md) type. Use [`zero`](https://developer.apple.com/documentation/foundation/nsdecimalnumber/1413127-zero) for the amount of pending items. The payment sheet doesn’t show the value of pending items.

> **Note**:  The payment request’s total must include a final value, even if the payment request includes one or more pending summary items. This total represents the total of all the known costs; don’t include the value of any pending items.

 The payment request’s total must include a final value, even if the payment request includes one or more pending summary items. This total represents the total of all the known costs; don’t include the value of any pending items.

## Parameters

- `label`: A short, localized description of the summary item.
- `amount`: The amount associated with the summary item.
- `type`: The type of the summary item.

## See Also

- [convenience init(label: String, amount: NSDecimalNumber)](pkpaymentsummaryitem/init(label:amount:).md)
  Initializes and returns a summary item with the given label and amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem/init(label:amount:type:))*