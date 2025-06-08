# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve the equation `Subfactor * x = b` for the vector `x` of complex float values.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Float, _ B: DenseVector_Complex_Float, _ X: DenseVector_Complex_Float)
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by   ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-3hev5)*