# MPSMatrixSolveTriangular

**Framework**: Metal Performance Shaders  
**Kind**: class

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

#### Overview

This kernel finds the solution matrix to the system *op(A) * X = alpha * B* or *X * op(A) = alpha * B*, where:

- A is either an upper or lower triangular matrix
- *op(A)* is either *Aᵀ* or *A*
- *X* is the resulting matrix of solutions
- *B* is the array of right hand sides for which the equations are to be solved

## Topics

### Initializers
- [init(device: any MTLDevice, right: Bool, upper: Bool, transpose: Bool, unit: Bool, order: Int, numberOfRightHandSides: Int, alpha: Double)](mpsmatrixsolvetriangular/init(device:right:upper:transpose:unit:order:numberofrighthandsides:alpha:).md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, rightHandSideMatrix: MPSMatrix, solutionMatrix: MPSMatrix)](mpsmatrixsolvetriangular/encode(commandbuffer:sourcematrix:righthandsidematrix:solutionmatrix:).md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MPSMatrixDecompositionCholesky](mpsmatrixdecompositioncholesky.md)
  A kernel for computing the Cholesky factorization of a matrix.
- [class MPSMatrixSolveCholesky](mpsmatrixsolvecholesky.md)
  A kernel for computing the solution of a linear system of equations using a Cholesky factorization.
- [class MPSMatrixDecompositionLU](mpsmatrixdecompositionlu.md)
  A kernel for computing the LU factorization of a matrix using partial pivoting with row interchanges.
- [class MPSMatrixSolveLU](mpsmatrixsolvelu.md)
  A kernel for computing the solution of a linear system of equations using an LU factorization.
- [class MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
  A kernel that consumes one matrix and produces one matrix.
- [class MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.
- [enum MPSMatrixDecompositionStatus](mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsolvetriangular)*