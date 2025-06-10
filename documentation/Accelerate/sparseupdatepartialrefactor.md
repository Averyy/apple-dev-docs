# SparseUpdatePartialRefactor

**Framework**: Accelerate  
**Kind**: var

Low-rank update algorithm selector

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
var SparseUpdatePartialRefactor: SparseUpdate_t { get }
```

#### Discussion

See `SparseUpdateFactor()` for a full description of these updates.

## See Also

- [func SparseGetInertia(SparseOpaqueFactorization_Float, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-6r90r.md)
  Returns the inertia of a single-precision  factorization.
- [func SparseGetInertia(SparseOpaqueFactorization_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-2ykzq.md)
  Returns the inertia of a double-precision  factorization.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-2gc7f.md)
  Returns the inertia of an LDLT factorization in complex double.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Float, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-6ca5h.md)
  Returns the inertia of an LDLT factorization in complex float.
- [struct SparseUpdate_t](sparseupdate_t.md)
  Low-rank update algorithm selector


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseupdatepartialrefactor)*