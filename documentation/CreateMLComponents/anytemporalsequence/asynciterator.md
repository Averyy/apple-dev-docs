# AnyTemporalSequence.AsyncIterator

**Framework**: Create ML Components  
**Kind**: typealias

The type of asynchronous iterator that produces elements of this asynchronous sequence.

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
typealias AsyncIterator = AnyTemporalIterator<AnyTemporalSequence<Feature>.Element>
```

## See Also

- [func makeAsyncIterator() -> AnyTemporalIterator<AnyTemporalSequence<Feature>.Element>](anytemporalsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AnyTemporalSequence.Element](anytemporalsequence/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/anytemporalsequence/asynciterator)*