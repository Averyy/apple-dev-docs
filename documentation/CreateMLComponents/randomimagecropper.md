# RandomImageCropper

**Framework**: Create ML Components  
**Kind**: struct

Crops an image at a random location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct RandomImageCropper
```

## Topics

### Creating an image cropper
- [init(scale: ClosedRange<Double>, aspectRatio: Double?)](randomimagecropper/init(scale:aspectratio:).md)
  Creates an augmentation that crops an input image at a random location with a scale that indicates the lower and upper bounds to randomly scale the height and width of the image. The range must be between 0 and 1.
- [init(targetSize: CGSize)](randomimagecropper/init(targetsize:).md)
  Creates an augmentation that crops an input image at a random location to the specified target size.
- [init(targetWidth: Double, targetHeight: Double)](randomimagecropper/init(targetwidth:targetheight:).md)
  Creates an augmentation that crops an input image at a random location to the specified target width and height.
### Performing the augmentation
- [func applied(to: CIImage, generator: inout some RandomNumberGenerator, eventHandler: EventHandler?) async throws -> CIImage](randomimagecropper/applied(to:generator:eventhandler:).md)
  Randomly crops an image at a random location of a given size.

## Relationships

### Conforms To
- [RandomTransformer](randomtransformer.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct ShuffleRandomly](shufflerandomly.md)
  Apply transformations in a random order.
- [struct UniformRandomFloatingPointParameter](uniformrandomfloatingpointparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [class UniformRandomIntegerParameter](uniformrandomintegerparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [struct UpsampledAugmentationSequence](upsampledaugmentationsequence.md)
  An async sequence of augmented elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/randomimagecropper)*