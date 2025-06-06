# receive(completion:)

**Framework**: Combine  
**Kind**: method  
**Required**: Yes

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
func receive(completion: Subscribers.Completion<Self.Failure>)
```

## Parameters

- `completion`: A   case indicating whether publishing completed normally or with an error.

## See Also

- [func receive(subscription: any Subscription)](subscriber/receive(subscription:).md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [Subscribers.Completion](subscribers/completion.md)
  A signal that a publisher doesn’t produce additional elements, either due to normal completion or an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscriber/receive(completion:))*