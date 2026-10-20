# MPSMatrixFindTopK

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel for computing the top-K values and their corresponding indices in a matrix.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixFindTopK
```

```objc
@interface MPSMatrixFindTopK : MPSMatrixUnaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixfindtopk/init%28coder,device%29.md)
- [init(device: any MTLDevice, numberOfTopKValues: Int)](./mpsmatrixfindtopk/init%28device,numberoftopkvalues%29.md)
### Instance Properties
- [var indexOffset: Int](./mpsmatrixfindtopk/indexoffset.md)
- [var numberOfTopKValues: Int](./mpsmatrixfindtopk/numberoftopkvalues.md)
- [var sourceColumns: Int](./mpsmatrixfindtopk/sourcecolumns.md)
- [var sourceRows: Int](./mpsmatrixfindtopk/sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsmatrixfindtopk/copy%28with,device%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, resultIndexMatrix: MPSMatrix, resultValueMatrix: MPSMatrix)](./mpsmatrixfindtopk/encode%28commandbuffer,inputmatrix,resultindexmatrix,resultvaluematrix%29.md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](./mpsmatrixunarykernel.md)
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
- [class MPSMatrixVectorMultiplication](./mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfindtopk)*