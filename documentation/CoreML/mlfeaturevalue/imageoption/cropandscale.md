# cropAndScale

**Framework**: Core ML  
**Kind**: property

The option you use to crop and scale an image when creating an image feature value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let cropAndScale: MLFeatureValue.ImageOption
```

#### Discussion

Use this value as a dictionary key for the `options` argument of an image-based `MLFeatureValue` initializer. Pair this key with a [`VNImageCropAndScaleOption`](https://developer.apple.com/documentation/Vision/VNImageCropAndScaleOption) value in the initializer’s `options` dictionary. For example, see [`init(CGImage:pixelsWide:pixelsHigh:pixelFormatType:options:)`](mlfeaturevalue/init(cgimage:pixelswide:pixelshigh:pixelformattype:options:).md).

## See Also

- [static let cropRect: MLFeatureValue.ImageOption](mlfeaturevalue/imageoption/croprect.md)
  The option you use to crop an image when creating an image feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/imageoption/cropandscale)*