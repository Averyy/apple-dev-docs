# HumanBodyActionCounter.CumulativeSumSequence

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [var count: Int?](./cumulativesumsequence/count.md)
  The estimated number of predictions.
### Creating an iterator
- [func makeAsyncIterator() -> HumanBodyActionCounter.CumulativeSumSequence.Iterator](./cumulativesumsequence/makeasynciterator%28%29.md)
  Constructs an iterator.
- [HumanBodyActionCounter.CumulativeSumSequence.Iterator](./cumulativesumsequence/iterator.md)
  An async iterator of cumulative count sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [TemporalSequence](../temporalsequence.md)

## See Also

### Performing the transformation
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> HumanBodyActionCounter.OutputSequence](./applied%28to,eventhandler%29.md)
  Predicts cumulative human body action counts from a sequence of human body pose windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter/cumulativesumsequence)*