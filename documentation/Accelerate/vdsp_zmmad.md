# vDSP_zmmaD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Adds a double-precision complex matrix to the product of two double-precision complex matrices.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_zmmaD(const DSPDoubleSplitComplex *__A, vDSP_Stride __IA, const DSPDoubleSplitComplex *__B, vDSP_Stride __IB, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC, const DSPDoubleSplitComplex *__D, vDSP_Stride __ID, vDSP_Length __M, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

The following code adds the matrix `c` to the product of matrices `a` and `b`, and writes the result to matrix `d`:

**Swift**:

```swift
// Compute the following:
//                        [ 4+5i,
// [ 1+2i, 2+3i, 3+4i ] *   5+6i,  + [ 4+5i ] = [ -20+90i ]
//                          6+7i ]

let m: vDSP_Length = 1
let n: vDSP_Length = 1
let p: vDSP_Length = 3

// Create a matrix with `m` rows and `p` columns.
let aReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: Int(m * p))
_ = aReal.initialize(from: [1, 2, 3])

let aImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: Int(m * p))
_ = aImag.initialize(from: [2, 3, 4])

var a = DSPDoubleSplitComplex(realp: aReal.baseAddress!,
                              imagp: aImag.baseAddress!)

// Create a matrix with `p` rows and `n` columns.
let bReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: Int(p * n))
_ = bReal.initialize(from: [4, 5, 6])

let bImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: Int(p * n))
_ = bImag.initialize(from: [5, 6, 7])

var b = DSPDoubleSplitComplex(realp: bReal.baseAddress!,
                              imagp: bImag.baseAddress!)

// Create a matrix with `m` rows and `n` columns.
let cReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: Int(m * n))
_ = cReal.initialize(from: [4])

let cImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: Int(m * n))
_ = cImag.initialize(from: [5])

var c = DSPDoubleSplitComplex(realp: cReal.baseAddress!,
                              imagp: cImag.baseAddress!)

// Create a matrix with `m` rows and `n` columns.
let dReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: Int(m * n))
let dImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: Int(m * n))

var d = DSPDoubleSplitComplex(realp: dReal.baseAddress!,
                              imagp: dImag.baseAddress!)

vDSP_zmmaD(&a, 1,
           &b, 1,
           &c, 1,
           &d, 1,
           m, n, p)

print(Array(dReal)) // Prints "[-20.0]".
print(Array(dImag)) // Prints "[90.0]".
```

**Objective-C**:

```objc
// Compute the following:
//                        [ 4+5i,
// [ 1+2i, 2+3i, 3+4i ] *   5+6i,  + [ 4+5i ] = [ -20+90i ]
//                          6+7i ]
vDSP_Length m = 1, n = 1, p = 3;

// Create a matrix with `m` rows and `p` columns.
double aRealp[3] = {1, 2, 3};
double aImagp[3] = {2, 3, 4};
DSPDoubleSplitComplex a = { .realp = aRealp, .imagp = aImagp };

// Create a matrix with `p` rows and `n` columns.
double bRealp[3] = {4, 5, 6};
double bImagp[3] = {5, 6, 7};
DSPDoubleSplitComplex b = { .realp = bRealp, .imagp = bImagp };

// Create a matrix with `m` rows and `n` columns.
double cRealp[1] = {4};
double cImagp[1] = {5};
DSPDoubleSplitComplex c = { .realp = cRealp, .imagp = cImagp };

// Create a matrix with `m` rows and `n` columns.
double dRealp[1];
double dImagp[1];
DSPDoubleSplitComplex d = { .realp = dRealp, .imagp = dImagp };

vDSP_zmmaD(&a, 1, &b, 1, &c, 1, &d, 1, m, n, p);

// Prints "realp [-20], imagp [90]".
printf("realp [%g]\n", dRealp[0]);
printf("imagp [%g]\n", dImagp[0]);
```

## Parameters

- `__A`: The single-precision complex `M` x `P` input matrix `a` in `d = (a * b) + c`.
- `__IA`: The distance between the elements in the matrix `A`.
- `__B`: The single-precision complex `P` x `N` input matrix `b` in `d = (a * b) + c`.
- `__IB`: The distance between the elements in the matrix `B`.
- `__C`: The single-precision complex `M` x `N` input matrix `c` in `d = (a * b) + c`.
- `__IC`: The distance between the elements in the matrix `C`.
- `__D`: The single-precision complex `M` x `N` output matrix `d` in `d = (a * b) + c`.
- `__ID`: The distance between the elements in the matrix `D`.
- `__M`: The number of rows in matrices `A`, `C`, and `D`.
- `__N`: The number of columns in matrix `B`, `C`, and `D`.
- `__P`: The number of columns in matrix `A` and the number of rows in matrix `B`.

## See Also

### Multiplying and adding complex matrices
- [vDSP_zmma](./vdsp_zmma.md)
  Adds a single-precision complex matrix to the product of two single-precision complex matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zmmad)*