# init(headroomStops:componentMix:controlPoints:)

**Framework**: ColorSync  
**Kind**: init

Creates an alternate gain curve.

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
init(headroomStops: Float = 0.0, componentMix: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix, controlPoints: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints) throws
```

#### Discussion

> **Note**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.negativeHeadroomStops(_:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/negativeheadroomstops(_:).md) if `headroomStops` is negative, or [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.zeroFreeStyleWeights`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/zerofreestyleweights.md) if a free-style `componentMix` has all-zero weights.

## Parameters

- `headroomStops`: The headroom this curve targets, in stops above reference white. Must be greater than or equal to `0`.
- `componentMix`: How the framework derives the driving signal from each pixel.
- `controlPoints`: The spline control points defining the curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/init(headroomstops:componentmix:controlpoints:))*