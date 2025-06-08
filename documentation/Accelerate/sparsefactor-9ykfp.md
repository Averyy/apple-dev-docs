# SparseFactor(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the specified factorization of a sparse matrix of complex float values, using the specified options.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseFactor(_ type: SparseFactorization_t, _ Matrix: SparseMatrix_Complex_Float, _ options: SparseSymbolicFactorOptions, _ nfoptions: SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float
```

#### Return Value

Factorization of Matrix.

## Parameters

- `type`: The type of factorization to perform.
- `Matrix`: The matrix to factorize.
- `nfoptions`: Numeric factor options, for example pivoting parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:_:_:)-9ykfp)*