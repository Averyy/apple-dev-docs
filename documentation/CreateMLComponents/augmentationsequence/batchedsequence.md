# AugmentationSequence.BatchedSequence

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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

Available when `Base` conforms to `Sequence`, `RandomTransformer` conforms to `RandomTransformer`, `RandomNumberGenerator` conforms to `RandomNumberGenerator`, `Base.Element` is `AnnotatedFeature<RandomTransformer.Input, Annotation>`, and `RandomTransformer.Input` is `RandomTransformer.Output`.

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.BatchedSequence.AsyncIterator](./batchedsequence/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces batches.
- [AugmentationSequence.Element](./element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](./batchedsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Batching an augmentation sequence
- [func batches(ofSize: Int, dropsLastPartialBatch: Bool) -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.BatchedSequence](./batches%28ofsize,dropslastpartialbatch%29.md)
  Batches a augmentation sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence/batchedsequence)*