# makeAsyncIterator()

**Framework**: Create ML Components  
**Kind**: method

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

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
func makeAsyncIterator() -> Downsampler<Input>.DownStreamSequence.Iterator
```

#### Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

- [Downsampler.DownStreamSequence.Iterator](downsampler/downstreamsequence/iterator.md)
  An async iterator of down stream sequence.
- [Downsampler.DownStreamSequence.AsyncIterator](downsampler/downstreamsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [Downsampler.DownStreamSequence.Feature](downsampler/downstreamsequence/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/downstreamsequence/makeasynciterator())*