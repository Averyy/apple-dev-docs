# adding(headroomAdaptiveGainCurve:)

**Framework**: ColorSync  
**Kind**: method  
**Role**: Instance Method

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
func adding(headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve) -> ColorSyncProfile?
```

#### Return Value

A new profile carrying the HAGC tag, or `nil` if this profile’s transfer function isn’t PQ, HLG, or linear, or if embedding fails.

#### Discussion

The curve is validated when you construct [`ColorSyncProfile.HeadroomAdaptiveGainCurve`](./headroomadaptivegaincurve-swift.struct.md), so this method only embeds it. The original profile is unchanged.

## Parameters

- `headroomAdaptiveGainCurve`: The HAGC info dictionary to create the metadata embedded in the profile.

## See Also

### Attaching a curve in Swift
- [func adding(headroomAdaptiveGainCurveMetadata: Data, options: ColorSyncProfile.HeadroomAdaptiveGainCurveOptions) -> ColorSyncProfile?](./adding%28headroomadaptivegaincurvemetadata,options%29.md)
  Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.
- [ColorSyncProfile.HeadroomAdaptiveGainCurveOptions](./headroomadaptivegaincurveoptions.md)
  Options that configure how a Headroom Adaptive Gain Curve is read from or embedded in a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/adding(headroomadaptivegaincurve:))*