# updateStatus(_:)

**Framework**: ProximityReader  
**Kind**: method

Updates the status on the customer’s screen.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func updateStatus(_ status: CustomerEngagement.Status) async throws
```

## Mentions

- [Adding support for Tap to Share to your app](adding-support-for-tap-to-share-to-your-app.md)

#### Discussion

When there isn’t any form, like a sign-up form being displayed, the screen defaults to [`CustomerEngagement.Status.ready`](customerengagement/status/ready.md) unless there is a [`CustomerEngagement.ShoppingCart`](customerengagement/shoppingcart.md). [`CustomerEngagement.Status.ready`](customerengagement/status/ready.md) resets the default screen from [`CustomerEngagement.ShoppingCart`](customerengagement/shoppingcart.md).

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the request fails.

## Parameters

- `status`: An enum that defines a fixed status text which includes a title and a subtitle.

## See Also

- [func updateShoppingCart(CustomerEngagement.ShoppingCart) async throws -> CustomerEngagement.ShoppingCartToken](customerengagementsession/updateshoppingcart(_:).md)
  Updates the shopping cart on the customer’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/updatestatus(_:))*