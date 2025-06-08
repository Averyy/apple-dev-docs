# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ B: DenseVector_Complex_Double, _ X: DenseVector_Complex_Double, _ workspace: UnsafeMutableRawPointer)
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by   .
- `workspace`: (Scratch) A workspace of size   .   This memory must be 16-byte aligned (any allocation returned   by   has this property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-9ui81)*