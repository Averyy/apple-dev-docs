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
func makeAsyncIterator() -> SlidingWindowTransformer<Input>.WindowSequence.Iterator
```

#### Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

- [SlidingWindowTransformer.WindowSequence.Iterator](slidingwindowtransformer/windowsequence/iterator.md)
  An async iterator of window sequence.
- [SlidingWindowTransformer.WindowSequence.AsyncIterator](slidingwindowtransformer/windowsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [SlidingWindowTransformer.WindowSequence.Feature](slidingwindowtransformer/windowsequence/feature.md)
  The feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer/windowsequence/makeasynciterator())*