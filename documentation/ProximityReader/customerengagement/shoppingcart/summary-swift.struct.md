# CustomerEngagement.ShoppingCart.Summary

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A breakdown of totals, line items, and optional footer text for a shopping cart.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct Summary
```

## Topics

### Structures
- [CustomerEngagement.ShoppingCart.Summary.LineItem](./summary-swift.struct/lineitem.md)
  A label and value pair of text in the summary section.
### Initializers
- [init(summaryLines: [CustomerEngagement.ShoppingCart.Summary.LineItem], footer: String?, total: Decimal)](./summary-swift.struct/init%28summarylines,footer,total%29.md)
### Instance Properties
- [let footer: String?](./summary-swift.struct/footer.md)
  A multiline text at the bottom of the summary section.
- [let summaryLines: [CustomerEngagement.ShoppingCart.Summary.LineItem]](./summary-swift.struct/summarylines.md)
  An array of label-value pairs listing taxes, discounts, or other cart-level entries in the summary. These entries apply to the entire cart rather than individual line items.
- [let total: Decimal](./summary-swift.struct/total.md)
  A decimal value indicating the total amount of the shopping cart.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/shoppingcart/summary-swift.struct)*