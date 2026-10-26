# lsmr

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

LSMR is MINRES specialised for solving least squares.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
SparseLSMROptions lsmr;
```

#### Discussion

Use LSMR to solve equations of the form Ax=b where an exact solution does not exist. The returned solution minimises || b-Ax ||_2.

Whilst LSMR is equivalent to MINRES applied to the normal equations `A^TAx = A^Tb` in exact arithmetic, it has superior numerical behaviour and should be used in preference.

We note that due to the implicit squaring of the condition of A in the normal equations, LSMR may struggle to converge in single precision, and double precision arithmetic is recommended.

For symmetric (Hermitian) positive-definite systems, use CG instead. For square, full rank unsymmetric or indefinite equations, use GMRES instead.

- **`reportError`**: Function to use to report parameter errors.

  If `NULL`, errors are logged via `<os/log.h>` and execution is halted via `__builtin_trap()`.  If non-`NULL`, the provided function is called with a human-readable string describing the error condition. If the callback returns, control will be returned to the caller with any outputs in a safe but undefined state (i.e. they may hold partial results or garbage, but all sizes and pointers are valid).
- **`lambda`**: Damping parameter, if non-zero the actual problem solved is

  ```
        min_x || Ax-b ||_2 + lambda || x ||_2.
  ```

  Using damping can often allow the iteration to converge on ill-conditioned systems.
- **`variant`**: Variant of GMRES to use. See definition of `SparseGMRESVariant_t` for further information on the available variants.
- **`nvec`**: Number of vectors used for local orthogonalization. If n`vec<=0`, no orthogonalization is performed.
- **`convergenceTest`**: Which convergence test to use. See definition of `SparseLSMRConvergenceTest_t` for further information.
- **`maxIterations`**: Maximum number of iterations to perform. If 0, the default value of 4n is used.

  However, if a good preconditioner is available and/or the matrix is well conditioned such that singular values are clustered, a value of n/2 may be more appropriate.
- **`atol`**: Either absolute tolerance (default test) or A tolerance (Fong-Saunders test). In the Fong and Saunders case, it should hold an estimate of the relative error in the data defining the matrix A. For example, if A is accurate to about 6 digits, set atol = 1.0e-6. In the Fong and Saunders case, if atol is 0.0, it is treated as machine epsilon. If using the default test, a value of 0.0 is treated as 0.0.
- **`rtol`**: Relative convergence tolerance (default test only). If `rtol = 0.0`, default value of `sqrt(epsilon)` is used. If negative, `rtol` is treated as 0.0 (default is not used).
- **`btol`**: b tolerance (Fong-Saunders test only). It should hold an estimate of the relative error in the data defining the rhs b. For example, if b is accurate to about 6 digits, set btol = 1.0e-6. If btol is zero, it is treated as machine epsilon.
- **`conditionLimit`**: Condition number limit (Fong-Saunders test). Iterations will be terminated if a computed estimate of cond(Abar) exceeds this value. This is intended to prevent certain small or zero singular values of A or Abar from coming into effect and causing unwanted growth in the computed solution.

  conditionLimit and lambda may be used separately or together to regularize ill-conditioned systems.

  Normally, conlim should be in the range 1000 to 1/eps. Suggested value:

  - `conditionLimit = 1/(100*eps)`  for compatible systems,
  - `conditionLimit = 1/(10*sqrt(eps))` for least squares.

  If `conditionLimit` is `0.0,` it is treated as `1/eps`.
- **`reportStatus`**: Function to use to report status (iteration count and residual of first right-hand side) every few iterations. If NULL, status is not reported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterativemethod/options/lsmr)*