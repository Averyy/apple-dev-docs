# MPSMatrixUnaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel that consumes one matrix and produces one matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixUnaryKernel
```

```objc
@interface MPSMatrixUnaryKernel : MPSKernel
```

## Topics

### Instance Properties
- [var batchSize: Int](./mpsmatrixunarykernel/batchsize.md)
- [var batchStart: Int](./mpsmatrixunarykernel/batchstart.md)
- [var resultMatrixOrigin: MTLOrigin](./mpsmatrixunarykernel/resultmatrixorigin.md)
- [var sourceMatrixOrigin: MTLOrigin](./mpsmatrixunarykernel/sourcematrixorigin.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Inherited By
- [MPSMatrixBatchNormalization](./mpsmatrixbatchnormalization.md)
- [MPSMatrixDecompositionCholesky](./mpsmatrixdecompositioncholesky.md)
- [MPSMatrixDecompositionLU](./mpsmatrixdecompositionlu.md)
- [MPSMatrixFindTopK](./mpsmatrixfindtopk.md)
- [MPSMatrixNeuron](./mpsmatrixneuron.md)
- [MPSMatrixSoftMax](./mpsmatrixsoftmax.md)
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
- [class MPSMatrixBinaryKernel](./mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.
- [enum MPSMatrixDecompositionStatus](./mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixunarykernel)*