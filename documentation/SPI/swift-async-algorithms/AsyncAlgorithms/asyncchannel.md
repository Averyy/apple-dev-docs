---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchannel"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncChannel

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: class  
**Role**: Class

A channel for sending elements from one task to another with back pressure.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
final class AsyncChannel<Element> where Element : Sendable
```

#### Overview

The `AsyncChannel` class is intended to be used as a communication type between tasks, particularly when one task produces values and another task consumes those values. The back pressure applied by `send(_:)` via the suspension/resume ensures that the production of values does not exceed the consumption of values from iteration. This method suspends after enqueuing the event and is resumed when the next call to `next()` on the `Iterator` is made, or when `finish()` is called from another Task. As `finish()` induces a terminal state, there is no more need for a back pressure management. This function does not suspend and will finish all the pending iterations.

## Topics

### Structures
- [AsyncChannel.Iterator](./asyncchannel/iterator.md)
### Initializers
- [init()](./asyncchannel/init%28%29.md)
### Instance Methods
- [func finish()](./asyncchannel/finish%28%29.md)
  Immediately resumes all the suspended operations. All subsequent calls to `next(_:)` will resume immediately.
- [func makeAsyncIterator() -> AsyncChannel<Element>.Iterator](./asyncchannel/makeasynciterator%28%29.md)
- [func send(Element) async](./asyncchannel/send%28_%29.md)
  Sends an element to an awaiting iteration. This function will resume when the next call to `next()` is made or when a call to `finish()` is made from another task. If the channel is already finished then this returns immediately. If the task is cancelled, this function will resume without sending the element. Other sending operations from other tasks will remain active.
### Type Aliases
- [AsyncChannel.AsyncIterator](./asyncchannel/asynciterator.md)
- [AsyncChannel.Element](./asyncchannel/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncchannel/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncchannel/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchannel)*