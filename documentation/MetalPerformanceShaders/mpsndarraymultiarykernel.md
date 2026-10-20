# MPSNDArrayMultiaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSNDArrayMultiaryKernel : MPSNDArrayMultiaryBase
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](./mpsndarraymultiarykernel/init%28coder,device%29.md)
- [init(device: any MTLDevice, sourceCount: Int)](./mpsndarraymultiarykernel/init%28device,sourcecount%29.md)
### Instance Methods
- [func encode(to: (any MTLComputeCommandEncoder)?, commandBuffer: any MTLCommandBuffer, sourceArrays: [MPSNDArray], destinationArray: MPSNDArray)](./mpsndarraymultiarykernel/encode%28to,commandbuffer,sourcearrays,destinationarray%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray]) -> MPSNDArray](./mpsndarraymultiarykernel/encode%28to,sourcearrays%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], destinationArray: MPSNDArray)](./mpsndarraymultiarykernel/encode%28to,sourcearrays,destinationarray%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], resultState: MPSState?, destinationArray: MPSNDArray)](./mpsndarraymultiarykernel/encode%28to,sourcearrays,resultstate,destinationarray%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](./mpsndarraymultiarykernel/encode%28to,sourcearrays,resultstate,outputstateistemporary%29.md)
- [func encode(withMTL4CommandEncoder: any MTL4ComputeCommandEncoder, sourceArrays: [MPSNDArray], destinationArray: MPSNDArray)](./mpsndarraymultiarykernel/encode%28withmtl4commandencoder,sourcearrays,destinationarray%29.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryBase](./mpsndarraymultiarybase.md)
### Inherited By
- [MPSNDArrayAffineInt4Dequantize](./mpsndarrayaffineint4dequantize.md)
- [MPSNDArrayBinaryKernel](./mpsndarraybinarykernel.md)
- [MPSNDArrayLUTDequantize](./mpsndarraylutdequantize.md)
- [MPSNDArrayMatrixMultiplication](./mpsndarraymatrixmultiplication.md)
- [MPSNDArrayUnaryKernel](./mpsndarrayunarykernel.md)
- [MPSNDArrayVectorLUTDequantize](./mpsndarrayvectorlutdequantize.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel)*