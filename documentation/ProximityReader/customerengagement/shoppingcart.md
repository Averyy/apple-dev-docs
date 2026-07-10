# CustomerEngagement.ShoppingCart

**Framework**: ProximityReader  
**Kind**: struct

A structure that describes the shopping cart content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct ShoppingCart
```

## Mentions

- [Adding support for Tap to Share to your app](adding-support-for-tap-to-share-to-your-app.md)

## Topics

### Structures
- [CustomerEngagement.ShoppingCart.Item](customerengagement/shoppingcart/item.md)
  An item in a shopping cart, including details like price and quantity.
- [CustomerEngagement.ShoppingCart.Summary](customerengagement/shoppingcart/summary-swift.struct.md)
  A breakdown of totals, line items, and optional footer text for a shopping cart.
### Initializers
- [init(items: [CustomerEngagement.ShoppingCart.Item], summary: CustomerEngagement.ShoppingCart.Summary)](customerengagement/shoppingcart/init(items:summary:).md)
  Creates a shopping cart summary.
### Instance Properties
- [let items: [CustomerEngagement.ShoppingCart.Item]](customerengagement/shoppingcart/items.md)
  The items in the shopping cart.
- [let summary: CustomerEngagement.ShoppingCart.Summary](customerengagement/shoppingcart/summary-swift.property.md)
  A summary section of the shopping cart.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CustomerEngagement.Address](customerengagement/address.md)
  A customer’s address collected during a customer engagement session.
- [CustomerEngagement.CustomerInfo](customerengagement/customerinfo.md)
  A response structure that describes customer information.
- [CustomerEngagement.SignUp](customerengagement/signup.md)
  Contact information and marketing consent selections a customer provides during a sign-up request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/shoppingcart)*