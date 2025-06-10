# vDSP_BiquadFunctions Implementations

**Framework**: Accelerate

## Topics

### Type Methods
- [static func applyMulti(setup: vDSP_biquadm_SetupD, pInputs: UnsafeMutablePointer<UnsafePointer<vDSP.VectorizableDouble.Scalar>>, pOutputs: UnsafeMutablePointer<UnsafeMutablePointer<vDSP.VectorizableDouble.Scalar>>, count: vDSP_Length)](vdsp/vectorizabledouble/applymulti(setup:pinputs:poutputs:count:).md)
- [static func applySingle<U, V>(source: U, destination: inout V, delays: UnsafeMutablePointer<vDSP.VectorizableDouble.Scalar>, setup: vDSP_biquad_Setup, sectionCount: vDSP_Length, count: vDSP_Length)](vdsp/vectorizabledouble/applysingle(source:destination:delays:setup:sectioncount:count:).md)
- [static func destroySetup(channelCount: UInt, biquadSetup: OpaquePointer)](vdsp/vectorizabledouble/destroysetup(channelcount:biquadsetup:).md)
- [static func makeBiquadSetup(channelCount: vDSP_Length, coefficients: [Double], sectionCount: vDSP_Length) -> OpaquePointer?](vdsp/vectorizabledouble/makebiquadsetup(channelcount:coefficients:sectioncount:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/vectorizabledouble/vdsp_biquadfunctions-implementations)*