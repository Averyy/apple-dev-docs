# AsyncThrowingPublisher

**Framework**: Combine  
**Kind**: struct

A publisher that exposes its elements as a throwing asynchronous sequence.

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
struct AsyncThrowingPublisher<P> where P : Publisher
```

#### Overview

`AsyncThrowingPublisher` conforms to [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), which allows callers to receive values with the `for`-`await`-`in` syntax, rather than attaching a [`Subscriber`](subscriber.md). If the upstream publisher terminates with an error, `AsyncThrowingPublisher` throws the error to the awaiting caller.

Use the [`values`](publisher/values-v7nz.md) property of the [`Publisher`](publisher.md) protocol to wrap an existing publisher with an instance of this type.

## Topics

### Creating an Asynchronous Publisher
- [init(_:)](asyncthrowingpublisher/init(_:).md)
  Creates a publisher that exposes elements received from an upstream publisher as a throwing asynchronous sequence.
### Creating an Iterator
- [func makeAsyncIterator() -> AsyncThrowingPublisher<P>.Iterator](asyncthrowingpublisher/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncThrowingPublisher.Iterator](asyncthrowingpublisher/iterator.md)
  The iterator that produces elements of the asynchronous publisher sequence.
### Supporting Types
- [AsyncThrowingPublisher.Element](asyncthrowingpublisher/element.md)
  The type of element produced by this asynchronous sequence.
### Type Aliases
- [AsyncThrowingPublisher.AsyncIterator](asyncthrowingpublisher/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](asyncthrowingpublisher/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [struct AsyncPublisher](asyncpublisher.md)
  A publisher that exposes its elements as an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncthrowingpublisher)*