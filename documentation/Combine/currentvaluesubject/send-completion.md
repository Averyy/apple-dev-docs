# send(completion:)

**Framework**: Combine  
**Kind**: method

Sends a completion signal to the subscriber.

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
final func send(completion: Subscribers.Completion<Failure>)
```

## Parameters

- `completion`: A   instance which indicates whether publishing has finished normally or failed with an error.

## See Also

- [func send(subscription: any Subscription)](currentvaluesubject/send(subscription:).md)
  Sends a subscription to the subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/currentvaluesubject/send(completion:))*