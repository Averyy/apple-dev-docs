---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbufferedbyteiterator"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncBufferedByteIterator

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncIterator` that provides a convenient and high-performance implementation of a common architecture for `AsyncSequence` of `UInt8`, otherwise known as byte streams.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncBufferedByteIterator
```

## Overview

Bytes are read into an internal buffer of `capacity` bytes via the `readFunction`. Invoking `next()` returns bytes from the internal buffer until it’s empty, and then suspends and awaits another invocation of `readFunction` to refill. If `readFunction` returns 0 (indicating nothing was read), `next()` will return `nil` from then on. Cancellation is checked before each invocation of `readFunction`, which means that many calls to `next()` will not check for cancellation.

A typical use of `AsyncBufferedByteIterator` looks something like this:

```
struct AsyncBytes: AsyncSequence {
  public typealias Element = UInt8
  var handle: ReadableThing

  internal init(_ readable: ReadableThing) {
    handle = readable
  }

  public func makeAsyncIterator() -> AsyncBufferedByteIterator {
    return AsyncBufferedByteIterator(capacity: 16384) { buffer in
      // This runs once every 16384 invocations of next()
      return try await handle.read(into: buffer)
    }
  }
}
```

## Topics

### Initializers
- [init(capacity: Int, readFunction: (UnsafeMutableRawBufferPointer) async throws -> Int)](./asyncbufferedbyteiterator/init%28capacity,readfunction%29.md)
  Creates an asynchronous buffered byte iterator with a specified capacity and read function.
### Instance Methods
- [func next() async throws -> UInt8?](./asyncbufferedbyteiterator/next%28%29.md)
  Reads a byte out of the buffer if available. When no bytes are available, this will trigger the read function to reload the buffer and then return the next byte from that buffer.
### Type Aliases
- [AsyncBufferedByteIterator.Element](./asyncbufferedbyteiterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](./asyncbufferedbyteiterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- _Concurrency.AsyncIteratorProtocol


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbufferedbyteiterator)*