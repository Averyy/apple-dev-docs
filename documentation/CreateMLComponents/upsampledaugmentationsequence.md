# UpsampledAugmentationSequence

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
struct UpsampledAugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation> where Base : Collection, RandomTransformer : RandomTransformer, RandomNumberGenerator : RandomNumberGenerator, Base.Element == AnnotatedFeature<RandomTransformer.Input, Annotation>, RandomTransformer.Input == RandomTransformer.Output
```

## Topics

### Getting the transformer
- [let transformer: RandomTransformer](upsampledaugmentationsequence/transformer.md)
  The transformation applied to each element.
### Creating an iterator
- [func makeAsyncIterator() -> UpsampledAugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.AsyncIterator](upsampledaugmentationsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [UpsampledAugmentationSequence.Element](upsampledaugmentationsequence/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](upsampledaugmentationsequence/asyncsequence-implementations.md)

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
- [struct AugmentationSequence](augmentationsequence.md)
  An async sequence of augmented elements.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/upsampledaugmentationsequence)*