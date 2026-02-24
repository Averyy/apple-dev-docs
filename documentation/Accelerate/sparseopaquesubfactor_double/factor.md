# factor

**Framework**: Accelerate  
**Kind**: property

A semi-opaque type representing a matrix factorization in double.

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
var factor: SparseOpaqueFactorization_Double
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

- **`status`**: Indicates status of factorization object.
- **`attributes`**: Flags associated with this factorization object. In particular, transpose field indicates whether object is considered to be factorization of A or A^T.
- **`symbolicFactorization`**: Symbolic Factorization upon which this Numeric Factorization depends.
- **`userFactorStorage`**: Flag that indicates if user provided storage backing this object. If true, then factor storage must be freed by the user once all references are finished with (though any additional storage allocated due to pivoting will still be freed by `SparseCleanup`).
- **`numericFactorization`**: Pointer to private internal representation of numeric factor.
- **`solveWorkspaceRequiredStatic`**: The required size of workspace, in bytes, for a call to `SparseSolve` is `solveWorkspaceRequiredStatic + nrhs * solveWorkspaceRequiredPerRHS` where `nrhs` is the number of right-hand side vectors.
- **`solveWorkspaceRequiredPerRHS`**: The required size of workspace, in bytes, for a call to `SparseSolve` is `solveWorkspaceRequiredStatic + nrhs * solveWorkspaceRequiredPerRHS` where `nrhs` is the number of right-hand side vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesubfactor_double/factor)*