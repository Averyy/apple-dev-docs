---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncTimerSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that produces elements at regular intervals.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
struct AsyncTimerSequence<C> where C : Clock
```

## Topics

### Structures
- [AsyncTimerSequence.Iterator](./asynctimersequence/iterator.md)
  The iterator for an `AsyncTimerSequence` instance.
### Initializers
- [init(interval: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C)](./asynctimersequence/init%28interval,tolerance,clock%29.md)
  Create an `AsyncTimerSequence` with a given repeating interval.
### Instance Methods
- [func makeAsyncIterator() -> AsyncTimerSequence<C>.Iterator](./asynctimersequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncTimerSequence.Element](./asynctimersequence/element.md)
### Type Methods
- [static func repeating(every: Duration, tolerance: Duration?) -> AsyncTimerSequence<SuspendingClock>](./asynctimersequence/repeating%28every,tolerance%29.md)
  Create an `AsyncTimerSequence` with a given repeating interval.
- [static func repeating(every: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) -> AsyncTimerSequence<C>](./asynctimersequence/repeating%28every,tolerance,clock%29.md)
  Create an `AsyncTimerSequence` with a given repeating interval.
### Default Implementations
- [AsyncSequence Implementations](./asynctimersequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asynctimersequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence)*