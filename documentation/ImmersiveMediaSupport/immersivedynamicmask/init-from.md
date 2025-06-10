# init(from:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [init(name: String, maskStereoRelation: ImmersiveDynamicMask.MaskStereoRelation, edgeTreatment: ImmersiveDynamicMask.MaskEdgeTreatment, controlPointInterpolation: ImmersiveDynamicMask.ControlPointInterpolation, leftControlPoints: [simd_float3], rightControlPoints: [simd_float3], edgeWidthInDegrees: Float)](immersivedynamicmask/init(name:maskstereorelation:edgetreatment:controlpointinterpolation:leftcontrolpoints:rightcontrolpoints:edgewidthindegrees:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivedynamicmask/init(from:))*