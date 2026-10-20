# MPSMatrixVectorMultiplication

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A matrix-vector multiplication kernel

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixVectorMultiplication
```

```objc
@interface MPSMatrixVectorMultiplication : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init(device: any MTLDevice, transpose: Bool, rows: Int, columns: Int, alpha: Double, beta: Double)](./mpsmatrixvectormultiplication/init%28device,transpose,rows,columns,alpha,beta%29.md)
- [init(device: any MTLDevice, rows: Int, columns: Int)](./mpsmatrixvectormultiplication/init%28device,rows,columns%29.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, inputVector: MPSVector, resultVector: MPSVector)](./mpsmatrixvectormultiplication/encode%28commandbuffer,inputmatrix,inputvector,resultvector%29.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](./mpsmatrixbinarykernel.md)
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

### Matrix Arithmetic Operations
- [class MPSMatrixSum](./mpsmatrixsum.md)
  A kernel for performing a pointwise summation of a matrix.
- [class MPSMatrixMultiplication](./mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixFindTopK](./mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixvectormultiplication)*