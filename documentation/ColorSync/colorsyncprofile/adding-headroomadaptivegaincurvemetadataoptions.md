# adding(headroomAdaptiveGainCurveMetadata:options:)

**Framework**: ColorSync  
**Kind**: method

Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.

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
func adding(headroomAdaptiveGainCurveMetadata: Data, options: ColorSyncProfile.HeadroomAdaptiveGainCurveOptions = .init()) -> ColorSyncProfile?
```

## Mentions

- [Authoring Headroom Adaptive Gain Curve metadata](authoring-headroom-adaptive-gain-curve-metadata.md)

#### Return Value

A new profile carrying the HAGC tag, or `nil` if this profile’s transfer function isn’t PQ, HLG, or linear, or if embedding fails.

#### Discussion

Use this to move an HAGC between profiles without interpreting it — for example, to carry the HAGC payload read from one profile into another, or one shared with a video stream (SMPTE ST 2094-50 payload). The original profile is unchanged.

## Parameters

- `headroomAdaptiveGainCurveMetadata`: The raw HAGC payload to embed.
- `options`: Options that configure embedding. Reserved for future use.

## See Also

- [func adding(headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve) -> ColorSyncProfile?](colorsyncprofile/adding(headroomadaptivegaincurve:).md)
  Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.
- [ColorSyncProfile.HeadroomAdaptiveGainCurveOptions](colorsyncprofile/headroomadaptivegaincurveoptions.md)
  Options that configure how a Headroom Adaptive Gain Curve is read from or embedded in a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/adding(headroomadaptivegaincurvemetadata:options:))*