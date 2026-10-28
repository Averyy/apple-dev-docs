---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingchannel"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncThrowingChannel

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: class  
**Role**: Class

An error-throwing channel for sending elements from on task to another with back pressure.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
final class AsyncThrowingChannel<Element, Failure> where Element : Sendable, Failure : Error
```

## Overview

The `AsyncThrowingChannel` class is intended to be used as a communication types between tasks, particularly when one task produces values and another task consumes those values. The back pressure applied by `send(_:)` via suspension/resume ensures that the production of values does not exceed the consumption of values from iteration. This method suspends after enqueuing the event and is resumed when the next call to `next()` on the `Iterator` is made, or when `finish()`/`fail(_:)` is called from another Task. As `finish()` and `fail(_:)` induce a terminal state, there is no more need for a back pressure management. Those functions do not suspend and will finish all the pending iterations.

## Topics

### Structures
- [AsyncThrowingChannel.Iterator](./asyncthrowingchannel/iterator.md)
### Initializers
- [init()](./asyncthrowingchannel/init%28%29.md)
### Instance Methods
- [func fail(any Error)](./asyncthrowingchannel/fail%28_%29.md)
  Sends an error to all awaiting iterations. All subsequent calls to `next(_:)` will resume immediately.
- [func finish()](./asyncthrowingchannel/finish%28%29.md)
  Immediately resumes all the suspended operations. All subsequent calls to `next(_:)` will resume immediately.
- [func makeAsyncIterator() -> AsyncThrowingChannel<Element, Failure>.Iterator](./asyncthrowingchannel/makeasynciterator%28%29.md)
- [func send(Element) async](./asyncthrowingchannel/send%28_%29.md)
  Sends an element to an awaiting iteration. This function will resume when the next call to `next()` is made or when a call to `finish()` or `fail` is made from another task. If the channel is already finished then this returns immediately. If the task is cancelled, this function will resume without sending the element. Other sending operations from other tasks will remain active.
### Type Aliases
- [AsyncThrowingChannel.AsyncIterator](./asyncthrowingchannel/asynciterator.md)
- [AsyncThrowingChannel.Element](./asyncthrowingchannel/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncthrowingchannel/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncthrowingchannel/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingchannel)*