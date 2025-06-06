# AnyCancellable

**Framework**: Combine  
**Kind**: class

A type-erasing cancellable object that executes a provided closure when canceled.

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
final class AnyCancellable
```

## Mentions

- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md)

#### Overview

Subscriber implementations can use this type to provide a “cancellation token” that makes it possible for a caller to cancel a publisher, but not to use the [`Subscription`](subscription.md) object to request items.

An [`AnyCancellable`](anycancellable.md) instance automatically calls [`cancel()`](cancellable/cancel().md) when deinitialized.

## Topics

### Creating a Type-Erased Cancellable
- [init(() -> Void)](anycancellable/init(_:)-3icn3.md)
  Initializes the cancellable object with the given cancel-time closure.
### Canceling Actions
- [func cancel()](anycancellable/cancel.md)
  Cancel the activity.
### Storing AnyCancellable Instances
- [func store<C>(in: inout C)](anycancellable/store(in:)-6cr9i.md)
  Stores this type-erasing cancellable instance in the specified collection.
- [func store(in: inout Set<AnyCancellable>)](anycancellable/store(in:)-3hyxs.md)
  Stores this type-erasing cancellable instance in the specified set.
### Operators
- [static func == (AnyCancellable, AnyCancellable) -> Bool](anycancellable/==(_:_:).md)
  Returns a Boolean value that indicates whether two instances are equal, as determined by comparing whether their references point to the same instance.
### Initializers
- [init<C>(C)](anycancellable/init(_:)-48fh3.md)
### Instance Properties
- [var hashValue: Int](anycancellable/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](anycancellable/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](anycancellable/equatable-implementations.md)

## Relationships

### Conforms To
- [Cancellable](cancellable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol Publisher](publisher.md)
  Declares that a type can transmit a sequence of values over time.
- [enum Publishers](publishers.md)
  A namespace for types that serve as publishers.
- [struct AnyPublisher](anypublisher.md)
  A publisher that performs type erasure by wrapping another publisher.
- [struct Published](published.md)
  A type that publishes a property marked with an attribute.
- [protocol Cancellable](cancellable.md)
  A protocol indicating that an activity or action supports cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anycancellable)*