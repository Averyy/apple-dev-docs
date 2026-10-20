# SparseMultiply(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Perform the multiply operation `y = Subfactor * x` for complex floatr values, in place.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Complex_Float, _ XY: DenseVector_Complex_Float)
```

```c
static void SparseMultiply(SparseOpaqueSubfactor_Complex_Float Subfactor, DenseVector_Complex_Float xy);
```

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by `SparseCreateSubfactor()`.

## See Also

### Subfactor and dense matrix multiplication
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double)](./sparsemultiply%28_,_%29-88trz.md)
  Performs the multiply operation *Y* *= Subfactor * X,* __in place on a dense matrix of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float)](./sparsemultiply%28_,_%29-3r4mf.md)
  Performs the multiply operation *Y*_ _*= Subfactor * X*, in place on a dense matrix of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double)](./sparsemultiply%28_,_,_%29-4nosz.md)
  Performs the multiply operation *Y* *= Subfactor * X* on a dense matrix of double-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsemultiply%28_,_,_%29-88stx.md)
  Performs the multiply operation *Y* *= Subfactor * X* on a dense matrix of single-precision values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiply%28_,_%29-34fp6.md)
  Perform the multiply operation `Y = Subfactor * X` in place for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiply%28_,_,_%29-6wrnf.md)
  Perform the multiply operation `Y = Subfactor * X` for complex float values.
- [func SparseMultiply(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](./sparsemultiply%28_,_,_%29-7q8gs.md)
  Perform the multiply operation `Y = Subfactor * X` for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:)-3dwed)*