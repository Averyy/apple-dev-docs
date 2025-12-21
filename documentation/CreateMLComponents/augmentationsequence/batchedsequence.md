# AugmentationSequence.BatchedSequence

**Framework**: Create ML Components  
**Kind**: struct

An async sequence that batches an augmentation sequence.

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
struct BatchedSequence
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.BatchedSequence.AsyncIterator](augmentationsequence/batchedsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces batches.
- [AugmentationSequence.Element](augmentationsequence/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](augmentationsequence/batchedsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func batches(ofSize: Int, dropsLastPartialBatch: Bool) -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.BatchedSequence](augmentationsequence/batches(ofsize:dropslastpartialbatch:).md)
  Batches a augmentation sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence/batchedsequence)*