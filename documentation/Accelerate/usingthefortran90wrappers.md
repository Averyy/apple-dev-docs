# Using the Fortran 90 wrappers for Accelerate BLAS and LAPACK

**Framework**: Accelerate

Call BLAS and LAPACK routines from Fortran 90 source code.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

#### Overview

Accelerate ships a set of Fortran 90 interface modules that bind Fortran source to the `ACCELERATE_NEW_LAPACK` symbols in the Accelerate framework. The modules declare every BLAS and LAPACK routine with explicit Fortran interfaces, so the compiler can check argument types and shapes at the call site. You don’t link a separate library — the interface module compiles alongside your program and resolves directly to Accelerate.

Four interface modules ship with the SDK:

| Module file | API | Integer width |
| --- | --- | --- |
| `accelerate_blas_lp64.f90` | BLAS | LP64 — default `integer` (4 bytes) |
| `accelerate_blas_ilp64.f90` | BLAS | ILP64 — `integer(8)` (8 bytes) |
| `accelerate_lapack_lp64.f90` | LAPACK | LP64 — default `integer` (4 bytes) |
| `accelerate_lapack_ilp64.f90` | LAPACK | ILP64 — `integer(8)` (8 bytes) |

Use the LP64 modules with code that relies on Fortran’s default 4-byte integer. Use the ILP64 modules when you need 8-byte integers — for example, problems whose leading dimensions or array indices don’t fit in a 32-bit signed integer. The LP64 modules bind to the `$NEWLAPACK` symbol suffix; the ILP64 modules bind to the `$NEWLAPACK$ILP64` suffix.

#### Adopt a Wrapper Module in Your Source

Add a `use` statement for the module that matches the API and integer width you need, then call the routine directly. The example below calls `dgemm` from the ILP64 BLAS wrapper:

```fortran
use accelerate_blas_ilp64

integer(8) :: m, n, k, lda, ldb, ldc
! declare alpha, beta, and arrays a, b, c with matching kinds

call dgemm('N', 'N', m, n, k, alpha, a, lda, b, ldb, beta, c, ldc)
```

> ❗ **Important**:  When you use the ILP64 modules, declare every integer that you pass to a wrapped routine — sizes, leading dimensions, pivot arrays, `info` flags — as `integer(8)`. When you use the LP64 modules, the default `integer` kind is the correct width.

LAPACK routines that take a callback, such as the `SELECT` argument to `SGEES`, `DGEES`, `CGEES`, or `ZGEES`, expect a `type(c_funptr)` value. Use `c_funloc` from `iso_c_binding` to obtain a function pointer from a Fortran procedure.

#### Compile and Link Against Accelerate

> **Note**:  The `gfortran` compiler doesn’t ship with Xcode. Install a Fortran 90 (or later) compiler before you build.

Pass the interface module’s source file on the `gfortran` command line ahead of your own source. The command below compiles `example_program.f90` against the ILP64 BLAS wrappers and links the resulting binary to the Accelerate framework:

```bash
gfortran -o example_program \
    $(xcrun -sdk macosx --show-sdk-path)/usr/include/accelerate_blas_ilp64.f90 \
    example_program.f90 \
    -F$(xcrun -sdk macosx --show-sdk-path)/System/Library/Frameworks \
    -framework Accelerate \
    -L$(xcrun -sdk macosx --show-sdk-path)/usr/lib
```

Each argument plays a specific role:

- `-o example_program` names the output binary.
- `$(xcrun -sdk macosx --show-sdk-path)/usr/include/accelerate_blas_ilp64.f90` is the interface module to compile. Substitute one of `accelerate_blas_lp64.f90`, `accelerate_lapack_lp64.f90`, or `accelerate_lapack_ilp64.f90` to select a different API or integer width. If your program uses both BLAS and LAPACK, pass both interface files.
- `example_program.f90` is your Fortran source. It must appear after the interface module so the compiler resolves the `use` statement by the time it reaches your code.
- `-F$(xcrun -sdk macosx --show-sdk-path)/System/Library/Frameworks -framework Accelerate` points the linker at the Accelerate framework in the selected SDK and links it.
- `-L$(xcrun -sdk macosx --show-sdk-path)/usr/lib` adds the SDK’s library directory to the link search path for any standard libraries `gfortran` needs.

The `xcrun -sdk macosx --show-sdk-path` invocation expands to the active macOS SDK on the build machine, so the same command line works across Xcode versions without hard-coded paths.

## Topics

### Related libraries
- [BLAS](blas-library.md)
  Perform common linear algebra operations with Apple’s implementation of the Basic Linear Algebra Subprograms (BLAS).
- [LAPACK/BLAS Functions](lapack-functions.md)
  An updated BLAS interface supporting ILP64 is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/usingthefortran90wrappers)*