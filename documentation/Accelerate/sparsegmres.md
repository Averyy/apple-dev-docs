# SparseGMRES(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a generalized minimal residual (GMRES) method with specified options.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseGMRES(_ options: SparseGMRESOptions) -> SparseIterativeMethod
```

#### Return Value

A [`SparseIterativeMethod`](sparseiterativemethod.md) structure that represents a generalized minimal residual (GMRES) method.

#### Discussion

Use GMRES to solve  when  is symmetric indefinite or unsymmetric.

For symmetric positive-definite systems, use [`SparseConjugateGradient(_:)`](sparseconjugategradient(_:).md). For rectangular or singular systems, use [`SparseLSMR(_:)`](sparselsmr(_:).md).

## Parameters

- `options`: The options to use when creating the GMRES method, such as the maximum number of iterations to perform.

## See Also

- [func SparseGMRES() -> SparseIterativeMethod](sparsegmres().md)
  Returns a generalized minimal residual (GMRES) method.
- [struct SparseGMRESOptions](sparsegmresoptions.md)
  Options for creating a generalized minimal residual (GMRES) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmres(_:))*