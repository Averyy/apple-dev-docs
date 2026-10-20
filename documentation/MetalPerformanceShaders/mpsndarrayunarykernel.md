# MPSNDArrayUnaryKernel

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
class MPSNDArrayUnaryKernel
```

```objc
@interface MPSNDArrayUnaryKernel : MPSNDArrayMultiaryKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](./mpsndarrayunarykernel/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsndarrayunarykernel/init%28device%29.md)
### Instance Properties
- [var dilationRates: MPSNDArraySizes](./mpsndarrayunarykernel/dilationrates.md)
- [var edgeMode: MPSImageEdgeMode](./mpsndarrayunarykernel/edgemode.md)
- [var kernelSizes: MPSNDArraySizes](./mpsndarrayunarykernel/kernelsizes.md)
- [var offsets: MPSNDArrayOffsets](./mpsndarrayunarykernel/offsets.md)
- [var strides: MPSNDArrayOffsets](./mpsndarrayunarykernel/strides.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray) -> MPSNDArray](./mpsndarrayunarykernel/encode%28to,sourcearray%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, destinationArray: MPSNDArray)](./mpsndarrayunarykernel/encode%28to,sourcearray,destinationarray%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState: MPSState?, destinationArray: MPSNDArray)](./mpsndarrayunarykernel/encode%28to,sourcearray,resultstate,destinationarray%29.md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](./mpsndarrayunarykernel/encode%28to,sourcearray,resultstate,outputstateistemporary%29.md)
- [func encode(withMTL4CommandEncoder: any MTL4ComputeCommandEncoder, sourceArray: MPSNDArray, destinationArray: MPSNDArray)](./mpsndarrayunarykernel/encode%28withmtl4commandencoder,sourcearray,destinationarray%29.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryKernel](./mpsndarraymultiarykernel.md)
### Inherited By
- [MPSNDArrayIdentity](./mpsndarrayidentity.md)
- [MPSNDArrayStridedSlice](./mpsndarraystridedslice.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel)*