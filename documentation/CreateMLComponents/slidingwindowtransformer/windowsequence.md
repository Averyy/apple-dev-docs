# SlidingWindowTransformer.WindowSequence

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An async sequence of windows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct WindowSequence
```

Available when `Input` conforms to `Sendable`.

## Topics

### Getting the count
- [var count: Int?](./windowsequence/count.md)
  The number of elements in the sequence.
### Creating an iterator
- [SlidingWindowTransformer.WindowSequence.Iterator](./windowsequence/iterator.md)
  An async iterator of window sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [TemporalSequence](../temporalsequence.md)

## See Also

### Performing the transformation
- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> SlidingWindowTransformer<Input>.WindowSequence](./applied%28to,eventhandler%29.md)
  Extracts a window sequence from the input sequence


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer/windowsequence)*