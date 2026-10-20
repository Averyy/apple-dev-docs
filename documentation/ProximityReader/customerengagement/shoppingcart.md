# CustomerEngagement.ShoppingCart

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A structure that describes the shopping cart content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct ShoppingCart
```

## Mentions

- [Adding support for Tap to Share to your app](../adding-support-for-tap-to-share-to-your-app.md)

## Topics

### Structures
- [CustomerEngagement.ShoppingCart.Item](./shoppingcart/item.md)
  An item in a shopping cart, including details like price and quantity.
- [CustomerEngagement.ShoppingCart.Summary](./shoppingcart/summary-swift.struct.md)
  A breakdown of totals, line items, and optional footer text for a shopping cart.
### Initializers
- [init(items: [CustomerEngagement.ShoppingCart.Item], summary: CustomerEngagement.ShoppingCart.Summary)](./shoppingcart/init%28items,summary%29.md)
  Creates a shopping cart summary.
### Instance Properties
- [let items: [CustomerEngagement.ShoppingCart.Item]](./shoppingcart/items.md)
  The items in the shopping cart.
- [let summary: CustomerEngagement.ShoppingCart.Summary](./shoppingcart/summary-swift.property.md)
  A summary section of the shopping cart.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting customer information
- [CustomerEngagement.Address](./address.md)
  A customer’s address collected during a customer engagement session.
- [CustomerEngagement.CustomerInfo](./customerinfo.md)
  A response structure that describes customer information.
- [CustomerEngagement.SignUp](./signup.md)
  Contact information and marketing consent selections a customer provides during a sign-up request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/shoppingcart)*