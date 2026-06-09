# CustomerEngagement.ShoppingCart.Summary

**Framework**: ProximityReader  
**Kind**: struct

A breakdown of totals, line items, and optional footer text for a shopping cart.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct Summary
```

## Topics

### Structures
- [CustomerEngagement.ShoppingCart.Summary.LineItem](customerengagement/shoppingcart/summary-swift.struct/lineitem.md)
  A label and value pair of text in the summary section.
### Initializers
- [init(summaryLines: [CustomerEngagement.ShoppingCart.Summary.LineItem], footer: String?, total: Decimal)](customerengagement/shoppingcart/summary-swift.struct/init(summarylines:footer:total:).md)
### Instance Properties
- [let footer: String?](customerengagement/shoppingcart/summary-swift.struct/footer.md)
  A multiline text at the bottom of the summary section.
- [let summaryLines: [CustomerEngagement.ShoppingCart.Summary.LineItem]](customerengagement/shoppingcart/summary-swift.struct/summarylines.md)
  An array of label-value pairs listing taxes, discounts, or other cart-level entries in the summary. These entries apply to the entire cart rather than individual line items.
- [let total: Decimal](customerengagement/shoppingcart/summary-swift.struct/total.md)
  A decimal value indicating the total amount of the shopping cart.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/shoppingcart/summary-swift.struct)*