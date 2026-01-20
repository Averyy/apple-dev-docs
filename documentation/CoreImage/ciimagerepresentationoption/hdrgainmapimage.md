# hdrGainMapImage

**Framework**: Core Image  
**Kind**: property

An optional key and value to save a gain map channel to a JPEG or HEIF.

**Availability**:
- iOS 14.1+
- iPadOS 14.1+
- Mac Catalyst 14.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let hdrGainMapImage: CIImageRepresentationOption
```

#### Discussion

The value for this key needs to be a monochrome [`CIImage`](ciimage.md) instance.

If the [`hdrGainMapAsRGB`](ciimagerepresentationoption/hdrgainmapasrgb.md) option it true, then it needs to be an RGB [`CIImage`](ciimage.md) instance.

The `/CIImage/properties` should contain metadata information equivalent to what is returned when initializing an image using [`auxiliaryHDRGainMap`](ciimageoption/auxiliaryhdrgainmap.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimagerepresentationoption/hdrgainmapimage)*