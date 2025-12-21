# Option set support

**Framework**: Create ML

Inspect and modify a video augmentation option set with the properties and methods it inherits from standard protocols.

#### Overview

You don’t typically use these properties and methods directly.

[`MLHandActionClassifier.VideoAugmentationOptions`](mlhandactionclassifier/videoaugmentationoptions.md) inherits these symbols from [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) and [`Codable`](https://developer.apple.com/documentation/Swift/Codable). Create a set of video augmentations by creating an array literal with any combination of these type properties:

- `horizontalFlip`
- `randomMove`
- `randomScale`
- `randomShift`
- `frameDrop`
- `timeInterpolate`

## Topics

### Creating an augmentation
- [init(rawValue: Int)](mlhandactionclassifier/videoaugmentationoptions/init(rawvalue:).md)
  Creates an option set from an integer.

## See Also

- [static let dropFrames: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/dropframes.md)
  Randomly drop frames from a video.
- [static let horizontallyFlip: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/horizontallyflip.md)
  Apply left-right flips to the pose in a video.
- [static let interpolateFrames: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/interpolateframes.md)
  Random time interpolation through a video.
- [static let rotate: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/rotate.md)
  Randomly rotate the pose in a video.
- [static let scale: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/scale.md)
  Randomly scale the pose in a video.
- [static let translate: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/translate.md)
  Randomly translate the pose in a video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/option-set-support)*