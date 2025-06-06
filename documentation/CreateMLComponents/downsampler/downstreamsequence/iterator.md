# Downsampler.DownStreamSequence.Iterator

**Framework**: Create ML Components  
**Kind**: struct

An async iterator of down stream sequence.

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
struct Iterator
```

## Topics

### Getting the next element
- [func next() async throws -> TemporalFeature<Downsampler<Input>.Output>?](downsampler/downstreamsequence/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [Downsampler.DownStreamSequence.Iterator.Element](downsampler/downstreamsequence/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](downsampler/downstreamsequence/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> Downsampler<Input>.DownStreamSequence.Iterator](downsampler/downstreamsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [Downsampler.DownStreamSequence.AsyncIterator](downsampler/downstreamsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [Downsampler.DownStreamSequence.Feature](downsampler/downstreamsequence/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/downstreamsequence/iterator)*