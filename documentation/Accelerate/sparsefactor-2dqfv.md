# SparseFactor(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.

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
func SparseFactor(_ symbolicFactor: SparseOpaqueSymbolicFactorization, _ Matrix: SparseMatrix_Complex_Float, _ nfoptions: SparseNumericFactorOptions, _ factorStorage: UnsafeMutableRawPointer?, _ workspace: UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Float
```

#### Return Value

Factorization of Matrix.

#### Discussion

Note that internal memory allocations may occur in the case of pivoted factorizations that result in delayed pivots. If you require closer control over memory allocations, supply a `sfoptions.malloc()` function that implements the required behaviour, or use an alternative non-pivoted factorization returns. Note that if `sfoptions.malloc()` returns NULL the factorization will abort immediately.

## Parameters

- `Matrix`: The matrix to factorize.
- `nfoptions`: Numeric factor options, for example pivoting parameters.
- `factorStorage`: A pointer to space used to store the factorization   of size at least   bytes. This storage   should not be altered by the user during the lifetime of the return   value. This memory must be 16-byte aligned (any allocation returned   by malloc() has this property).
- `workspace`: A pointer to a workspace of size at least    bytes. This workspace may be   reused or destroyed by the user as soon as the function returns.   This memory must be 16-byte aligned (any allocation returned   by   has this property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:_:_:_:)-2dqfv)*