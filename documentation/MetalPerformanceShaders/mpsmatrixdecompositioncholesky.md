# MPSMatrixDecompositionCholesky

**Framework**: Metal Performance Shaders  
**Kind**: class

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

#### Overview

This kernel computes one of the following factorizations of a matrix :

where:

-  is a symmetric positive-definite matrix for which the factorization is to be computed
-  is the lower triangular matrix
-  is the upper triangular matrix

## Topics

### Initializers
- [init(device: any MTLDevice, lower: Bool, order: Int)](mpsmatrixdecompositioncholesky/init(device:lower:order:).md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, resultMatrix: MPSMatrix, status: (any MTLBuffer)?)](mpsmatrixdecompositioncholesky/encode(commandbuffer:sourcematrix:resultmatrix:status:).md)

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

- [class MPSMatrixSolveCholesky](mpsmatrixsolvecholesky.md)
  A kernel for computing the solution of a linear system of equations using a Cholesky factorization.
- [class MPSMatrixDecompositionLU](mpsmatrixdecompositionlu.md)
  A kernel for computing the LU factorization of a matrix using partial pivoting with row interchanges.
- [class MPSMatrixSolveLU](mpsmatrixsolvelu.md)
  A kernel for computing the solution of a linear system of equations using an LU factorization.
- [class MPSMatrixSolveTriangular](mpsmatrixsolvetriangular.md)
  A kernel for computing the solution of a linear system of equations using a triangular coefficient matrix.
- [class MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
  A kernel that consumes one matrix and produces one matrix.
- [class MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.
- [enum MPSMatrixDecompositionStatus](mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdecompositioncholesky)*