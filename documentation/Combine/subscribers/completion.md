# Subscribers.Completion

**Framework**: Combine  
**Kind**: enum  
**Role**: Enumeration

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

- [Receiving and Handling Events with Combine](../receiving-and-handling-events-with-combine.md)

## Topics

### Completion states
- [Subscribers.Completion.finished](./completion/finished.md)
  The publisher finished normally.
- [Subscribers.Completion.failure(_:)](./completion/failure%28_%29.md)
  The publisher stopped publishing due to the indicated error.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Receiving life cycle events
- [func receive(subscription: any Subscription)](../subscriber/receive%28subscription%29.md)
  Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [func receive(completion: Subscribers.Completion<Self.Failure>)](../subscriber/receive%28completion%29.md)
  Tells the subscriber that the publisher has completed publishing, either normally or with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/completion)*