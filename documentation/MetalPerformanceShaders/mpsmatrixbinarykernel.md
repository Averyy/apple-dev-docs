# MPSMatrixBinaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel that consumes two matrices and produces one matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixBinaryKernel
```

```objc
@interface MPSMatrixBinaryKernel : MPSKernel
```

## Topics

### Instance Properties
- [var batchSize: Int](./mpsmatrixbinarykernel/batchsize.md)
- [var batchStart: Int](./mpsmatrixbinarykernel/batchstart.md)
- [var primarySourceMatrixOrigin: MTLOrigin](./mpsmatrixbinarykernel/primarysourcematrixorigin.md)
- [var resultMatrixOrigin: MTLOrigin](./mpsmatrixbinarykernel/resultmatrixorigin.md)
- [var secondarySourceMatrixOrigin: MTLOrigin](./mpsmatrixbinarykernel/secondarysourcematrixorigin.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Inherited By
- [MPSMatrixBatchNormalizationGradient](./mpsmatrixbatchnormalizationgradient.md)
- [MPSMatrixFullyConnected](./mpsmatrixfullyconnected.md)
- [MPSMatrixFullyConnectedGradient](./mpsmatrixfullyconnectedgradient.md)
- [MPSMatrixNeuronGradient](./mpsmatrixneurongradient.md)
- [MPSMatrixSoftMaxGradient](./mpsmatrixsoftmaxgradient.md)
- [MPSMatrixSolveCholesky](./mpsmatrixsolvecholesky.md)
- [MPSMatrixSolveLU](./mpsmatrixsolvelu.md)
- [MPSMatrixSolveTriangular](./mpsmatrixsolvetriangular.md)
- [MPSMatrixVectorMultiplication](./mpsmatrixvectormultiplication.md)
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

### Classes for Decomposition and Solving
- [class MPSMatrixDecompositionCholesky](./mpsmatrixdecompositioncholesky.md)
  A kernel for computing the Cholesky factorization of a matrix.
- [class MPSMatrixSolveCholesky](./mpsmatrixsolvecholesky.md)
  A kernel for computing the solution of a linear system of equations using a Cholesky factorization.
- [class MPSMatrixDecompositionLU](./mpsmatrixdecompositionlu.md)
  A kernel for computing the LU factorization of a matrix using partial pivoting with row interchanges.
- [class MPSMatrixSolveLU](./mpsmatrixsolvelu.md)
  A kernel for computing the solution of a linear system of equations using an LU factorization.
- [class MPSMatrixSolveTriangular](./mpsmatrixsolvetriangular.md)
  A kernel for computing the solution of a linear system of equations using a triangular coefficient matrix.
- [class MPSMatrixUnaryKernel](./mpsmatrixunarykernel.md)
  A kernel that consumes one matrix and produces one matrix.
- [enum MPSMatrixDecompositionStatus](./mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbinarykernel)*