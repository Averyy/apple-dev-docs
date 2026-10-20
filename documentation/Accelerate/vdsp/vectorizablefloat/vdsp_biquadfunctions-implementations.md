# vDSP_BiquadFunctions Implementations

**Framework**: Accelerate  
**Role**: API Collection

## Topics

### Type Methods
- [static func applyMulti(setup: vDSP_biquadm_SetupD, pInputs: UnsafeMutablePointer<UnsafePointer<vDSP.VectorizableFloat.Scalar>>, pOutputs: UnsafeMutablePointer<UnsafeMutablePointer<vDSP.VectorizableFloat.Scalar>>, count: vDSP_Length)](./applymulti%28setup,pinputs,poutputs,count%29.md)
- [static func applySingle<U, V>(source: U, destination: inout V, delays: UnsafeMutablePointer<vDSP.VectorizableFloat.Scalar>, setup: vDSP_biquad_Setup, sectionCount: vDSP_Length, count: vDSP_Length)](./applysingle%28source,destination,delays,setup,sectioncount,count%29.md)
- [static func destroySetup(channelCount: UInt, biquadSetup: OpaquePointer)](./destroysetup%28channelcount,biquadsetup%29.md)
- [static func makeBiquadSetup(channelCount: UInt, coefficients: [Double], sectionCount: UInt) -> OpaquePointer?](./makebiquadsetup%28channelcount,coefficients,sectioncount%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/vectorizablefloat/vdsp_biquadfunctions-implementations)*