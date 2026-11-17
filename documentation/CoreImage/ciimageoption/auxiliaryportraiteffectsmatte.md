# auxiliaryPortraitEffectsMatte

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static let auxiliaryPortraitEffectsMatte: CIImageOption
```

```c
extern CIImageOption const kCIImageAuxiliaryPortraitEffectsMatte;
```

## Discussion

The value of this key is an [`NSNumber`](../../Foundation/nsnumber.md) containing a Boolean `true` or `false`.

## See Also

### Auxiliary Images
- [static let auxiliaryDepth: CIImageOption](./auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryDisparity: CIImageOption](./auxiliarydisparity.md)
  The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [static let auxiliaryHDRGainMap: CIImageOption](./auxiliaryhdrgainmap.md)
- [static let auxiliarySemanticSegmentationGlassesMatte: CIImageOption](./auxiliarysemanticsegmentationglassesmatte.md)
- [static let auxiliarySemanticSegmentationHairMatte: CIImageOption](./auxiliarysemanticsegmentationhairmatte.md)
- [static let auxiliarySemanticSegmentationSkinMatte: CIImageOption](./auxiliarysemanticsegmentationskinmatte.md)
- [static let auxiliarySemanticSegmentationSkyMatte: CIImageOption](./auxiliarysemanticsegmentationskymatte.md)
- [static let auxiliarySemanticSegmentationTeethMatte: CIImageOption](./auxiliarysemanticsegmentationteethmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/auxiliaryportraiteffectsmatte)*