# SparseUpdate_t

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Low-rank update algorithm selector

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct SparseUpdate_t
```

```c
typedef enum { ... } SparseUpdate_t;
```

#### Overview

See `SparseUpdateFactor()` for a full description of these updates.

- **`SparseUpdatePartialRefactor`**: Perform update using a partial refactorization of the matrix

## Topics

### Initializers
- [init(UInt8)](./sparseupdate_t/init%28_%29.md)
- [init(rawValue: UInt8)](./sparseupdate_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt8](./sparseupdate_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Factorization inertia functions
- [func SparseGetInertia(SparseOpaqueFactorization_Float, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](./sparsegetinertia%28_,_,_,_%29-6r90r.md)
  Returns the inertia of a single-precision *LDLᵀ* factorization.
- [func SparseGetInertia(SparseOpaqueFactorization_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](./sparsegetinertia%28_,_,_,_%29-2ykzq.md)
  Returns the inertia of a double-precision *LDLᵀ* factorization.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](./sparsegetinertia%28_,_,_,_%29-2gc7f.md)
  Returns the inertia of an LDLT factorization in complex double.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Float, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](./sparsegetinertia%28_,_,_,_%29-6ca5h.md)
  Returns the inertia of an LDLT factorization in complex float.
- [var SparseUpdatePartialRefactor: SparseUpdate_t](./sparseupdatepartialrefactor.md)
  Low-rank update algorithm selector


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseupdate_t)*