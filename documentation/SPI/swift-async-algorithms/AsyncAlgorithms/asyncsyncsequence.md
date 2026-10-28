---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncsyncsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncSyncSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence composed from a synchronous sequence.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncSyncSequence<Base> where Base : Sequence
```

## Overview

Asynchronous lazy sequences can be used to interface existing or pre-calculated data to interoperate with other asynchronous sequences and algorithms based on asynchronous sequences.

This functions similarly to `LazySequence` by accessing elements sequentially in the iterator’s `next()` method.

## Topics

### Structures
- [AsyncSyncSequence.Iterator](./asyncsyncsequence/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AsyncSyncSequence<Base>.Iterator](./asyncsyncsequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncSyncSequence.Element](./asyncsyncsequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncsyncsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncsyncsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncsyncsequence)*