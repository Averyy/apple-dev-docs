# MPSMatrixSoftMaxGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A gradient softmax kernel that operates on matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixSoftMaxGradient
```

```objc
@interface MPSMatrixSoftMaxGradient : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixsoftmaxgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsmatrixsoftmaxgradient/init%28device%29.md)
### Instance Properties
- [var sourceColumns: Int](./mpsmatrixsoftmaxgradient/sourcecolumns.md)
- [var sourceRows: Int](./mpsmatrixsoftmaxgradient/sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixsoftmaxgradient/copy%28with,device%29.md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, forwardOutputMatrix: MPSMatrix, resultMatrix: MPSMatrix)](./mpsmatrixsoftmaxgradient/encode%28to,gradientmatrix,forwardoutputmatrix,resultmatrix%29.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](./mpsmatrixbinarykernel.md)
### Inherited By
- [MPSMatrixLogSoftMaxGradient](./mpsmatrixlogsoftmaxgradient.md)
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

## See Also

### Matrix Softmax Operations
- [class MPSMatrixLogSoftMax](./mpsmatrixlogsoftmax.md)
  A logarithmic softmax kernel that operates on matrices.
- [class MPSMatrixLogSoftMaxGradient](./mpsmatrixlogsoftmaxgradient.md)
  A logarithmic gradient softmax kernel that operates on matrices.
- [class MPSMatrixSoftMax](./mpsmatrixsoftmax.md)
  A softmax kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsoftmaxgradient)*