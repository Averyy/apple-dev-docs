# makeAsyncIterator()

**Framework**: Create ML Components  
**Kind**: method

Creates the asynchronous iterator that produces batches.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func makeAsyncIterator() -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.BatchedSequence.AsyncIterator
```

## See Also

- [AugmentationSequence.BatchedSequence.Element](augmentationsequence/batchedsequence/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence/batchedsequence/makeasynciterator())*