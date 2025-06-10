# vDSP_wienerD

**Framework**: Accelerate  
**Kind**: func

Solves a system of linear equations for a double-precision symmetric Toeplitz coefficient matrix.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_wienerD(vDSP_Length __L, const double * __A, const double * __C, double * __F, double * __P, int __Flag, int * __Error);
```

#### Discussion

Use this function to solve a system of simultaneous equations where the coefficient matrix is a symmetric Toeplitz matrix. A symmetric matrix is one that’s equal to its transpose, that is, a matrix that’s identical when swapping its row and column indices. A Toeplitz matrix is a matrix where each diagonal is constant.

The example below shows a matrix equation where the coefficient matrix is a symmetric Toeplitz matrix:

![A mathematical formula that describes a matrix equation. A four-by-four matrix is multiplied by the four-element vector, f, equals a four-element matrix. The vector f contains unknown values.](https://docs-assets.developer.apple.com/published/fca17823d6f2acf7f9fb11682abb3800/media-3855534%402x.png)

This function solves the equation and finds the values for the output vector, `__F`.

![A mathematical formula that describes a matrix equation. A four-by-four matrix is multiplied by the four-element vector, f, equals a four-element matrix. The vector f contains known values.](https://docs-assets.developer.apple.com/published/ced19e4f17693d7d3cea92b8377b470d/media-3855533%402x.png)

Because the 4 x 4 coefficient matrix is symmetric, it contains four diagonal bands that you define using a four-element vector. The following code shows how to solve a system of linear equations using [`vDSP_wiener`](vdsp_wiener.md):

```swift
// The `coefficientMatrix` array contains the diagonal values of
// the symmetric Toeplitz coefficient matrix `a` in `a · f = c`.
let coefficientMatrix: [Double] = [15, 60, 3, 9]

// The `constants` array contains the RHS `c` in `a · f = c`.
let constants: [Double] = [360, 564, 816, 510]

var performanceIndex = [Double](repeating: 0,
                                count: constants.count)
var error = Int32(0)

// On return, `result` contains the solution `f` in `a · f = c`.
let result = [Double](unsafeUninitializedCapacity: constants.count) {
    buffer, count in
    
    vDSP_wienerD(vDSP_Length(constants.count),
                coefficientMatrix,
                constants,
                buffer.baseAddress!,
                &performanceIndex, 0,
                &error)
    
    count = constants.count
}

guard error == 0 else {
    fatalError("Solve failed at pass \(error).")
}

// Prints `[1.9999999999999964, 3.9999999999999885,
//          6.0000000000000036, 8.000000000000002] ≈ [2, 4, 6, 8]`
print(result)
```

Note that this function only works out-of-place.

Typical methods for solving  equations in  unknowns have execution times proportional to _N_3, and memory requirements proportional to _N_2. By taking advantage of duplicate elements, the recursion method implemented by [`vDSP_wiener`](vdsp_wiener.md) executes in a time proportional to _N_2 and requires memory proportional to . The Wiener-Levinson algorithm recursively builds a solution by computing the  matrix solution from the  matrix solution.

You can use the solution, , as a Wiener filter.

## Parameters

- `__L`: The number of elements in the output vector.
- `__A`: The diagonal values of the coefficient matrix. If you’re using this function to generate a Wiener filter, pass the autocorrelation of a given signal.
- `__C`: The values of the RHS vector. If you’re using this function to generate a Wiener filter, pass the cross-correlation of signal and observation.
- `__F`: The output vector.
- `__P`: The performance index that’s a measure of the error for each component of the signal.
- `__Flag`: Not currently used, pass zero.
- `__Error`: The error flag. In the case of an error, the function populates the error flag with the pass in which the failure occurred.

## See Also

- [vDSP_wiener](vdsp_wiener.md)
  Solves a system of linear equations for a single-precision symmetric Toeplitz coefficient matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_wienerd)*