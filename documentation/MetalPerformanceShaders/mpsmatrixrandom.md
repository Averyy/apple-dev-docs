# MPSMatrixRandom

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
class MPSMatrixRandom
```

## Topics

### Instance Properties
- [var batchSize: Int](mpsmatrixrandom/batchsize.md)
- [var batchStart: Int](mpsmatrixrandom/batchstart.md)
- [var destinationDataType: MPSDataType](mpsmatrixrandom/destinationdatatype.md)
- [var distributionType: MPSMatrixRandomDistribution](mpsmatrixrandom/distributiontype.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, destinationMatrix: MPSMatrix)](mpsmatrixrandom/encode(commandbuffer:destinationmatrix:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, destinationVector: MPSVector)](mpsmatrixrandom/encode(commandbuffer:destinationvector:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSMatrixRandomMTGP32](mpsmatrixrandommtgp32.md)
- [MPSMatrixRandomPhilox](mpsmatrixrandomphilox.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandom)*