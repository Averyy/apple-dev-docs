# MPSMatrixRandom

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
class MPSMatrixRandom
```

```objc
@interface MPSMatrixRandom : MPSKernel
```

## Topics

### Instance Properties
- [var batchSize: Int](./mpsmatrixrandom/batchsize.md)
- [var batchStart: Int](./mpsmatrixrandom/batchstart.md)
- [var destinationDataType: MPSDataType](./mpsmatrixrandom/destinationdatatype.md)
- [var distributionType: MPSMatrixRandomDistribution](./mpsmatrixrandom/distributiontype.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, destinationMatrix: MPSMatrix)](./mpsmatrixrandom/encode%28commandbuffer,destinationmatrix%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, destinationVector: MPSVector)](./mpsmatrixrandom/encode%28commandbuffer,destinationvector%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Inherited By
- [MPSMatrixRandomMTGP32](./mpsmatrixrandommtgp32.md)
- [MPSMatrixRandomPhilox](./mpsmatrixrandomphilox.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandom)*