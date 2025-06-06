# receive(subscription:)

**Framework**: Combine  
**Kind**: method

Tells the subscriber that it has successfully subscribed to the publisher and may request items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
final func receive(subscription: any Subscription)
```

#### Discussion

Use the received [`Subscription`](subscription.md) to request items from the publisher.

## Parameters

- `subscription`: A subscription that represents the connection between publisher and subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/sink/receive(subscription:))*