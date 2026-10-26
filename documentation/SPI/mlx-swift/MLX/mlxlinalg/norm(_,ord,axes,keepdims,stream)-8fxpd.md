---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/norm(_:ord:axes:keepdims:stream:)-8fxpd"
framework: "mlx-swift/MLX"
---

# norm(_:ord:axes:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Matrix or vector norm.

## Declaration

```swift
static func norm(_ array: MLXArray, ord: MLXLinalg.NormKind? = nil, axes: some Collection<Int>, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

Output containing the norm(s)

#### Discussion

For values of `ord < 1`, the result is, strictly speaking, not a mathematical norm, but it may still be useful for various numerical purposes.

The following norms can be calculated:

| ord | norm for matrices | norm for vectors |
| --- | --- | --- |
| None | Frobenius norm | 2-norm |
| ‘fro’ | Frobenius norm | – |
| inf | max(sum(abs(x), axis-1)) | max(abs(x)) |
| -inf | min(sum(abs(x), axis-1)) | min(abs(x)) |
| 0 | – | sum(x !- 0) |
| 1 | max(sum(abs(x), axis-0)) | as below |
| -1 | min(sum(abs(x), axis-0)) | as below |
| 2 | 2-norm (largest sing. value) | as below |
| -2 | smallest singular value | as below |
| other | – | sum(abs(x)**ord)**(1./ord) |

Nuclear norm and norms based on singular values are implemented by the linalg backend.

The Frobenius norm is given by G. H. Golub and C. F. Van Loan, *Matrix Computations*, Baltimore, MD, Johns Hopkins University Press, 1985, pg. 15

The nuclear norm is the sum of the singular values.

Both the Frobenius and nuclear norm orders are only defined for matrices and produce a fatal error when `array.ndim != 2`

##### See Also

- [`norm(_:ord:axes:keepDims:stream:)`](./norm%28_,ord,axes,keepdims,stream%29-8fxpd.md)

## Parameters

- `array`: Input array
- `ord`: Order of the norm, see table
- `axes`: Axes that hold 2d matrices
- `keepDims`: If `true` the axes which are normed over are left in the result as dimensions with size one
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlinalg/norm(_:ord:axes:keepdims:stream:)-8fxpd)*