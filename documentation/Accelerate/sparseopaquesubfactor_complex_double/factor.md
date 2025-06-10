# factor

**Framework**: Accelerate  
**Kind**: property

A semi-opaque type representing a matrix factorization in complex double.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var factor: SparseOpaqueFactorization_Complex_Double
```

#### Discussion

Use the `SparseCleanup` function to free resources held by these objects.

The object can be in one of the following states:

1. Something went wrong with symbolic factorization, nothing is valid. - indicated by `.symbolicFactorization.status < 0`
2. Symbolic factorization was good, but failed in numeric factorization initialization. - indicated by `.symbolicFactorization.status >= 0 && .status < 0 && .numericFactorization == NULL`
- symbolic factorization may be used for future calls.
3. Symbolic factorization was good, factor allocated/initialized correctly, but numeric factorization failed e.g. a Cholesky factorization of an indefinite matrix was attempted. - indicated by `.symbolicFactorization.status >= 0 && .status < 0 && .numericFactorization not NULL`
- user may pass this object to `SparseRefactor_Double` with a modified matrix
4. Symbolic and numeric factorizations are both good - indicated by `.status >= 0`


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesubfactor_complex_double/factor)*