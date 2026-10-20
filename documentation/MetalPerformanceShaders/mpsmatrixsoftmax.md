# MPSMatrixSoftMax

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSMatrixSoftMax : MPSMatrixUnaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixsoftmax/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsmatrixsoftmax/init%28device%29.md)
### Instance Properties
- [var sourceColumns: Int](./mpsmatrixsoftmax/sourcecolumns.md)
- [var sourceRows: Int](./mpsmatrixsoftmax/sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixsoftmax/copy%28with,device%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, resultMatrix: MPSMatrix)](./mpsmatrixsoftmax/encode%28commandbuffer,inputmatrix,resultmatrix%29.md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](./mpsmatrixunarykernel.md)
### Inherited By
- [MPSMatrixLogSoftMax](./mpsmatrixlogsoftmax.md)
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
- [class MPSMatrixSoftMaxGradient](./mpsmatrixsoftmaxgradient.md)
  A gradient softmax kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsoftmax)*