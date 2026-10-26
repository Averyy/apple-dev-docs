# sparse_outer_product_dense_double_complex

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```c
sparse_status sparse_outer_product_dense_double_complex(sparse_dimension M, sparse_dimension N, sparse_dimension nz, _Complex double alpha, const _Complex double * restrictx, sparse_stride incx, const _Complex double * restricty, const sparse_index * restrictindy, sparse_matrix_double_complex* restrictC);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_outer_product_dense_double_complex)*