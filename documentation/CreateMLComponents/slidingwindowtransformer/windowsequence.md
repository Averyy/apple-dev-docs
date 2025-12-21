# SlidingWindowTransformer.WindowSequence

**Framework**: Create ML Components  
**Kind**: struct

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

## Topics

### Getting the count
- [var count: Int?](slidingwindowtransformer/windowsequence/count.md)
  The number of elements in the sequence.
### Creating an iterator
- [SlidingWindowTransformer.WindowSequence.Iterator](slidingwindowtransformer/windowsequence/iterator.md)
  An async iterator of window sequence.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> SlidingWindowTransformer<Input>.WindowSequence](slidingwindowtransformer/applied(to:eventhandler:).md)
  Extracts a window sequence from the input sequence


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer/windowsequence)*