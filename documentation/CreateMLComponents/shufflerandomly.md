# ShuffleRandomly

**Framework**: Create ML Components  
**Kind**: struct

Apply transformations in a random order.

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
struct ShuffleRandomly<Element>
```

## Topics

### Creating a transformer
- [init<RandomTransformer>(() -> RandomTransformer)](shufflerandomly/init(_:).md)
  Creates a random shuffle augmentation.
### Performing the transformation
- [func applied(to: Element, generator: inout some RandomNumberGenerator, eventHandler: EventHandler?) async throws -> Element](shufflerandomly/applied(to:generator:eventhandler:).md)
  Apply transformations in a random order.
### Type Aliases
- [ShuffleRandomly.Input](shufflerandomly/input.md)
  The input type.
- [ShuffleRandomly.Output](shufflerandomly/output.md)
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
- [struct ChooseRandomly](chooserandomly.md)
  Apply single transformation randomly chosen from a list of transformers.
- [struct RandomImageCropper](randomimagecropper.md)
  Crops an image at a random location.
- [struct UniformRandomFloatingPointParameter](uniformrandomfloatingpointparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [class UniformRandomIntegerParameter](uniformrandomintegerparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [struct UpsampledAugmentationSequence](upsampledaugmentationsequence.md)
  An async sequence of augmented elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/shufflerandomly)*