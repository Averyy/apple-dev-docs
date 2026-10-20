# MPSMatrixSolveTriangular

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel for computing the solution of a linear system of equations using a triangular coefficient matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixSolveTriangular
```

```objc
@interface MPSMatrixSolveTriangular : MPSMatrixBinaryKernel
```

#### Overview

This kernel finds the solution matrix to the system *op(A) * X = alpha * B* or *X * op(A) = alpha * B*, where:

- A is either an upper or lower triangular matrix
- *op(A)* is either *Aᵀ* or *A*
- *X* is the resulting matrix of solutions
- *B* is the array of right hand sides for which the equations are to be solved

## Topics

### Initializers
- [init(device: any MTLDevice, right: Bool, upper: Bool, transpose: Bool, unit: Bool, order: Int, numberOfRightHandSides: Int, alpha: Double)](./mpsmatrixsolvetriangular/init%28device,right,upper,transpose,unit,order,numberofrighthandsides,alpha%29.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, rightHandSideMatrix: MPSMatrix, solutionMatrix: MPSMatrix)](./mpsmatrixsolvetriangular/encode%28commandbuffer,sourcematrix,righthandsidematrix,solutionmatrix%29.md)

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

### Classes for Decomposition and Solving
- [class MPSMatrixDecompositionCholesky](./mpsmatrixdecompositioncholesky.md)
  A kernel for computing the Cholesky factorization of a matrix.
- [class MPSMatrixSolveCholesky](./mpsmatrixsolvecholesky.md)
  A kernel for computing the solution of a linear system of equations using a Cholesky factorization.
- [class MPSMatrixDecompositionLU](./mpsmatrixdecompositionlu.md)
  A kernel for computing the LU factorization of a matrix using partial pivoting with row interchanges.
- [class MPSMatrixSolveLU](./mpsmatrixsolvelu.md)
  A kernel for computing the solution of a linear system of equations using an LU factorization.
- [class MPSMatrixUnaryKernel](./mpsmatrixunarykernel.md)
  A kernel that consumes one matrix and produces one matrix.
- [class MPSMatrixBinaryKernel](./mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.
- [enum MPSMatrixDecompositionStatus](./mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsolvetriangular)*