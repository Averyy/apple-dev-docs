# avDepthData

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

The depth data representation of an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let avDepthData: CIImageRepresentationOption
```

```c
extern CIImageRepresentationOption const kCIImageRepresentationAVDepthData;
```

#### Discussion

`options` dictionary key for image export methods to represent data as [`AVDepthData`](../../AVFoundation/avdepthdata.md).

## See Also

### Type Properties
- [static let avPortraitEffectsMatte: CIImageRepresentationOption](./avportraiteffectsmatte.md)
- [static let avSemanticSegmentationMattes: CIImageRepresentationOption](./avsemanticsegmentationmattes.md)
- [static let depthImage: CIImageRepresentationOption](./depthimage.md)
  `options` dictionary key for image export methods to output depth data.
- [static let disparityImage: CIImageRepresentationOption](./disparityimage.md)
  `options` dictionary key for image export methods to output disparity data.
- [static let portraitEffectsMatteImage: CIImageRepresentationOption](./portraiteffectsmatteimage.md)
- [static let semanticSegmentationGlassesMatteImage: CIImageRepresentationOption](./semanticsegmentationglassesmatteimage.md)
- [static let semanticSegmentationHairMatteImage: CIImageRepresentationOption](./semanticsegmentationhairmatteimage.md)
- [static let semanticSegmentationSkinMatteImage: CIImageRepresentationOption](./semanticsegmentationskinmatteimage.md)
- [static let semanticSegmentationSkyMatteImage: CIImageRepresentationOption](./semanticsegmentationskymatteimage.md)
- [static let semanticSegmentationTeethMatteImage: CIImageRepresentationOption](./semanticsegmentationteethmatteimage.md)
- [static let hdrImage: CIImageRepresentationOption](./hdrimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimagerepresentationoption/avdepthdata)*