# CustomerEngagement.ShoppingCart.Summary.LineItem

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A label and value pair of text in the summary section.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct LineItem
```

## Topics

### Initializers
- [init(label: String, value: Decimal)](./lineitem/init%28label,value%29-3pcav.md)
  Creates a line item with a label and decimal value, formatted using the session currency and customer’s locale.
- [init(label: String, value: String)](./lineitem/init%28label,value%29-lf9.md)
  Creates a line item with the given label and string value.
### Instance Properties
- [let label: String](./lineitem/label.md)
  The summary line label.
- [let value: CustomerEngagement.ShoppingCart.Summary.LineItem.Value](./lineitem/value-swift.property.md)
  The stored string or decimal representation of the line item.
### Enumerations
- [CustomerEngagement.ShoppingCart.Summary.LineItem.Value](./lineitem/value-swift.enum.md)
  A value that holds either a [`String`](../../../../Swift/string.md) or `[`Decimal`](../../../../Foundation/decimal.md) amount for a summary line item.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/shoppingcart/summary-swift.struct/lineitem)*