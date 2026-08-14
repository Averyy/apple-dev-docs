# MPSNDArrayUnaryKernel

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
class MPSNDArrayUnaryKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarrayunarykernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsndarrayunarykernel/init(device:).md)
### Instance Properties
- [var dilationRates: MPSNDArraySizes](mpsndarrayunarykernel/dilationrates.md)
- [var edgeMode: MPSImageEdgeMode](mpsndarrayunarykernel/edgemode.md)
- [var kernelSizes: MPSNDArraySizes](mpsndarrayunarykernel/kernelsizes.md)
- [var offsets: MPSNDArrayOffsets](mpsndarrayunarykernel/offsets.md)
- [var strides: MPSNDArrayOffsets](mpsndarrayunarykernel/strides.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray) -> MPSNDArray](mpsndarrayunarykernel/encode(to:sourcearray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, destinationArray: MPSNDArray)](mpsndarrayunarykernel/encode(to:sourcearray:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState: MPSState?, destinationArray: MPSNDArray)](mpsndarrayunarykernel/encode(to:sourcearray:resultstate:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](mpsndarrayunarykernel/encode(to:sourcearray:resultstate:outputstateistemporary:).md)
- [func encode(withMTL4CommandEncoder: any MTL4ComputeCommandEncoder, sourceArray: MPSNDArray, destinationArray: MPSNDArray)](mpsndarrayunarykernel/encode(withmtl4commandencoder:sourcearray:destinationarray:).md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryKernel](mpsndarraymultiarykernel.md)
### Inherited By
- [MPSNDArrayIdentity](mpsndarrayidentity.md)
- [MPSNDArrayStridedSlice](mpsndarraystridedslice.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel)*