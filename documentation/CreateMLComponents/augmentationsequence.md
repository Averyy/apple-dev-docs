# AugmentationSequence

**Framework**: Create ML Components  
**Kind**: struct

An async sequence of augmented elements.

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
struct AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation> where Base : Sequence, RandomTransformer : RandomTransformer, RandomNumberGenerator : RandomNumberGenerator, Base.Element == AnnotatedFeature<RandomTransformer.Input, Annotation>, RandomTransformer.Input == RandomTransformer.Output
```

## Topics

### Getting the transformer
- [var transformer: RandomTransformer](augmentationsequence/transformer.md)
  The transformation applied to each element.
### Batching an augmentation sequence
- [func batches(ofSize: Int, dropsLastPartialBatch: Bool) -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.BatchedSequence](augmentationsequence/batches(ofsize:dropslastpartialbatch:).md)
  Batches a augmentation sequence.
- [AugmentationSequence.BatchedSequence](augmentationsequence/batchedsequence.md)
  An async sequence that batches an augmentation sequence.
### Creating an iterator
- [func makeAsyncIterator() -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.AsyncIterator](augmentationsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AugmentationSequence.Element](augmentationsequence/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](augmentationsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [struct ApplyEachRandomly](applyeachrandomly.md)
  Applies each transformer randomly given a probability.
- [struct ApplyRandomly](applyrandomly.md)
  Randomly applies the transformer with the given probability.
- [struct AugmentationBuilder](augmentationbuilder.md)
  A series of augmentations.
- [struct Augmenter](augmenter.md)
  An augmenter.
- [struct ChooseRandomly](chooserandomly.md)
  Apply single transformation randomly chosen from a list of transformers.
- [struct RandomImageCropper](randomimagecropper.md)
  Crops an image at a random location.
- [struct ShuffleRandomly](shufflerandomly.md)
  Apply transformations in a random order.
- [struct UniformRandomFloatingPointParameter](uniformrandomfloatingpointparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [class UniformRandomIntegerParameter](uniformrandomintegerparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [struct UpsampledAugmentationSequence](upsampledaugmentationsequence.md)
  An async sequence of augmented elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence)*