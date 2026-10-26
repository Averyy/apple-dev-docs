# sparse_matrix_product_dense_float_complex

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
sparse_status sparse_matrix_product_dense_float_complex(enum CBLAS_ORDER order, enum CBLAS_TRANSPOSE transa, sparse_dimension n, _Complex float alpha, sparse_matrix_float_complex A, const _Complex float * restrictB, sparse_dimension ldb, _Complex float * restrictC, sparse_dimension ldc);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse_matrix_product_dense_float_complex)*