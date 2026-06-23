# updateShoppingCart(_:)

**Framework**: ProximityReader  
**Kind**: method

Updates the shopping cart on the customer’s device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func updateShoppingCart(_ shoppingCart: CustomerEngagement.ShoppingCart) async throws -> CustomerEngagement.ShoppingCartToken
```

#### Return Value

[`CustomerEngagement.ShoppingCartToken`](customerengagement/shoppingcarttoken.md) for making payment request using [`requestPayment(for:using:delegate:)`](customerengagementsession/requestpayment(for:using:delegate:).md).

#### Discussion

This function can be called repeatedly as the shopping cart is populated, and each update replaces the entire shopping cart.

When there isn’t any form, like a sign-up form being displayed, the screen defaults to the current [`CustomerEngagement.ShoppingCart`](customerengagement/shoppingcart.md).

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the request fails.

## Parameters

- `shoppingCart`: A structure of the shopping cart, consisting of shopping cart items and the summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/updateshoppingcart(_:))*