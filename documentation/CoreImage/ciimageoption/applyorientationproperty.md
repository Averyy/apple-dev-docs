# applyOrientationProperty

**Framework**: Core Image  
**Kind**: property

The key for transforming an image according to orientation metadata.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let applyOrientationProperty: CIImageOption
```

#### Discussion

Images can contain metadata that reveals the orientation at capture time.  You can load this metadata into [`CIImage`](ciimage.md) with [`imageWithContentsOfURL:`](ciimage/imagewithcontentsofurl:.md) or [`init(data:)`](ciimage/init(data:).md) when the captured image contains orientation metadata.  Use any of the `initWith:options:` methods if the [`properties`](ciimageoption/properties.md) ([`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) of metadata properties) option is also provided.

If the value of this key is true, then calls to [`imageWithContentsOfURL:options:`](ciimage/imagewithcontentsofurl:options:.md) and [`imageWithData:options:`](ciimage/imagewithdata:options:.md) will return the image transformed according to its orientation metadata.

## See Also

- [static let auxiliaryDepth: CIImageOption](ciimageoption/auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryDisparity: CIImageOption](ciimageoption/auxiliarydisparity.md)
  The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [static let auxiliaryHDRGainMap: CIImageOption](ciimageoption/auxiliaryhdrgainmap.md)
- [static let auxiliaryPortraitEffectsMatte: CIImageOption](ciimageoption/auxiliaryportraiteffectsmatte.md)
  The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
- [static let auxiliarySemanticSegmentationGlassesMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationglassesmatte.md)
- [static let auxiliarySemanticSegmentationHairMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationhairmatte.md)
- [static let auxiliarySemanticSegmentationSkinMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationskinmatte.md)
- [static let auxiliarySemanticSegmentationSkyMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationskymatte.md)
- [static let auxiliarySemanticSegmentationTeethMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationteethmatte.md)
- [static let cacheImmediately: CIImageOption](ciimageoption/cacheimmediately.md)
- [static let colorSpace: CIImageOption](ciimageoption/colorspace.md)
  The key for a color space.
- [static let expandToHDR: CIImageOption](ciimageoption/expandtohdr.md)
  A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [static let nearestSampling: CIImageOption](ciimageoption/nearestsampling.md)
  The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [static let properties: CIImageOption](ciimageoption/properties.md)
  The key for image metadata properties.
- [static let providerTileSize: CIImageOption](ciimageoption/providertilesize.md)
  A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/applyorientationproperty)*