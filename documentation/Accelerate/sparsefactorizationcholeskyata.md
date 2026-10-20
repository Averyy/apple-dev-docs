# SparseFactorizationCholeskyAtA

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

A constant that represents *QR* factorization without storing *Q*.

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
var SparseFactorizationCholeskyAtA: SparseFactorization_t { get }
```

```c
SparseFactorizationCholeskyAtA
```

#### Discussion

[`SparseFactorizationCholeskyAtA`](./sparsefactorizationcholeskyata.md) provides an equivalent to *AᵀA = RᵀR.*

## See Also

### Factorization types for overdetermined and underdetermined systems
- [var SparseFactorizationQR: SparseFactorization_t](./sparsefactorizationqr.md)
  A constant that represents QR factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactorizationcholeskyata)*