# UniformRandomFloatingPointParameter

**Framework**: Create ML Components  
**Kind**: struct

Applies the transformer with a randomly generated input parameter.

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
struct UniformRandomFloatingPointParameter<RandomTransformer, Parameter> where RandomTransformer : RandomTransformer, Parameter : BinaryFloatingPoint, RandomTransformer.Input == RandomTransformer.Output, Parameter.RawSignificand : FixedWidthInteger
```

## Mentions

- [Augmenting images to expand your training data](augmenting-images-to-expand-your-training-data.md)

#### Overview

The parameter is chosen from a continuous uniform distribution in the specified range.

Note that a new transformer is created every time this transformer is applied. This may cause performance issues if the embedded transformer creation is costly.

## Topics

### Creating a transformer
- [init<Input>(range: ClosedRange<Parameter>, (Parameter) -> RandomTransformer)](uniformrandomfloatingpointparameter/init(range:_:).md)
  Creates a Random Parameter transformer.
### Getting the range
- [var range: ClosedRange<Parameter>](uniformrandomfloatingpointparameter/range.md)
  The range of a random number to use as input to the transformer.
### Applying
- [func applied(to: RandomTransformer.Input, generator: inout some RandomNumberGenerator, eventHandler: EventHandler?) async throws -> RandomTransformer.Output](uniformrandomfloatingpointparameter/applied(to:generator:eventhandler:).md)
  Performs the random apply operation on the input.

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
- [struct ShuffleRandomly](shufflerandomly.md)
  Apply transformations in a random order.
- [class UniformRandomIntegerParameter](uniformrandomintegerparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [struct UpsampledAugmentationSequence](upsampledaugmentationsequence.md)
  An async sequence of augmented elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/uniformrandomfloatingpointparameter)*