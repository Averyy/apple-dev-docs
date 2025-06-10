# la_matrix_product(_:_:)

**Framework**: Accelerate  
**Kind**: func

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func la_matrix_product(_ matrix_left: la_object_t, _ matrix_right: la_object_t) -> la_object_t
```

#### Discussion

Compute a matrix product.

Left splat operands are treated as 1 x rows(matrix_right) vectors and right splat operands are treated as cols(matrix_left) x 1 vectors.

For convenience, in certain situations vector operands may be implicitly transposed.  Specifically,

If cols(matrix_left) == rows(matrix_right) rows(matrix_left) x cols(matrix_right) = matrix_left * matrix_right Else if cols(matrix_left) == 1 and rows(matrix_left) == rows(matrix_right) 1 x cols(matrix_right) = transpose(matrix_left) * matrix_right Else if rows(matrix_right) == 1 and cols(matrix_left) == cols(matrix_right) rows(matrix_left) x 1 = matrix_left * transpose(matrix_right) Else result has the status LA_DIMENSION_MISMATCH_ERROR.

If either operand is not a vector or matrix or splat, or if both operands are splats, the result has the status LA_INVALID_PARAMETER_ERROR.

Otherwise the result is a matrix with 1 row if matrix_left is vector or splat and rows(matrix_left) otherwise, and 1 column if matrix_right is vector or splat and cols(matrix_right) otherwise.

If cols(matrix_left) == rows(matrix_right), the i,jth element of the matrix is: sum_{k=0…cols(matrix_left)} matrix_left[i,k] * matrix_right[k,j] If cols(matrix_left) == 1 and rows(matrix_left) == rows(matrix_right), the 0,jth element of matrix is: sum_{k=0…rows(matrix_right)} matrix_left[k,0] * matrix_right[k,j] If rows(matrix_right) == 1 and cols(matrix_left) == cols(matrix_right), the i,0th element of matrix is: sum_{k=0…cols(matrix_left)} matrix_left[i,k] * matrix_right[0,k]

## See Also

- [func caxpy_(UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](caxpy_(_:_:_:_:_:_:).md)
- [func ccopy_(UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](ccopy_(_:_:_:_:_:).md)
- [func cdotc_(OpaquePointer, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cdotc_(_:_:_:_:_:_:).md)
- [func cdotu_(OpaquePointer, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cdotu_(_:_:_:_:_:_:).md)
- [func cgbmv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgbmv_(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgemm_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgemm_(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgemv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgemv_(_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cgerc_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgerc_(_:_:_:_:_:_:_:_:_:).md)
- [func cgeru_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cgeru_(_:_:_:_:_:_:_:_:_:).md)
- [func chbmv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](chbmv_(_:_:_:_:_:_:_:_:_:_:_:).md)
- [func chemm_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](chemm_(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func chemv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](chemv_(_:_:_:_:_:_:_:_:_:_:).md)
- [func cher2_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cher2_(_:_:_:_:_:_:_:_:_:).md)
- [func cher2k_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cher2k_(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func cher_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](cher_(_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/la_matrix_product(_:_:))*