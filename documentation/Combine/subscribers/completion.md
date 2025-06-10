# Subscribers.Completion

**Framework**: Combine  
**Kind**: enum

A signal that a publisher doesn’t produce additional elements, either due to normal completion or an error.

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
@frozen
enum Completion<Failure> where Failure : Error
```

## Mentions

- [Receiving and Handling Events with Combine](receiving-and-handling-events-with-combine.md)

## Topics

### Completion States
- [Subscribers.Completion.finished](subscribers/completion/finished.md)
  The publisher finished normally.
- [Subscribers.Completion.failure(_:)](subscribers/completion/failure(_:).md)
  The publisher stopped publishing due to the indicated error.
### Default Implementations
- [Decodable Implementations](subscribers/completion/decodable-implementations.md)
- [Encodable Implementations](subscribers/completion/encodable-implementations.md)
- [Equatable Implementations](subscribers/completion/equatable-implementations.md)
- [Hashable Implementations](subscribers/completion/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func receive(subscription: any Subscription)](subscriber/receive(subscription:).md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [func receive(completion: Subscribers.Completion<Self.Failure>)](subscriber/receive(completion:).md)
  Tells the subscriber that the publisher has completed publishing, either normally or with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/completion)*