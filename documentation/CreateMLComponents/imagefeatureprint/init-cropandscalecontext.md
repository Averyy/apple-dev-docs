# init(cropAndScale:context:)

**Framework**: Create ML Components  
**Kind**: init

Creates a FeaturePrint feature extractor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(cropAndScale: VNImageCropAndScaleOption = .centerCrop, context: CIContext = CIContext())
```

## Parameters

- `cropAndScale`: The scaling and cropping options.
- `context`: The CoreImage context to use for the operation. Defaults to a new default context.

## See Also

- [init(from: any Decoder) throws](imagefeatureprint/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(revision: Int, cropAndScale: VNImageCropAndScaleOption, context: CIContext)](imagefeatureprint/init(revision:cropandscale:context:).md)
  Creates a FeaturePrint feature extractor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagefeatureprint/init(cropandscale:context:))*