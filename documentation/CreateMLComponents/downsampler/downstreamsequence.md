# Downsampler.DownStreamSequence

**Framework**: Create ML Components  
**Kind**: struct

An async sequence of down stream elements.

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
struct DownStreamSequence
```

## Topics

### Getting the count
- [var count: Int?](downsampler/downstreamsequence/count.md)
  The count of elements.
### Creating an iterator
- [Downsampler.DownStreamSequence.Iterator](downsampler/downstreamsequence/iterator.md)
  An async iterator of down stream sequence.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> Downsampler<Input>.DownStreamSequence](downsampler/applied(to:eventhandler:).md)
  Down samples the input sequence


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/downstreamsequence)*