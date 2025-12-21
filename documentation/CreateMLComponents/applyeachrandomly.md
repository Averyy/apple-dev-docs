# ApplyEachRandomly

**Framework**: Create ML Components  
**Kind**: struct

Applies each transformer randomly given a probability.

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
struct ApplyEachRandomly<Element>
```

## Topics

### Creating an augmentation
- [init<RandomTransformer>(probability: Double, () -> RandomTransformer)](applyeachrandomly/init(probability:_:).md)
  Creates an augmentation that applies each transformer randomly in the given order.
### Getting the probability
- [let probability: Double](applyeachrandomly/probability.md)
  The probability of applying each transformer. Default value is 0.5.
### Applying transformers
- [func applied(to: Element, generator: inout some RandomNumberGenerator, eventHandler: EventHandler?) async throws -> Element](applyeachrandomly/applied(to:generator:eventhandler:).md)
  Applies each transformer randomly in order with a probability.

## Relationships

### Conforms To
- [RandomTransformer](randomtransformer.md)

## See Also

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
- [struct UpsampledAugmentationSequence](upsampledaugmentationsequence.md)
  An async sequence of augmented elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/applyeachrandomly)*