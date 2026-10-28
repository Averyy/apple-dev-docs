# AsyncStream.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

The asynchronous iterator for iterating an asynchronous stream.

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
struct Iterator
```

## Overview

This type doesn’t conform to `Sendable`. Don’t use it from multiple concurrent contexts. It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

## Topics

### Iterating over Elements
- [func next() async -> Element?](./iterator/next%28%29.md)
  The next value from the asynchronous stream.
### Instance Methods
- [func next(isolation: isolated (any Actor)?) async -> Element?](./iterator/next%28isolation%29.md)
  The next value from the asynchronous stream.
### Default Implementations
- [AsyncIteratorProtocol Implementations](./iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../asynciteratorprotocol.md)

## See Also

### Creating an Iterator
- [func makeAsyncIterator() -> AsyncStream<Element>.Iterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/iterator)*