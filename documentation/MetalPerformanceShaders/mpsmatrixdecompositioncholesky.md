# MPSMatrixDecompositionCholesky

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel for computing the Cholesky factorization of a matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixDecompositionCholesky
```

```objc
@interface MPSMatrixDecompositionCholesky : MPSMatrixUnaryKernel
```

## Overview

This kernel computes one of the following factorizations of a matrix *A*:

- *A = LLᵀ*
- *A = UᵀU*

where:

- *A* is a symmetric positive-definite matrix for which the factorization is to be computed
- *L* is the lower triangular matrix
- *U* is the upper triangular matrix

## Topics

### Initializers
- [init(device: any MTLDevice, lower: Bool, order: Int)](./mpsmatrixdecompositioncholesky/init%28device,lower,order%29.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, resultMatrix: MPSMatrix, status: (any MTLBuffer)?)](./mpsmatrixdecompositioncholesky/encode%28commandbuffer,sourcematrix,resultmatrix,status%29.md)

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
- [class MPSMatrixBinaryKernel](./mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.
- [enum MPSMatrixDecompositionStatus](./mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdecompositioncholesky)*