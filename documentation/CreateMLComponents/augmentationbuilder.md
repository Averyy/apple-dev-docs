# AugmentationBuilder

**Framework**: Create ML Components  
**Kind**: struct

A series of augmentations.

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
@resultBuilder
struct AugmentationBuilder<Element>
```

## Topics

### Building augmentations
- [static func buildPartialBlock(accumulated: some RandomTransformer<Element, Element>, next: some RandomTransformer<Element, Element>) -> some RandomTransformer<Element, Element>
](augmentationbuilder/buildpartialblock(accumulated:next:)-3h3fp.md)
  Builds a partial result by combining an accumulated random transformer and a new random transformer.
- [static func buildPartialBlock(accumulated: some RandomTransformer<Element, Element>, next: some Transformer<Element, Element>) -> some RandomTransformer<Element, Element>
](augmentationbuilder/buildpartialblock(accumulated:next:)-4a0qn.md)
  Builds a partial result by combining an accumulated random transformer and a new transformer.
- [static func buildPartialBlock(first: some RandomTransformer<Element, Element>) -> some RandomTransformer<Element, Element>
](augmentationbuilder/buildpartialblock(first:)-5lyed.md)
  Builds a partial result random transformer from the first random transformer.
- [static func buildPartialBlock(first: some Transformer<Element, Element>) -> some RandomTransformer<Element, Element>
](augmentationbuilder/buildpartialblock(first:)-8uoqq.md)
  Builds a partial result from the first transformer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ApplyEachRandomly](applyeachrandomly.md)
  Applies each transformer randomly given a probability.
- [struct ApplyRandomly](applyrandomly.md)
  Randomly applies the transformer with the given probability.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationbuilder)*