# HumanBodyActionCounter.CumulativeSumSequence

**Framework**: Create ML Components  
**Kind**: struct

Cumulative human body action count sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct CumulativeSumSequence
```

## Topics

### Getting the count
- [var count: Int?](humanbodyactioncounter/cumulativesumsequence/count.md)
  The estimated number of predictions.
### Creating an iterator
- [func makeAsyncIterator() -> HumanBodyActionCounter.CumulativeSumSequence.Iterator](humanbodyactioncounter/cumulativesumsequence/makeasynciterator.md)
  Constructs an iterator.
- [HumanBodyActionCounter.CumulativeSumSequence.Iterator](humanbodyactioncounter/cumulativesumsequence/iterator.md)
  An async iterator of cumulative count sequence.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> HumanBodyActionCounter.OutputSequence](humanbodyactioncounter/applied(to:eventhandler:).md)
  Predicts cumulative human body action counts from a sequence of human body pose windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter/cumulativesumsequence)*