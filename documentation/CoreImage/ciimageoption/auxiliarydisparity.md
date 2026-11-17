# auxiliaryDisparity

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

The key into the properties dictionary indicating whether to return an auxiliary disparity image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let auxiliaryDisparity: CIImageOption
```

```c
extern CIImageOption const kCIImageAuxiliaryDisparity;
```

## Discussion

The value of this key is an [`NSNumber`](../../Foundation/nsnumber.md) containing a Boolean `true` or `false`.  If the value is `true`, then calls to [`imageWithContentsOfURL:options:`](../ciimage/imagewithcontentsofurl_options_.md) and [`imageWithData:options:`](../ciimage/imagewithdata_options_.md) will return the auxiliary image as a half-float monochrome image instead of the primary image, or [`nil`](../../ObjectiveC/nil-227m0.md) if no auxiliary image exists.

## See Also

### Auxiliary Images
- [static let auxiliaryDepth: CIImageOption](./auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryHDRGainMap: CIImageOption](./auxiliaryhdrgainmap.md)
- [static let auxiliaryPortraitEffectsMatte: CIImageOption](./auxiliaryportraiteffectsmatte.md)
  The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
- [static let auxiliarySemanticSegmentationGlassesMatte: CIImageOption](./auxiliarysemanticsegmentationglassesmatte.md)
- [static let auxiliarySemanticSegmentationHairMatte: CIImageOption](./auxiliarysemanticsegmentationhairmatte.md)
- [static let auxiliarySemanticSegmentationSkinMatte: CIImageOption](./auxiliarysemanticsegmentationskinmatte.md)
- [static let auxiliarySemanticSegmentationSkyMatte: CIImageOption](./auxiliarysemanticsegmentationskymatte.md)
- [static let auxiliarySemanticSegmentationTeethMatte: CIImageOption](./auxiliarysemanticsegmentationteethmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/auxiliarydisparity)*