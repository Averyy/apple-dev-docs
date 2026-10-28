# la_scale_with_double(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0
- tvOS 8.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 7.0

> **Deprecated**: This API is deprecated, please use BLAS and LAPACK

## Declaration

```swift
func la_scale_with_double(_ matrix: la_object_t, _ scalar: Double) -> la_object_t
```

```c
extern la_object_tla_scale_with_double(la_object_t matrix, double scalar);
```

## Discussion

Multiply a matrix or vector by a scalar given by a double.

Returns a matrix whose entries are the product of the scalar and the corresponding element of the source matrix.  If the source object is not a vector or matrix, the returned object will have status LA_INVALID_PARAMETER_ERROR.

If the scalar type of matrix is not double LA_PRECISION_MISMATCH_ERROR is returned.

## See Also

### Functions
- [func caxpy_(UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./caxpy_%28_,_,_,_,_,_%29.md)
- [func ccopy_(UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./ccopy_%28_,_,_,_,_%29.md)
- [func cdotc_(OpaquePointer, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cdotc_%28_,_,_,_,_,_%29.md)
- [func cdotu_(OpaquePointer, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cdotu_%28_,_,_,_,_,_%29.md)
- [func cgbmv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgbmv_%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func cgemm_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgemm_%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func cgemv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgemv_%28_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func cgerc_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgerc_%28_,_,_,_,_,_,_,_,_%29.md)
- [func cgeru_(UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cgeru_%28_,_,_,_,_,_,_,_,_%29.md)
- [func chbmv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./chbmv_%28_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func chemm_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./chemm_%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func chemv_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./chemv_%28_,_,_,_,_,_,_,_,_,_%29.md)
- [func cher2_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cher2_%28_,_,_,_,_,_,_,_,_%29.md)
- [func cher2k_(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<__LAPACK_int>, OpaquePointer, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cher2k_%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func cher_(UnsafePointer<CChar>, UnsafePointer<__LAPACK_int>, UnsafePointer<Float>, OpaquePointer?, UnsafePointer<__LAPACK_int>, OpaquePointer?, UnsafePointer<__LAPACK_int>)](./cher_%28_,_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/la_scale_with_double(_:_:))*