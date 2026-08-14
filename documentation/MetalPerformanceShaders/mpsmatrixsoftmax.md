# MPSMatrixSoftMax

**Framework**: Metal Performance Shaders  
**Kind**: class

A softmax kernel that operates on matrices.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixSoftMax
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixsoftmax/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsmatrixsoftmax/init(device:).md)
### Instance Properties
- [var sourceColumns: Int](mpsmatrixsoftmax/sourcecolumns.md)
- [var sourceRows: Int](mpsmatrixsoftmax/sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixsoftmax/copy(with:device:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, resultMatrix: MPSMatrix)](mpsmatrixsoftmax/encode(commandbuffer:inputmatrix:resultmatrix:).md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
### Inherited By
- [MPSMatrixLogSoftMax](mpsmatrixlogsoftmax.md)
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

## See Also

- [class MPSMatrixLogSoftMax](mpsmatrixlogsoftmax.md)
  A logarithmic softmax kernel that operates on matrices.
- [class MPSMatrixLogSoftMaxGradient](mpsmatrixlogsoftmaxgradient.md)
  A logarithmic gradient softmax kernel that operates on matrices.
- [class MPSMatrixSoftMaxGradient](mpsmatrixsoftmaxgradient.md)
  A gradient softmax kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsoftmax)*