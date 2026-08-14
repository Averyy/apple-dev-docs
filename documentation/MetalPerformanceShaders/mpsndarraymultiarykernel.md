# MPSNDArrayMultiaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNDArrayMultiaryKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraymultiarykernel/init(coder:device:).md)
- [init(device: any MTLDevice, sourceCount: Int)](mpsndarraymultiarykernel/init(device:sourcecount:).md)
### Instance Methods
- [func encode(to: (any MTLComputeCommandEncoder)?, commandBuffer: any MTLCommandBuffer, sourceArrays: [MPSNDArray], destinationArray: MPSNDArray)](mpsndarraymultiarykernel/encode(to:commandbuffer:sourcearrays:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray]) -> MPSNDArray](mpsndarraymultiarykernel/encode(to:sourcearrays:).md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], destinationArray: MPSNDArray)](mpsndarraymultiarykernel/encode(to:sourcearrays:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], resultState: MPSState?, destinationArray: MPSNDArray)](mpsndarraymultiarykernel/encode(to:sourcearrays:resultstate:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](mpsndarraymultiarykernel/encode(to:sourcearrays:resultstate:outputstateistemporary:).md)
- [func encode(withMTL4CommandEncoder: any MTL4ComputeCommandEncoder, sourceArrays: [MPSNDArray], destinationArray: MPSNDArray)](mpsndarraymultiarykernel/encode(withmtl4commandencoder:sourcearrays:destinationarray:).md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryBase](mpsndarraymultiarybase.md)
### Inherited By
- [MPSNDArrayAffineInt4Dequantize](mpsndarrayaffineint4dequantize.md)
- [MPSNDArrayBinaryKernel](mpsndarraybinarykernel.md)
- [MPSNDArrayLUTDequantize](mpsndarraylutdequantize.md)
- [MPSNDArrayMatrixMultiplication](mpsndarraymatrixmultiplication.md)
- [MPSNDArrayUnaryKernel](mpsndarrayunarykernel.md)
- [MPSNDArrayVectorLUTDequantize](mpsndarrayvectorlutdequantize.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel)*