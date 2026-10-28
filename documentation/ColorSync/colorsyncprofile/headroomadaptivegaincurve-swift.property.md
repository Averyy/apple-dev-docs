# headroomAdaptiveGainCurve

**Framework**: ColorSync  
**Kind**: property  
**Role**: Instance Property

The Headroom Adaptive Gain Curve embedded in this profile, or `nil` if it carries no HAGC tag.

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
var headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve? { get }
```

## Discussion

This decodes the HAGC tag into its structured form. For the unparsed bytes, use [`headroomAdaptiveGainCurveMetadata`](./headroomadaptivegaincurvemetadata.md).

## See Also

### Reading a curve in Swift
- [var headroomAdaptiveGainCurveMetadata: Data?](./headroomadaptivegaincurvemetadata.md)
  The raw Headroom Adaptive Gain Curve data embedded in this profile, or `nil` if it carries no HAGC tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.property)*