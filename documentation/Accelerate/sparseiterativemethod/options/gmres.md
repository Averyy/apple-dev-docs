# gmres

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

Right-preconditioned (F/DQ)GMRES Parameters Options.

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
SparseGMRESOptions gmres;
```

## Discussion

Use (F/DQ)GMRES to solve `Ax=b` when `A` is symmetric (Hermitian) indefinite or unsymmetric.

For symmetric (Hermitian) positive-definite systems, use CG instead. For rectangular or singular systems, use LSMR instead.

- **`reportError`**: Function to use to report parameter errors.

  If `NULL`, errors are logged via `<os/log.h>` and execution is halted via `__builtin_trap()`.  If non-`NULL`, the provided function is called with a human-readable string describing the error condition. If the callback returns, control will be returned to the caller with any outputs in a safe but undefined state (i.e. they may hold partial results or garbage, but all sizes and pointers are valid).
- **`variant`**: Variant of GMRES to use. See definition of `SparseGMRESVariant_t` for further information on the available variants.
- **`nvec`**: Number of orthagonal vectors maintained. For GMRES and FGMRES variants, this is the number of iterations between restarts. For DQGMRES it is the number of historical vectors maintained in memory.

  If `nvec<=0`, the default value of 16 is used.
- **`maxIterations`**: Maximum number of iterations to perform. If 0, the default value of 100 is used.
- **`atol`**: Absolute convergence tolerance. Iterate is considered to have converged if

  ```
  || b-Ax ||_2 < rtol * || b-Ax_0 ||_2 + atol
  ```
- **`rtol`**: Relative convergence tolerance. Iterate is considered to have converged if

  ```
  || b-Ax ||_2 < rtol * || b-Ax_0 ||_2 + atol
  ```

  If r`tol = 0.0`, default value of `sqrt(epsilon)` is used. If negative, `rtol` is treated as `0.0 `(default is not used).
- **`reportStatus`**: Function to use to report status (iteration count and residual of first right-hand side) every few iterations.

  If NULL, status is not reported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterativemethod/options/gmres)*