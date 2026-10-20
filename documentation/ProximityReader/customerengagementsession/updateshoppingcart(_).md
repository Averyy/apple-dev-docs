# updateShoppingCart(_:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Instance Method

Updates the shopping cart on the customer’s device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
final func updateShoppingCart(_ shoppingCart: CustomerEngagement.ShoppingCart) async throws -> CustomerEngagement.ShoppingCartToken
```

## Mentions

- [Adding support for Tap to Share to your app](../adding-support-for-tap-to-share-to-your-app.md)

#### Return Value

[`CustomerEngagement.ShoppingCartToken`](../customerengagement/shoppingcarttoken.md) for making payment request using [`requestPayment(for:using:delegate:)`](./requestpayment%28for,using,delegate%29.md).

#### Discussion

This function can be called repeatedly as the shopping cart is populated, and each update replaces the entire shopping cart.

When there isn’t any form, like a sign-up form being displayed, the screen defaults to the current [`CustomerEngagement.ShoppingCart`](../customerengagement/shoppingcart.md).

> **Throws**: [`CustomerEngagementSession.Error`](./error.md) if the request fails.

## Parameters

- `shoppingCart`: A structure of the shopping cart, consisting of shopping cart items and the summary.

## See Also

### Updating the customer status and cart
- [func updateStatus(CustomerEngagement.Status) async throws](./updatestatus%28_%29.md)
  Updates the status on the customer’s screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/updateshoppingcart(_:))*