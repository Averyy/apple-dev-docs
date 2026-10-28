# MPSMatrixDecompositionLU

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel for computing the LU factorization of a matrix using partial pivoting with row interchanges.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixDecompositionLU
```

```objc
@interface MPSMatrixDecompositionLU : MPSMatrixUnaryKernel
```

## Overview

This kernel object computes an LU factorization, *PA = LU*, where:

- *A* is a matrix for which the LU factorization is to be computed
- *L* is a unit lower triangular matrix
- *U* is an upper triangular matrix
- *P* is a permutation matrix

## Topics

### Initializers
- [init(device: any MTLDevice, rows: Int, columns: Int)](./mpsmatrixdecompositionlu/init%28device,rows,columns%29.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, resultMatrix: MPSMatrix, pivotIndices: MPSMatrix, info: (any MTLBuffer)?)](./mpsmatrixdecompositionlu/encode%28commandbuffer,sourcematrix,resultmatrix,pivotindices,info%29.md)

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

### Classes for Decomposition and Solving
- [class MPSMatrixDecompositionCholesky](./mpsmatrixdecompositioncholesky.md)
  A kernel for computing the Cholesky factorization of a matrix.
- [class MPSMatrixSolveCholesky](./mpsmatrixsolvecholesky.md)
  A kernel for computing the solution of a linear system of equations using a Cholesky factorization.
- [class MPSMatrixSolveLU](./mpsmatrixsolvelu.md)
  A kernel for computing the solution of a linear system of equations using an LU factorization.
- [class MPSMatrixSolveTriangular](./mpsmatrixsolvetriangular.md)
  A kernel for computing the solution of a linear system of equations using a triangular coefficient matrix.
- [class MPSMatrixUnaryKernel](./mpsmatrixunarykernel.md)
  A kernel that consumes one matrix and produces one matrix.
- [class MPSMatrixBinaryKernel](./mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.
- [enum MPSMatrixDecompositionStatus](./mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdecompositionlu)*