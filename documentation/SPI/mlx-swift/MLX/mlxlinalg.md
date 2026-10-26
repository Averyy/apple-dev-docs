---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg"
framework: "mlx-swift/MLX"
---

# MLXLinalg

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

## Declaration

```swift
enum MLXLinalg
```

## Topics

### Type Methods
- [static func cholesky(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/cholesky%28_,upper,stream%29.md)
  Compute the Cholesky decomposition of a real symmetric positive semi-definite matrix.
- [static func choleskyInv(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/choleskyinv%28_,upper,stream%29.md)
  Compute the inverse of a real symmetric positive semi-definite matrix using it’s Cholesky decomposition.
- [static func cross(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/cross%28_,_,axis,stream%29.md)
  Compute the cross product of two arrays along a specified axis.
- [static func det(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/det%28_,stream%29.md)
  Compute the determinant of a square matrix.
- [static func eig(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./mlxlinalg/eig%28_,stream%29.md)
  Compute the eigenvalues and eigenvectors of a square matrix.
- [static func eigh(MLXArray, UPLO: String, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./mlxlinalg/eigh%28_,uplo,stream%29.md)
  Compute the eigenvalues and eigenvectors of a complex Hermitian or real symmetric matrix.
- [static func eigvals(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/eigvals%28_,stream%29.md)
  Compute the eigenvalues of a square matrix.
- [static func eigvalsh(MLXArray, UPLO: String, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/eigvalsh%28_,uplo,stream%29.md)
  Compute the eigenvalues of a complex Hermitian or real symmetric matrix.
- [static func inv(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/inv%28_,stream%29.md)
  Compute the inverse of a square matrix.
- [static func lu(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray, MLXArray)](./mlxlinalg/lu%28_,stream%29.md)
  Compute the LU factorization of the given matrix `A`.
- [static func lu_factor(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./mlxlinalg/lu_factor%28_,stream%29.md)
  Computes a compact representation of the LU factorization.
- [static func norm(MLXArray, ord: Double, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/norm%28_,ord,axes,keepdims,stream%29-84m8i.md)
  Matrix or vector norm.
- [static func norm(MLXArray, ord: MLXLinalg.NormKind?, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/norm%28_,ord,axes,keepdims,stream%29-8fxpd.md)
  Matrix or vector norm.
- [static func norm(MLXArray, ord: Double, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/norm%28_,ord,axis,keepdims,stream%29-1lhic.md)
  Matrix or vector norm.
- [static func norm(MLXArray, ord: Double, axis: IntOrArray?, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/norm%28_,ord,axis,keepdims,stream%29-2il4p.md)
  Matrix or vector norm.
- [static func norm(MLXArray, ord: MLXLinalg.NormKind?, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/norm%28_,ord,axis,keepdims,stream%29-6hhyc.md)
  Matrix or vector norm.
- [static func norm(MLXArray, ord: MLXLinalg.NormKind?, axis: IntOrArray?, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/norm%28_,ord,axis,keepdims,stream%29-p4vv.md)
  Matrix or vector norm.
- [static func pinv(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/pinv%28_,stream%29.md)
  Compute the (Moore-Penrose) pseudo-inverse of a matrix.
- [static func qr(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./mlxlinalg/qr%28_,stream%29.md)
  The QR factorization of the input matrix.
- [static func slogdet(MLXArray, stream: StreamOrDevice) -> (sign: MLXArray, logabsdet: MLXArray)](./mlxlinalg/slogdet%28_,stream%29.md)
  Compute the sign and natural log of the absolute value of the determinant of a square matrix.
- [static func solve(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/solve%28_,_,stream%29.md)
  Compute the solution to a system of linear equations `AX = B`.
- [static func solveTriangular(MLXArray, MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/solvetriangular%28_,_,upper,stream%29.md)
  Computes the solution of a triangular system of linear equations `AX = B`.
- [static func svd(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/svd%28_,stream%29-1q0js.md)
  The Singular Value Decomposition (SVD) of the input matrix.
- [static func svd(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray, MLXArray)](./mlxlinalg/svd%28_,stream%29-90yr1.md)
  The Singular Value Decomposition (SVD) of the input matrix.
- [static func triInv(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./mlxlinalg/triinv%28_,upper,stream%29.md)
  Compute the inverse of a triangular square matrix.
### Enumerations
- [MLXLinalg.NormKind](./mlxlinalg/normkind.md)
  Types of norms available.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg)*