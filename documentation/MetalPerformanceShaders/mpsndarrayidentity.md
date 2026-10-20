# MPSNDArrayIdentity

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MPSNDArrayIdentity
```

```objc
@interface MPSNDArrayIdentity : MPSNDArrayUnaryKernel
```

## Topics

### Initializers
- [init(device: any MTLDevice)](./mpsndarrayidentity/init%28device%29.md)
### Instance Methods
- [func reshape(with: (any MTLComputeCommandEncoder)?, commandBuffer: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray?) -> MPSNDArray?](./mpsndarrayidentity/reshape%28with,commandbuffer,sourcearray,dimensioncount,dimensionsizes,destinationarray%29.md)
- [func reshape(with: (any MTLComputeCommandEncoder)?, commandBuffer: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, shape: [NSNumber], destinationArray: MPSNDArray?) -> MPSNDArray?](./mpsndarrayidentity/reshape%28with,commandbuffer,sourcearray,shape,destinationarray%29.md)
- [func reshape(with: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray?) -> MPSNDArray?](./mpsndarrayidentity/reshape%28with,sourcearray,dimensioncount,dimensionsizes,destinationarray%29.md)
- [func reshape(with: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, shape: [NSNumber], destinationArray: MPSNDArray?) -> MPSNDArray?](./mpsndarrayidentity/reshape%28with,sourcearray,shape,destinationarray%29.md)
- [func reshape(withMTL4CommandEncoder: any MTL4ComputeCommandEncoder, sourceArray: MPSNDArray, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray)](./mpsndarrayidentity/reshape%28withmtl4commandencoder,sourcearray,dimensioncount,dimensionsizes,destinationarray%29.md)
- [func reshape(withMTL4CommandEncoder: any MTL4ComputeCommandEncoder, sourceArray: MPSNDArray, shape: [NSNumber], destinationArray: MPSNDArray)](./mpsndarrayidentity/reshape%28withmtl4commandencoder,sourcearray,shape,destinationarray%29.md)
- [func reshape(withSourceArray: MPSNDArray, shape: [NSNumber]) -> MPSNDArray?](./mpsndarrayidentity/reshape%28withsourcearray,shape%29.md)

## Relationships

### Inherits From
- [MPSNDArrayUnaryKernel](./mpsndarrayunarykernel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity)*