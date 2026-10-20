# headroomAdaptiveGainCurveMetadata

**Framework**: ColorSync  
**Kind**: property  
**Role**: Instance Property

The raw Headroom Adaptive Gain Curve data embedded in this profile, or `nil` if it carries no HAGC tag.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var headroomAdaptiveGainCurveMetadata: Data? { get }
```

## Mentions

- [Authoring Headroom Adaptive Gain Curve metadata](../authoring-headroom-adaptive-gain-curve-metadata.md)

#### Discussion

This is equivalent to the serialized SMPTE ST 2094-50. Embed it in another profile with [`adding(headroomAdaptiveGainCurveMetadata:options:)`](./adding%28headroomadaptivegaincurvemetadata,options%29.md), or read the decoded form from [`headroomAdaptiveGainCurve`](./headroomadaptivegaincurve-swift.property.md).

## See Also

### Reading a curve in Swift
- [var headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve?](./headroomadaptivegaincurve-swift.property.md)
  The Headroom Adaptive Gain Curve embedded in this profile, or `nil` if it carries no HAGC tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurvemetadata)*