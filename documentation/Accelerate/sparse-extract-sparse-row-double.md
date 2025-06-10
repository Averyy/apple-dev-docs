# sparse_extract_sparse_row_double(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Extracts values from a specified row of a double-precision sparse matrix.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func sparse_extract_sparse_row_double(_ A: sparse_matrix_double!, _ row: sparse_index, _ column_start: sparse_index, _ column_end: UnsafeMutablePointer<sparse_index>!, _ nz: sparse_dimension, _ val: UnsafeMutablePointer<Double>!, _ jndx: UnsafeMutablePointer<sparse_index>!) -> sparse_status
```

#### Return Value

On success `val` and `jndx` have been updated with the nonzero values of the `row`’th row, `column_end` holds the column index of the next nonzero value, and the number of nonzero values written are returned.  If `A` creation requirements are not met, [`SPARSE_ILLEGAL_PARAMETER`](sparse_illegal_parameter.md) is returned and `val` and `jndx` are unchanged.

#### Discussion

Extract the first `nz` values of the row beginning at `A[row,column_start]` for the sparse matrix `A`.  The number of nonzero values extracted is limited by `nz`, and the number of nonzero’s written to `jndx` and `val` are returned.  Additionally, the column index of the next nonzero value is returned in `column_end`. For example if `nz` is returned, not all nonzero values have been extracted, and a second extract can start from `column_end`.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `A`: The sparse matrix,  , which must have been created with  .   is returned if not met.
- `row`: The row for value extraction.
- `column_start`: The index of the column to start extraction.
- `column_end`: On return, holds the column index of the next nonzero value.
- `nz`: The number of values to extract from  .  Each of   and   are of size  .
- `val`: Pointer to array to hold the values extracted from the sparse matrix.  The value is extracted from the location specified by the corresponding indices of   and  .  Must be of size   elements.  If less than   nonzero values are found, then the last   elements of val are untouched.
- `jndx`: An array to hold the extracted column indices that correspond to the values in  . Note that these indices are relative to the matrix row and not the starting column index specified by  .  Returned indices are 0 based (first element of pointer is  ).  Must be of size   elements.

## See Also

- [func sparse_extract_sparse_row_float(sparse_matrix_float!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_float(_:_:_:_:_:_:_:).md)
  Extracts values from a specified row of a single-precision sparse matrix.
- [func sparse_extract_sparse_column_double(sparse_matrix_double!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Double>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_double(_:_:_:_:_:_:_:).md)
  Extracts values from a specified column of a double-precision sparse matrix.
- [func sparse_extract_sparse_column_float(sparse_matrix_float!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_float(_:_:_:_:_:_:_:).md)
  Extracts values from a specified column of a single-precision sparse matrix.
- [func sparse_extract_sparse_column_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_double_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_column_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_column_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_row_float_complex(sparse_matrix_float_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_float_complex(_:_:_:_:_:_:_:).md)
- [func sparse_extract_sparse_row_double_complex(sparse_matrix_double_complex!, sparse_index, sparse_index, UnsafeMutablePointer<sparse_index>!, sparse_dimension, OpaquePointer!, UnsafeMutablePointer<sparse_index>!) -> sparse_status](sparse_extract_sparse_row_double_complex(_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_extract_sparse_row_double(_:_:_:_:_:_:_:))*