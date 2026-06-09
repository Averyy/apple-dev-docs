# CustomerEngagement.ShoppingCart.Item

**Framework**: ProximityReader  
**Kind**: struct

An item in a shopping cart, including details like price and quantity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct Item
```

## Topics

### Initializers
- [init(id: String, name: String, quantity: Int, totalPrice: Decimal, totalAdjustedPrice: Decimal?, descriptions: [String], details: [String])](customerengagement/shoppingcart/item/init(id:name:quantity:totalprice:totaladjustedprice:descriptions:details:).md)
### Instance Properties
- [var descriptions: [String]](customerengagement/shoppingcart/item/descriptions.md)
  An array of description lines for this shopping cart item.
- [var details: [String]](customerengagement/shoppingcart/item/details.md)
  An array of detail lines for this shopping cart item.
- [let id: String](customerengagement/shoppingcart/item/id.md)
  A unique identifier of the shopping cart item.
- [var name: String](customerengagement/shoppingcart/item/name.md)
  The name of the shopping cart item.
- [var quantity: Int](customerengagement/shoppingcart/item/quantity.md)
  The total number of units that make up the line item.
- [var totalAdjustedPrice: Decimal?](customerengagement/shoppingcart/item/totaladjustedprice.md)
  A total adjusted price associated with the line item, typically used to indicate a price change.
- [var totalPrice: Decimal](customerengagement/shoppingcart/item/totalprice.md)
  A value indicating the total price of the item.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/shoppingcart/item)*