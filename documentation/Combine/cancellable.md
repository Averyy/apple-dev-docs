# Cancellable

**Framework**: Combine  
**Kind**: protocol

A protocol indicating that an activity or action supports cancellation.

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
protocol Cancellable
```

## Mentions

- [Receiving and Handling Events with Combine](receiving-and-handling-events-with-combine.md)
- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md)

#### Overview

Calling [`cancel()`](cancellable/cancel().md) frees up any allocated resources. It also stops side effects such as timers, network access, or disk I/O.

## Topics

### Canceling actions
- [func cancel()](cancellable/cancel.md)
  Cancel the activity.
### Storing instances
- [func store<C>(in: inout C)](cancellable/store(in:)-35vnt.md)
  Stores this cancellable instance in the specified collection.
- [func store(in: inout Set<AnyCancellable>)](cancellable/store(in:)-95sfl.md)
  Stores this cancellable instance in the specified set.
### Instance Methods
- [func storeWhileEntityActive(Entity)](cancellable/storewhileentityactive(_:).md)
  Retains the `Cancellable` as long as the entity is active (see `Entity.isActive`). If the entity is deactivated, the `Cancellable` is released.

## Relationships

### Inherited By
- [Subscription](subscription.md)
### Conforming Types
- [AnyCancellable](anycancellable.md)
- [Subscribers.Assign](subscribers/assign.md)
- [Subscribers.Sink](subscribers/sink.md)

## See Also

- [protocol Publisher](publisher.md)
  Declares that a type can transmit a sequence of values over time.
- [enum Publishers](publishers.md)
  A namespace for types that serve as publishers.
- [struct AnyPublisher](anypublisher.md)
  A publisher that performs type erasure by wrapping another publisher.
- [struct Published](published.md)
  A type that publishes a property marked with an attribute.
- [class AnyCancellable](anycancellable.md)
  A type-erasing cancellable object that executes a provided closure when canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/cancellable)*