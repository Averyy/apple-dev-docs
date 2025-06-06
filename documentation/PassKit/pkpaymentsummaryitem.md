# PKPaymentSummaryItem

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKPaymentSummaryItem
```

#### Overview

For shipping cost, use the [`PKShippingMethod`](pkshippingmethod.md) subclass.

## Topics

### Creating  summary items
- [convenience init(label: String, amount: NSDecimalNumber)](pkpaymentsummaryitem/init(label:amount:).md)
  Initializes and returns a summary item with the given label and amount.
- [convenience init(label: String, amount: NSDecimalNumber, type: PKPaymentSummaryItemType)](pkpaymentsummaryitem/init(label:amount:type:).md)
  Initializes and returns a summary item with the given label, amount, and type.
### Describing summary items
- [var label: String](pkpaymentsummaryitem/label.md)
  A short, localized description of the item.
- [var amount: NSDecimalNumber](pkpaymentsummaryitem/amount.md)
  The summary item’s amount.
- [var type: PKPaymentSummaryItemType](pkpaymentsummaryitem/type.md)
  The summary item’s type that indicates whether the amount is final.
- [enum PKPaymentSummaryItemType](pkpaymentsummaryitemtype.md)
  Constants that describe the type of the payment summary item, such as final or pending.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PKAutomaticReloadPaymentSummaryItem](pkautomaticreloadpaymentsummaryitem.md)
- [PKDeferredPaymentSummaryItem](pkdeferredpaymentsummaryitem.md)
- [PKDisbursementSummaryItem](pkdisbursementsummaryitem.md)
- [PKInstantFundsOutFeeSummaryItem](pkinstantfundsoutfeesummaryitem.md)
- [PKRecurringPaymentSummaryItem](pkrecurringpaymentsummaryitem.md)
- [PKShippingMethod](pkshippingmethod.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var summaryItems: [PKPaymentSummaryItem]](pkdisbursementrequest/summaryitems.md)
  An array of payment summary item objects that the framework presents to people.
- [class PKDisbursementSummaryItem](pkdisbursementsummaryitem.md)
  A summary item that represents a disbursement.
- [class PKInstantFundsOutFeeSummaryItem](pkinstantfundsoutfeesummaryitem.md)
  A summary item that represents a fee for an instant funds out transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentsummaryitem)*