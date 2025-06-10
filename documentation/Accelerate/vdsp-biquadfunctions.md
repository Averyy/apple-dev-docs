# vDSP_BiquadFunctions

**Framework**: Accelerate  
**Kind**: protocol

A protocol that defines functions for biquadratic filtering.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
protocol vDSP_BiquadFunctions
```

## Topics

### Associated Types
- [associatedtype Scalar](vdsp_biquadfunctions/scalar.md)
### Type Methods
- [static func applyMulti(setup: vDSP_biquadm_SetupD, pInputs: UnsafeMutablePointer<UnsafePointer<Self.Scalar>>, pOutputs: UnsafeMutablePointer<UnsafeMutablePointer<Self.Scalar>>, count: vDSP_Length)](vdsp_biquadfunctions/applymulti(setup:pinputs:poutputs:count:).md)
- [static func applySingle<U, V>(source: U, destination: inout V, delays: UnsafeMutablePointer<Self.Scalar>, setup: vDSP_biquad_Setup, sectionCount: vDSP_Length, count: vDSP_Length)](vdsp_biquadfunctions/applysingle(source:destination:delays:setup:sectioncount:count:).md)
- [static func destroySetup(channelCount: UInt, biquadSetup: OpaquePointer)](vdsp_biquadfunctions/destroysetup(channelcount:biquadsetup:).md)
- [static func makeBiquadSetup(channelCount: vDSP_Length, coefficients: [Double], sectionCount: vDSP_Length) -> OpaquePointer?](vdsp_biquadfunctions/makebiquadsetup(channelcount:coefficients:sectioncount:).md)

## Relationships

### Conforming Types
- [vDSP.VectorizableDouble](vdsp/vectorizabledouble.md)
- [vDSP.VectorizableFloat](vdsp/vectorizablefloat.md)

## See Also

- [protocol vDSP_FloatingPointBiquadFilterable](vdsp_floatingpointbiquadfilterable.md)
  Types that support biquadratic filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadfunctions)*