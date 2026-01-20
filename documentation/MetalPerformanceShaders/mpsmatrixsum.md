# MPSMatrixSum

**Framework**: Metal Performance Shaders  
**Kind**: class

A kernel for performing a pointwise summation of a matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixSum
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixsum/init(coder:device:).md)
- [init(device: any MTLDevice, count: Int, rows: Int, columns: Int, transpose: Bool)](mpsmatrixsum/init(device:count:rows:columns:transpose:).md)
### Instance Properties
- [var columns: Int](mpsmatrixsum/columns.md)
- [var count: Int](mpsmatrixsum/count.md)
- [var neuronParameterA: Float](mpsmatrixsum/neuronparametera.md)
- [var neuronParameterB: Float](mpsmatrixsum/neuronparameterb.md)
- [var neuronParameterC: Float](mpsmatrixsum/neuronparameterc.md)
- [var resultMatrixOrigin: MTLOrigin](mpsmatrixsum/resultmatrixorigin.md)
- [var rows: Int](mpsmatrixsum/rows.md)
- [var transpose: Bool](mpsmatrixsum/transpose.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], resultMatrix: MPSMatrix, scale: MPSVector?, offsetVector: MPSVector?, biasVector: MPSVector?, start: Int)](mpsmatrixsum/encode(to:sourcematrices:resultmatrix:scale:offsetvector:biasvector:start:).md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixsum/neurontype.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixsum/setneurontype(_:parametera:parameterb:parameterc:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
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

- [class MPSMatrixMultiplication](mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixVectorMultiplication](mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel
- [class MPSMatrixFindTopK](mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsum)*