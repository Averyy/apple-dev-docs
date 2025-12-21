# AnyPublisher

**Framework**: Combine  
**Kind**: struct

A publisher that performs type erasure by wrapping another publisher.

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
struct AnyPublisher<Output, Failure> where Failure : Error
```

## Mentions

- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

#### Overview

[`AnyPublisher`](anypublisher.md) is a concrete implementation of [`Publisher`](publisher.md) that has no significant properties of its own, and passes through elements and completion values from its upstream publisher.

Use [`AnyPublisher`](anypublisher.md) to wrap a publisher whose type has details you don’t want to expose across API boundaries, such as different modules. Wrapping a [`Subject`](subject.md) with [`AnyPublisher`](anypublisher.md) also prevents callers from accessing its [`send(_:)`](subject/send(_:).md) method. When you use type erasure this way, you can change the underlying publisher implementation over time without affecting existing clients.

You can use Combine’s [`eraseToAnyPublisher()`](publisher/erasetoanypublisher().md) operator to wrap a publisher with [`AnyPublisher`](anypublisher.md).

## Topics

### Creating a type-erased publisher
- [init<P>(P)](anypublisher/init(_:).md)
  Creates a type-erasing publisher to wrap the provided publisher.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Publisher](publisher.md)

## See Also

- [protocol Publisher](publisher.md)
  Declares that a type can transmit a sequence of values over time.
- [enum Publishers](publishers.md)
  A namespace for types that serve as publishers.
- [struct Published](published.md)
  A type that publishes a property marked with an attribute.
- [protocol Cancellable](cancellable.md)
  A protocol indicating that an activity or action supports cancellation.
- [class AnyCancellable](anycancellable.md)
  A type-erasing cancellable object that executes a provided closure when canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anypublisher)*