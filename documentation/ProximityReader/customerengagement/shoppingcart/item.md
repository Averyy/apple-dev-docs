# CustomerEngagement.ShoppingCart.Item

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

An item in a shopping cart, including details like price and quantity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct Item
```

## Topics

### Initializers
- [init(id: String, name: String, quantity: Int, totalPrice: Decimal, totalAdjustedPrice: Decimal?, descriptions: [String], details: [String])](./item/init%28id,name,quantity,totalprice,totaladjustedprice,descriptions,details%29.md)
### Instance Properties
- [var descriptions: [String]](./item/descriptions.md)
  An array of description lines for this shopping cart item.
- [var details: [String]](./item/details.md)
  An array of detail lines for this shopping cart item.
- [let id: String](./item/id.md)
  A unique identifier of the shopping cart item.
- [var name: String](./item/name.md)
  The name of the shopping cart item.
- [var quantity: Int](./item/quantity.md)
  The total number of units that make up the line item.
- [var totalAdjustedPrice: Decimal?](./item/totaladjustedprice.md)
  A total adjusted price associated with the line item, typically used to indicate a price change.
- [var totalPrice: Decimal](./item/totalprice.md)
  A value indicating the total price of the item.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/shoppingcart/item)*