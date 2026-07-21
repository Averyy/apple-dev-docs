# init(headroomStops:componentMix:controlPoints:)

**Framework**: ColorSync  
**Kind**: init

Creates an alternate gain curve.

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
init(headroomStops: Float = 0.0, componentMix: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ComponentMix, controlPoints: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints) throws
```

#### Discussion

> **Note**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.negativeHeadroomStops(_:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/negativeheadroomstops(_:).md) if `headroomStops` is negative, or [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.zeroFreeStyleWeights`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/zerofreestyleweights.md) if a free-style `componentMix` has all-zero weights.

## Parameters

- `headroomStops`: The headroom this curve targets, in stops above reference white. Must be greater than or equal to `0`.
- `componentMix`: How the driving signal is derived from each pixel.
- `controlPoints`: The spline control points defining the curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/init(headroomstops:componentmix:controlpoints:))*