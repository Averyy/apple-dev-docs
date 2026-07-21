# headroomAdaptiveGainCurve

**Framework**: ColorSync  
**Kind**: property

The Headroom Adaptive Gain Curve embedded in this profile, or `nil` if it carries no HAGC tag.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve? { get }
```

#### Discussion

This decodes the HAGC tag into its structured form. For the unparsed bytes, use [`headroomAdaptiveGainCurveMetadata`](colorsyncprofile/headroomadaptivegaincurvemetadata.md).

## See Also

- [var headroomAdaptiveGainCurveMetadata: Data?](colorsyncprofile/headroomadaptivegaincurvemetadata.md)
  The raw Headroom Adaptive Gain Curve data embedded in this profile, or `nil` if it carries no HAGC tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.property)*