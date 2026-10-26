---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg"
framework: "mlx-swift/MLXLinalg"
---

# MLXLinalg

**Framework**: mlx-swift/MLXLinalg  
**Kind**: module  
**Role**: Framework

## Topics

### Variables
- [let deprecationWarning: Void](./deprecationwarning.md)
### Functions
- [func cholesky(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./cholesky%28_,upper,stream%29.md)
  Compute the Cholesky decomposition of a real symmetric positive semi-definite matrix.
- [func choleskyInv(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./choleskyinv%28_,upper,stream%29.md)
  Compute the inverse of a real symmetric positive semi-definite matrix using it’s Cholesky decomposition.
- [func cross(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./cross%28_,_,axis,stream%29.md)
  Compute the cross product of two arrays along a specified axis.
- [func inv(MLXArray, stream: StreamOrDevice) -> MLXArray](./inv%28_,stream%29.md)
  Compute the inverse of a square matrix.
- [func lu(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray, MLXArray)](./lu%28_,stream%29.md)
  Compute the LU factorization of the given matrix `A`.
- [func lu_factor(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./lu_factor%28_,stream%29.md)
  Computes a compact representation of the LU factorization.
- [func norm(MLXArray, ord: Double, axes: [Int], keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axes,keepdims,stream%29-3t3ay.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: MLXLinalg.NormKind?, axes: [Int], keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axes,keepdims,stream%29-ugz6.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: MLXLinalg.NormKind?, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axis,keepdims,stream%29-2cn9x.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: MLXLinalg.NormKind?, axis: IntOrArray?, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axis,keepdims,stream%29-6eux3.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: Double, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axis,keepdims,stream%29-7fnqw.md)
  Matrix or vector norm.
- [func norm(MLXArray, ord: Double, axis: IntOrArray?, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./norm%28_,ord,axis,keepdims,stream%29-92jgz.md)
  Matrix or vector norm.
- [func qr(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./qr%28_,stream%29.md)
  The QR factorization of the input matrix.
- [func solve(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./solve%28_,_,stream%29.md)
  Compute the solution to a system of linear equations `AX = B`.
- [func solveTriangular(MLXArray, MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./solvetriangular%28_,_,upper,stream%29.md)
  Computes the solution of a triangular system of linear equations `AX = B`.
- [func svd(MLXArray, stream: StreamOrDevice) -> (MLXArray, MLXArray, MLXArray)](./svd%28_,stream%29.md)
  The Singular Value Decomposition (SVD) of the input matrix.
- [func triInv(MLXArray, upper: Bool, stream: StreamOrDevice) -> MLXArray](./triinv%28_,upper,stream%29.md)
  Compute the inverse of a triangular square matrix.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxlinalg)*