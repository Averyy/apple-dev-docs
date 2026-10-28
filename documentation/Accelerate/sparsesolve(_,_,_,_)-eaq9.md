# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the equation *Subfactor \* X = B* for the vector of double-precision values *X*, without any internal memory allocations.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Double, _ B: DenseVector_Double, _ X: DenseVector_Double, _ workspace: UnsafeMutableRawPointer)
```

```c
static void SparseSolve(SparseOpaqueSubfactor_Double Subfactor, DenseVector_Double b, DenseVector_Double x, void *workspace);
```

## Parameters

- `Subfactor`: The *Subfactor* in *Subfactor* *\* X = B* that [`SparseCreateSubfactor(_:_:)`](./sparsecreatesubfactor%28_,_%29-4renf.md) returns.
- `B`: The vector *B*.
- `X`: The vector *X*.
- `workspace`: A workspace of size `workspaceRequiredStatic` `+` `workspaceRequiredPerRHS`.

## See Also

### Vector-solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-7auge.md)
  Solves the equation *Subfactor \* X = B* for the vector of double-precision values *X*, in place and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-1xw9b.md)
  Solves the equation *Subfactor \* X = B* for the vector of single-precision values *X*, in place and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-2p6e3.md)
  Solves the equation *Subfactor \* X = B* for the vector of single-precision values *X*, without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-eaq9)*