# AsyncPublisher

**Framework**: Combine  
**Kind**: struct

A publisher that exposes its elements as an asynchronous sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct AsyncPublisher<P> where P : Publisher, P.Failure == Never
```

#### Overview

`AsyncPublisher` conforms to [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), which allows callers to receive values with the `for`-`await`-`in` syntax, rather than attaching a [`Subscriber`](subscriber.md).

Use the [`values`](publisher/values-1dm9r.md) property of the [`Publisher`](publisher.md) protocol to wrap an existing publisher with an instance of this type.

## Topics

### Creating an Asynchronous Publisher
- [init(_:)](asyncpublisher/init(_:).md)
  Creates a publisher that exposes elements received from an upstream publisher as an asynchronous sequence.
### Creating an Iterator
- [func makeAsyncIterator() -> AsyncPublisher<P>.Iterator](asyncpublisher/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncPublisher.Iterator](asyncpublisher/iterator.md)
  The iterator that produces elements of the asynchronous publisher sequence.
### Supporting Types
- [AsyncPublisher.Element](asyncpublisher/element.md)
  The type of element produced by this asynchronous sequence.
### Type Aliases
- [AsyncPublisher.AsyncIterator](asyncpublisher/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](asyncpublisher/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [struct AsyncThrowingPublisher](asyncthrowingpublisher.md)
  A publisher that exposes its elements as a throwing asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncpublisher)*