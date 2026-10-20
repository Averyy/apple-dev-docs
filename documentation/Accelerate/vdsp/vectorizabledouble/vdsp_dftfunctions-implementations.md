# vDSP_DFTFunctions Implementations

**Framework**: Accelerate  
**Role**: API Collection

## Topics

### Type Methods
- [static func destroySetup(OpaquePointer)](./destroysetup%28_%29.md)
- [static func makeDFTSetup<T>(previous: vDSP.DFT<T>?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType) -> OpaquePointer?](./makedftsetup%28previous,count,direction,transformtype%29.md)
- [static func transform<U, V>(dftSetup: OpaquePointer, inputReal: U, inputImaginary: U, outputReal: inout V, outputImaginary: inout V)](./transform%28dftsetup,inputreal,inputimaginary,outputreal,outputimaginary%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/vectorizabledouble/vdsp_dftfunctions-implementations)*