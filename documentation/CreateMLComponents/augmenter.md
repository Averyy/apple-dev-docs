# Augmenter

**Framework**: Create ML Components  
**Kind**: struct

An augmenter.

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
struct Augmenter<RandomTransformer, RandomNumberGenerator> where RandomTransformer : RandomTransformer, RandomNumberGenerator : RandomNumberGenerator, RandomTransformer.Input == RandomTransformer.Output
```

## Mentions

- [Augmenting images to expand your training data](augmenting-images-to-expand-your-training-data.md)

## Topics

### Creating an augmenter
- [init<Input>(generator: RandomNumberGenerator, () -> RandomTransformer)](augmenter/init(generator:_:).md)
  Creates an augmenter from a random number generator and an augmentation builder.
### Applying an augmentation
- [func applied<S, Annotation>(to: S) -> AugmentationSequence<S, RandomTransformer, RandomNumberGenerator, Annotation>](augmenter/applied(to:).md)
  Applies an augmentation per input of the base sequence.
- [func applied<C, Annotation>(to: C, upsampledBy: Int) -> UpsampledAugmentationSequence<C, RandomTransformer, RandomNumberGenerator, Annotation>](augmenter/applied(to:upsampledby:).md)
  Applies an augmentation repeatedly to an array of inputs.

## See Also

- [struct ApplyEachRandomly](applyeachrandomly.md)
  Applies each transformer randomly given a probability.
- [struct ApplyRandomly](applyrandomly.md)
  Randomly applies the transformer with the given probability.
- [struct AugmentationBuilder](augmentationbuilder.md)
  A series of augmentations.
- [struct AugmentationSequence](augmentationsequence.md)
  An async sequence of augmented elements.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmenter)*