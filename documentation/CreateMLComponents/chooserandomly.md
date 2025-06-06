# ChooseRandomly

**Framework**: Create ML Components  
**Kind**: struct

Apply single transformation randomly chosen from a list of transformers.

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
struct ChooseRandomly<Element>
```

## Topics

### Creating an augmentation
- [init<RandomTransformer>(() -> RandomTransformer)](chooserandomly/init(_:).md)
  Creates a choose randomly augmentation.
### Applying transformers
- [func applied(to: Element, generator: inout some RandomNumberGenerator, eventHandler: EventHandler?) async throws -> Element](chooserandomly/applied(to:generator:eventhandler:).md)
  Chooses a random transformer from a list of transformers and applies the chosen transformer.
### Type Aliases
- [ChooseRandomly.Input](chooserandomly/input.md)
  The input type.
- [ChooseRandomly.Output](chooserandomly/output.md)
  The output type.

## Relationships

### Conforms To
- [RandomTransformer](randomtransformer.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/chooserandomly)*