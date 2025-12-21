# init(revision:cropAndScale:context:)

**Framework**: Create ML Components  
**Kind**: init

Creates a FeaturePrint feature extractor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(revision: Int, cropAndScale: VNImageCropAndScaleOption = .centerCrop, context: CIContext = CIContext())
```

## Parameters

- `revision`: The revision of feature extractor to use.
- `cropAndScale`: The scaling and cropping options.
- `context`: The CoreImage context to use for the operation. Defaults to a new default context.

## See Also

- [init(cropAndScale: VNImageCropAndScaleOption, context: CIContext)](imagefeatureprint/init(cropandscale:context:).md)
  Creates a FeaturePrint feature extractor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagefeatureprint/init(revision:cropandscale:context:))*