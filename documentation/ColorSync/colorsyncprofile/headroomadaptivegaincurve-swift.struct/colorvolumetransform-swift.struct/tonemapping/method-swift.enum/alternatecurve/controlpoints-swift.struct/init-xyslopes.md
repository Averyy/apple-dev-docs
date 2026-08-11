# init(x:y:slopes:)

**Framework**: ColorSync  
**Kind**: init

Creates a set of spline control points.

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
init(x: [Float], y: [Float], slopes: ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes = .interpolate) throws
```

#### Discussion

> **Note**: [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.mismatchedControlPointArrays(x:y:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/mismatchedcontrolpointarrays(x:y:).md) if `x` and `y` differ in count, [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.tooManyControlPoints(count:limit:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/toomanycontrolpoints(count:limit:).md) if there are more than 32 points, or [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.mismatchedTangentCount(got:expected:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/mismatchedtangentcount(got:expected:).md) if explicit `slopes` don’t match the point count.

## Parameters

- `x`: Input levels normalized by reference white: 1.0 = reference white, and at most 32 points.
- `y`: Gain offsets in stops, one per `x` value. Must have the same count as `x` and non-negative.
- `slopes`: How the framework determines the slope at each control point. Defaults to [`ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes.interpolate`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/slopes-swift.enum/interpolate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/init(x:y:slopes:))*