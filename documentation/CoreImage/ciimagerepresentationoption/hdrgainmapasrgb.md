# hdrGainMapAsRGB

**Framework**: Core Image  
**Kind**: property

An optional key and value to request the gain map channel to be color instead of monochrome.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static let hdrGainMapAsRGB: CIImageRepresentationOption
```

#### Discussion

This key affects how the gain map image is calculated from the SDR receiver and the [`hdrImage`](ciimagerepresentationoption/hdrimage.md) image value.

The value for this is a Boolean where:

- True: the gain map is created as a color ratio between the HDR and SDR images.
- False: the gain map is created as a brightness ratio between the HDR and SDR images.
- Not specified: the default behavior False.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimagerepresentationoption/hdrgainmapasrgb)*