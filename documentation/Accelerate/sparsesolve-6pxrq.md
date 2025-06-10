# SparseSolve(_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the equation  in place for the vector of single-precision values .

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Float, _ XB: DenseVector_Float)
```

## Parameters

- `Subfactor`: The   in     that   returns.
- `XB`: On input, the vector  . On return, the vector   overwrites it.

## See Also

- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double)](sparsesolve(_:_:)-87v8w.md)
  Solves the equation  in place for the vector of double-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double)](sparsesolve(_:_:_:)-g0wb.md)
  Solves the equation  in place for the vector of double-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float)](sparsesolve(_:_:_:)-5mq7s.md)
  Solves the equation  in place for the vector of single-precision values .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-6pxrq)*