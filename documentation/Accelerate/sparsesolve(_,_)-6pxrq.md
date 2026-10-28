# SparseSolve(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the equation *Subfactor \* X = B* in place for the vector of single-precision values *X*.

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

```c
static void SparseSolve(SparseOpaqueSubfactor_Float Subfactor, DenseVector_Float xb);
```

## Parameters

- `Subfactor`: The *Subfactor* in *Subfactor* *\* X = B* that [`SparseCreateSubfactor(_:_:)`](./sparsecreatesubfactor%28_,_%29-4renf.md) returns.
- `XB`: On input, the vector *B*. On return, the vector *X* overwrites it.

## See Also

### Vector-solving functions
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double)](./sparsesolve%28_,_%29-87v8w.md)
  Solves the equation *Subfactor \* X = B* in place for the vector of double-precision values *X*.
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double)](./sparsesolve%28_,_,_%29-g0wb.md)
  Solves the equation *Subfactor \* X = B* in place for the vector of double-precision values *X*.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float)](./sparsesolve%28_,_,_%29-5mq7s.md)
  Solves the equation *Subfactor \* X = B* in place for the vector of single-precision values *X*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-6pxrq)*