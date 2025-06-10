# ApplyRandomly

**Framework**: Create ML Components  
**Kind**: struct

Randomly applies the transformer with the given probability.

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
struct ApplyRandomly<RandomTransformer> where RandomTransformer : RandomTransformer, RandomTransformer.Input == RandomTransformer.Output
```

## Topics

### Creating an augmentation
- [init<Input>(probability: Double, () -> RandomTransformer)](applyrandomly/init(probability:_:).md)
  Creates an apply randomly augmentation.
### Getting the probability
- [let probability: Double](applyrandomly/probability.md)
  The probability of applying the transformer. Default value is 0.5.
### Applying transformers
- [func applied(to: RandomTransformer.Input, generator: inout some RandomNumberGenerator, eventHandler: EventHandler?) async throws -> RandomTransformer.Output](applyrandomly/applied(to:generator:eventhandler:).md)
  Randomly applies a transformer on an input.
### Type Aliases
- [ApplyRandomly.Input](applyrandomly/input.md)
  The input type.
- [ApplyRandomly.Output](applyrandomly/output.md)
  The output type.

## Relationships

### Conforms To
- [RandomTransformer](randomtransformer.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ApplyEachRandomly](applyeachrandomly.md)
  Applies each transformer randomly given a probability.
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
- [struct UpsampledAugmentationSequence](upsampledaugmentationsequence.md)
  An async sequence of augmented elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/applyrandomly)*