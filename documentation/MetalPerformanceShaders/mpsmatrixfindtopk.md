# MPSMatrixFindTopK

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixfindtopk/init(coder:device:).md)
- [init(device: any MTLDevice, numberOfTopKValues: Int)](mpsmatrixfindtopk/init(device:numberoftopkvalues:).md)
### Instance Properties
- [var indexOffset: Int](mpsmatrixfindtopk/indexoffset.md)
- [var numberOfTopKValues: Int](mpsmatrixfindtopk/numberoftopkvalues.md)
- [var sourceColumns: Int](mpsmatrixfindtopk/sourcecolumns.md)
- [var sourceRows: Int](mpsmatrixfindtopk/sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixfindtopk/copy(with:device:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, resultIndexMatrix: MPSMatrix, resultValueMatrix: MPSMatrix)](mpsmatrixfindtopk/encode(commandbuffer:inputmatrix:resultindexmatrix:resultvaluematrix:).md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSMatrixSum](mpsmatrixsum.md)
  A kernel for performing a pointwise summation of a matrix.
- [class MPSMatrixMultiplication](mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixVectorMultiplication](mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfindtopk)*