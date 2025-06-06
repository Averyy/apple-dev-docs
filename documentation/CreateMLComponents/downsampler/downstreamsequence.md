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
- [func makeAsyncIterator() -> Downsampler<Input>.DownStreamSequence.Iterator](downsampler/downstreamsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [Downsampler.DownStreamSequence.Iterator](downsampler/downstreamsequence/iterator.md)
  An async iterator of down stream sequence.
- [Downsampler.DownStreamSequence.AsyncIterator](downsampler/downstreamsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [Downsampler.DownStreamSequence.Feature](downsampler/downstreamsequence/feature.md)
  The feature type.
### Type Aliases
- [Downsampler.DownStreamSequence.Element](downsampler/downstreamsequence/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](downsampler/downstreamsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> Downsampler<Input>.DownStreamSequence](downsampler/applied(to:eventhandler:).md)
  Down samples the input sequence
- [Downsampler.Input](downsampler/input.md)
  The input type.
- [Downsampler.Output](downsampler/output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/downstreamsequence)*