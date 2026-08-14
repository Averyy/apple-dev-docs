# ColorSyncProfile

**Framework**: ColorSync  
**Kind**: class

A reference to an immutable International Color Consortium (ICC) color profile.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class ColorSyncProfile
```

## Mentions

- [Authoring Headroom Adaptive Gain Curve metadata](authoring-headroom-adaptive-gain-curve-metadata.md)

## Topics

### Structures
- [ColorSyncProfile.HeadroomAdaptiveGainCurve](colorsyncprofile/headroomadaptivegaincurve-swift.struct.md)
  Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.
- [ColorSyncProfile.HeadroomAdaptiveGainCurveOptions](colorsyncprofile/headroomadaptivegaincurveoptions.md)
  Options that configure how a Headroom Adaptive Gain Curve is read from or embedded in a profile.
### Instance Properties
- [var headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve?](colorsyncprofile/headroomadaptivegaincurve-swift.property.md)
  The Headroom Adaptive Gain Curve embedded in this profile, or `nil` if it carries no HAGC tag.
- [var headroomAdaptiveGainCurveMetadata: Data?](colorsyncprofile/headroomadaptivegaincurvemetadata.md)
  The raw Headroom Adaptive Gain Curve data embedded in this profile, or `nil` if it carries no HAGC tag.
### Instance Methods
- [func adding(headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve) -> ColorSyncProfile?](colorsyncprofile/adding(headroomadaptivegaincurve:).md)
  Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.
- [func adding(headroomAdaptiveGainCurveMetadata: Data, options: ColorSyncProfile.HeadroomAdaptiveGainCurveOptions) -> ColorSyncProfile?](colorsyncprofile/adding(headroomadaptivegaincurvemetadata:options:).md)
  Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.

## Relationships

### Inherited By
- [ColorSyncMutableProfile](colorsyncmutableprofile.md)
### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [class ColorSyncMutableProfile](colorsyncmutableprofile.md)
  A reference to a mutable ICC color profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile)*