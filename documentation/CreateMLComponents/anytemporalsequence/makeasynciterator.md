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
func makeAsyncIterator() -> AnyTemporalIterator<AnyTemporalSequence<Feature>.Element>
```

#### Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

- [AnyTemporalSequence.AsyncIterator](anytemporalsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [AnyTemporalSequence.Element](anytemporalsequence/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/anytemporalsequence/makeasynciterator())*