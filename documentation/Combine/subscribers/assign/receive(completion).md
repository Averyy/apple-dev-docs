# receive(completion:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Tells the subscriber that the publisher has completed publishing, either normally or with an error.

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
final func receive(completion: Subscribers.Completion<Never>)
```

## Parameters

- `completion`: A [`Subscribers.Completion`](../completion.md) case indicating whether publishing completed normally or with an error.

## See Also

### Receiving life cycle events
- [func receive(subscription: any Subscription)](./receive%28subscription%29.md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/assign/receive(completion:))*