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

#### Discussion

When there isn’t any form, like a sign-up form being displayed, the screen defaults to [`CustomerEngagement.Status.ready`](customerengagement/status/ready.md) unless there is a [`CustomerEngagement.ShoppingCart`](customerengagement/shoppingcart.md). [`CustomerEngagement.Status.ready`](customerengagement/status/ready.md) resets the default screen from [`CustomerEngagement.ShoppingCart`](customerengagement/shoppingcart.md).

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the request fails.

## Parameters

- `status`: An enum that defines a fixed status text which includes a title and a subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/updatestatus(_:))*