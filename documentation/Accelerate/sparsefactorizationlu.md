# SparseFactorizationLU

**Framework**: Accelerate  
**Kind**: var

Default LU factorization, currently LU with TPP.

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
var SparseFactorizationLU: SparseFactorization_t { get }
```

## See Also

- [var SparseFactorizationLUSPP: SparseFactorization_t](sparsefactorizationluspp.md)
  LU factorization with partial pivoting restricted to within supernodes only.
- [var SparseFactorizationLUTPP: SparseFactorization_t](sparsefactorizationlutpp.md)
  LU factorization with threshold partial pivoting.
- [var SparseFactorizationLUUnpivoted: SparseFactorization_t](sparsefactorizationluunpivoted.md)
  LU factorization with no numerical pivoting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactorizationlu)*