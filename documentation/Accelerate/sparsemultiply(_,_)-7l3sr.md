# SparseMultiply(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs the multiply operation *Y = Subfactor * X*, in place on a vector of single-precision values.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Float, _ XY: DenseVector_Float)
```

```c
static void SparseMultiply(SparseOpaqueSubfactor_Float Subfactor, DenseVector_Float xy);
```

## Parameters

- `Subfactor`: The subfactor to multiply by, which [`SparseCreateSubfactor(_:_:)`](./sparsecreatesubfactor%28_,_%29-4renf.md) returns.
- `XY`: On input, the vector *X*. On return, the vector *Y* overwrites it.

## See Also

### Subfactor and dense vector multiplication
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double)](./sparsemultiply%28_,_%29-8ehhn.md)
  Performs the multiply operation *Y = Subfactor * X*, in place on a vector of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double)](./sparsemultiply%28_,_,_%29-6abql.md)
  Performs the multiply operation *Y = Subfactor * X* on a vector of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseVector_Float, DenseVector_Float)](./sparsemultiply%28_,_,_%29-2h425.md)
  Performs the multiply operation *Y = Subfactor ** *X* on a vector of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](./sparsemultiply%28_,_%29-3s0hu.md)
  Perform the multiply operation `Y = Subfactor * X` in place for complex double values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double)](./sparsemultiply%28_,_%29-9fn7j.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values, in place.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](./sparsemultiply%28_,_,_%29-4fwfv.md)
  Perform the multiply operation `y = Subfactor * x` for complex double values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](./sparsemultiply%28_,_,_%29-58wuo.md)
  Perform the multiply operation `y = Subfactor * x` for complex float values..
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiply%28_,_,_%29-6wrnf.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:)-7l3sr)*