# MPSMatrixSum

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSMatrixSum : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixsum/init%28coder,device%29.md)
- [init(device: any MTLDevice, count: Int, rows: Int, columns: Int, transpose: Bool)](./mpsmatrixsum/init%28device,count,rows,columns,transpose%29.md)
### Instance Properties
- [var columns: Int](./mpsmatrixsum/columns.md)
- [var count: Int](./mpsmatrixsum/count.md)
- [var neuronParameterA: Float](./mpsmatrixsum/neuronparametera.md)
- [var neuronParameterB: Float](./mpsmatrixsum/neuronparameterb.md)
- [var neuronParameterC: Float](./mpsmatrixsum/neuronparameterc.md)
- [var resultMatrixOrigin: MTLOrigin](./mpsmatrixsum/resultmatrixorigin.md)
- [var rows: Int](./mpsmatrixsum/rows.md)
- [var transpose: Bool](./mpsmatrixsum/transpose.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], resultMatrix: MPSMatrix, scale: MPSVector?, offsetVector: MPSVector?, biasVector: MPSVector?, start: Int)](./mpsmatrixsum/encode%28to,sourcematrices,resultmatrix,scale,offsetvector,biasvector,start%29.md)
- [func neuronType() -> MPSCNNNeuronType](./mpsmatrixsum/neurontype%28%29.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](./mpsmatrixsum/setneurontype%28_,parametera,parameterb,parameterc%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
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
- [class MPSMatrixMultiplication](./mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixVectorMultiplication](./mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel
- [class MPSMatrixFindTopK](./mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsum)*