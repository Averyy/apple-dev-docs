# sparse_insert_entry_float(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Inserts a single scalar entry into a single-precision sparse matrix.

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
func sparse_insert_entry_float(_ A: sparse_matrix_float!, _ val: Float, _ i: sparse_index, _ j: sparse_index) -> sparse_status
```

#### Return Value

On successful insertion, `A` has been updated with the value and [`SPARSE_SUCCESS`](sparse_success.md) is returned.  If `A` creation requirements are not met, [`SPARSE_ILLEGAL_PARAMETER`](sparse_illegal_parameter.md) is returned and `A` is unchanged.

#### Discussion

Use to build a sparse matrix by inserting one scalar entry at a time.  This function is the equivalent of `A[i,j] = val`.

Note that matrix properties cannot be modified after value insertion begins. This includes properties such as specifying a triangular matrix.

Insertion can be expensive, generally speaking it is best to do a batch update.

Inserted values may be temporarily held internally within the object and only inserted into the sparse format when a later computation triggers a need to insert.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 19, iPadOS 19, macOS 16, tvOS 19, watchOS 19, and visionOS 3, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `A`: The sparse matrix,  , which must have been created with  .   is returned if not met.
- `val`: The scalar value to insert into the sparse matrix.
- `i`: The row location to insert the value. Indices are 0 based (first element of  pointer is  ).  Indices expected to be in the bounds of matrix dimensions, undefined behavior if not met.
- `j`: The column location to insert the value. Indices are 0 based (first element of  pointer is ptr[0]).  Indices expected to be in the bounds of matrix dimensions, undefined behavior if not met.

## See Also

- [func sparse_matrix_create_double(sparse_dimension, sparse_dimension) -> sparse_matrix_double!](sparse_matrix_create_double(_:_:).md)
  Returns a double-precision sparse matrix object.
- [func sparse_matrix_create_float(sparse_dimension, sparse_dimension) -> sparse_matrix_float!](sparse_matrix_create_float(_:_:).md)
  Returns a single-precision sparse matrix object.
- [func sparse_insert_entry_double(sparse_matrix_double!, Double, sparse_index, sparse_index) -> sparse_status](sparse_insert_entry_double(_:_:_:_:).md)
  Inserts a single scalar entry into a double-precision sparse matrix.
- [func sparse_insert_entries_double(sparse_matrix_double!, sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_double(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a double-precision sparse matrix.
- [func sparse_insert_entries_float(sparse_matrix_float!, sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_entries_float(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single-precision sparse matrix.
- [func sparse_insert_col_double(sparse_matrix_double!, sparse_index, sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_double(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single column of a double-precision sparse matrix.
- [func sparse_insert_col_float(sparse_matrix_float!, sparse_index, sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_col_float(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single column of a single-precision sparse matrix.
- [func sparse_insert_row_double(sparse_matrix_double!, sparse_index, sparse_dimension, UnsafePointer<Double>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_double(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single row of a double-precision sparse matrix.
- [func sparse_insert_row_float(sparse_matrix_float!, sparse_index, sparse_dimension, UnsafePointer<Float>!, UnsafePointer<sparse_index>!) -> sparse_status](sparse_insert_row_float(_:_:_:_:_:).md)
  Inserts a list of scalar entries into a single row of a single-precision sparse matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_insert_entry_float(_:_:_:_:))*