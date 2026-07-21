# headroomAdaptiveGainCurveMetadata

**Framework**: ColorSync  
**Kind**: property

The raw Headroom Adaptive Gain Curve data embedded in this profile, or `nil` if it carries no HAGC tag.

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
var headroomAdaptiveGainCurveMetadata: Data? { get }
```

## Mentions

- [Authoring Headroom Adaptive Gain Curve metadata](authoring-headroom-adaptive-gain-curve-metadata.md)

#### Discussion

This is equivalent to the serialized SMPTE ST 2094-50. Embed it in another profile with [`adding(headroomAdaptiveGainCurveMetadata:options:)`](colorsyncprofile/adding(headroomadaptivegaincurvemetadata:options:).md), or read the decoded form from [`headroomAdaptiveGainCurve`](colorsyncprofile/headroomadaptivegaincurve-swift.property.md).

## See Also

- [var headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve?](colorsyncprofile/headroomadaptivegaincurve-swift.property.md)
  The Headroom Adaptive Gain Curve embedded in this profile, or `nil` if it carries no HAGC tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurvemetadata)*