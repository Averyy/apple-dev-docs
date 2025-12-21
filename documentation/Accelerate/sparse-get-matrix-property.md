# sparse_get_matrix_property(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the value of the given property name.

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
func sparse_get_matrix_property(_ A: UnsafeMutableRawPointer!, _ pname: sparse_matrix_property) -> Int
```

#### Return Value

Returns the value of the property for a valid object and property, or 0 otherwise.

#### Discussion

Returns the value of the given property name. See matrix properties enumeration for further property details.

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. Starting with iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26, the libraries are in line with LAPACK 3.12.0. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## Parameters

- `A`: The sparse matrix object.
- `pname`: The property name to get the value of.  See   for options.

## See Also

- [func sparse_commit(UnsafeMutableRawPointer!) -> sparse_status](sparse_commit(_:).md)
  Puts values that you recently added to the matrix into the internal sparse storage format.
- [func sparse_matrix_destroy(UnsafeMutableRawPointer!) -> sparse_status](sparse_matrix_destroy(_:).md)
  Releases any memory associated with the matrix object.
- [func sparse_set_matrix_property(UnsafeMutableRawPointer!, sparse_matrix_property) -> sparse_status](sparse_set_matrix_property(_:_:).md)
  Sets the given property for a matrix object.
- [func sparse_get_matrix_number_of_rows(UnsafeMutableRawPointer!) -> sparse_dimension](sparse_get_matrix_number_of_rows(_:).md)
  Returns the number of rows of a matrix.
- [func sparse_get_matrix_number_of_columns(UnsafeMutableRawPointer!) -> sparse_dimension](sparse_get_matrix_number_of_columns(_:).md)
  Returns the number of columns of a matrix.
- [func sparse_get_matrix_nonzero_count(UnsafeMutableRawPointer!) -> Int](sparse_get_matrix_nonzero_count(_:).md)
  Returns the number of nonzero values of a matrix.
- [func sparse_get_matrix_nonzero_count_for_row(UnsafeMutableRawPointer!, sparse_index) -> Int](sparse_get_matrix_nonzero_count_for_row(_:_:).md)
  Returns the number of nonzero values in a row of a matrix.
- [func sparse_get_matrix_nonzero_count_for_column(UnsafeMutableRawPointer!, sparse_index) -> Int](sparse_get_matrix_nonzero_count_for_column(_:_:).md)
  Returns the number of nonzero values in a column of a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_get_matrix_property(_:_:))*