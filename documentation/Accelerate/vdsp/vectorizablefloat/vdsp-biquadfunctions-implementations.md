# vDSP_BiquadFunctions Implementations

**Framework**: Accelerate

## Topics

### Type Methods
- [static func applyMulti(setup: vDSP_biquadm_SetupD, pInputs: UnsafeMutablePointer<UnsafePointer<vDSP.VectorizableFloat.Scalar>>, pOutputs: UnsafeMutablePointer<UnsafeMutablePointer<vDSP.VectorizableFloat.Scalar>>, count: vDSP_Length)](vdsp/vectorizablefloat/applymulti(setup:pinputs:poutputs:count:).md)
- [static func applySingle<U, V>(source: U, destination: inout V, delays: UnsafeMutablePointer<vDSP.VectorizableFloat.Scalar>, setup: vDSP_biquad_Setup, sectionCount: vDSP_Length, count: vDSP_Length)](vdsp/vectorizablefloat/applysingle(source:destination:delays:setup:sectioncount:count:).md)
- [static func destroySetup(channelCount: UInt, biquadSetup: OpaquePointer)](vdsp/vectorizablefloat/destroysetup(channelcount:biquadsetup:).md)
- [static func makeBiquadSetup(channelCount: UInt, coefficients: [Double], sectionCount: UInt) -> OpaquePointer?](vdsp/vectorizablefloat/makebiquadsetup(channelcount:coefficients:sectioncount:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/vectorizablefloat/vdsp_biquadfunctions-implementations)*