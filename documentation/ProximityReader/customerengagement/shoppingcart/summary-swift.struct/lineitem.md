# CustomerEngagement.ShoppingCart.Summary.LineItem

**Framework**: ProximityReader  
**Kind**: struct

A label and value pair of text in the summary section.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct LineItem
```

## Topics

### Initializers
- [init(label: String, value: Decimal)](customerengagement/shoppingcart/summary-swift.struct/lineitem/init(label:value:)-3pcav.md)
  Creates a line item with a label and decimal value, formatted using the session currency and customer’s locale.
- [init(label: String, value: String)](customerengagement/shoppingcart/summary-swift.struct/lineitem/init(label:value:)-lf9.md)
  Creates a line item with the given label and string value.
### Instance Properties
- [let label: String](customerengagement/shoppingcart/summary-swift.struct/lineitem/label.md)
  The summary line label.
- [let value: CustomerEngagement.ShoppingCart.Summary.LineItem.Value](customerengagement/shoppingcart/summary-swift.struct/lineitem/value-swift.property.md)
  The stored string or decimal representation of the line item.
### Enumerations
- [CustomerEngagement.ShoppingCart.Summary.LineItem.Value](customerengagement/shoppingcart/summary-swift.struct/lineitem/value-swift.enum.md)
  A value that holds either a [`String`](https://developer.apple.com/documentation/swift/string) or `[`Decimal`](https://developer.apple.com/documentation/foundation/decimal) amount for a summary line item.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/shoppingcart/summary-swift.struct/lineitem)*