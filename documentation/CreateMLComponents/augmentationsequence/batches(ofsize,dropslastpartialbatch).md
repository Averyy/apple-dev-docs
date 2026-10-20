# batches(ofSize:dropsLastPartialBatch:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Batches a augmentation sequence.

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
func batches(ofSize size: Int, dropsLastPartialBatch: Bool) -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.BatchedSequence
```

Available when `Base` conforms to `Sequence`, `RandomTransformer` conforms to `RandomTransformer`, `RandomNumberGenerator` conforms to `RandomNumberGenerator`, `Base.Element` is `AnnotatedFeature<RandomTransformer.Input, Annotation>`, and `RandomTransformer.Input` is `RandomTransformer.Output`.

#### Return Value

An async sequence of batches.

## Parameters

- `size`: The number of elements contained in each batch.
- `dropsLastPartialBatch`: A Boolean value representing whether the last batch should be dropped if it has less than `size` elements.

## See Also

### Batching an augmentation sequence
- [AugmentationSequence.BatchedSequence](./batchedsequence.md)
  An async sequence that batches an augmentation sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence/batches(ofsize:dropslastpartialbatch:))*