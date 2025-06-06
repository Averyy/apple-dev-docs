# send(subscription:)

**Framework**: Combine  
**Kind**: method

Sends a subscription to the subscriber.

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
final func send(subscription: any Subscription)
```

#### Discussion

This call provides the [`Subject`](subject.md) an opportunity to establish demand for any new upstream subscriptions.

## Parameters

- `subscription`: The subscription instance through which the subscriber can request elements.

## See Also

- [func send(completion: Subscribers.Completion<Failure>)](currentvaluesubject/send(completion:).md)
  Sends a completion signal to the subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/currentvaluesubject/send(subscription:))*