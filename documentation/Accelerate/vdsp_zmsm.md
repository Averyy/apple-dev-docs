# vDSP_zmsm

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Subtracts the product of two single-precision complex matrices from a single-precision complex matrix.

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
extern void vDSP_zmsm(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__B, vDSP_Stride __IB, const DSPSplitComplex *__C, vDSP_Stride __IC, const DSPSplitComplex *__D, vDSP_Stride __ID, vDSP_Length __M, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

The following code subtracts the product of matrices `a` and `b from` the matrix `c`, and writes the result to matrix `d`:

**Swift**:

```swift
// Compute the following:
//                                   [ 4+5i,
// [ 4+5i ] - [ 1+2i, 2+3i, 3+4i ] *   5+6i,  = [ 28-80i ]
//                                     6+7i ]

let m: vDSP_Length = 1
let n: vDSP_Length = 1
let p: vDSP_Length = 3

// Create a matrix with `m` rows and `p` columns.
let aReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * p))
_ = aReal.initialize(from: [1, 2, 3])

let aImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * p))
_ = aImag.initialize(from: [2, 3, 4])

var a = DSPSplitComplex(realp: aReal.baseAddress!,
                        imagp: aImag.baseAddress!)

// Create a matrix with `p` rows and `n` columns.
let bReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(p * n))
_ = bReal.initialize(from: [4, 5, 6])

let bImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(p * n))
_ = bImag.initialize(from: [5, 6, 7])

var b = DSPSplitComplex(realp: bReal.baseAddress!,
                        imagp: bImag.baseAddress!)

// Create a matrix with `m` rows and `n` columns.
let cReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * n))
_ = cReal.initialize(from: [4])

let cImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * n))
_ = cImag.initialize(from: [5])

var c = DSPSplitComplex(realp: cReal.baseAddress!,
                        imagp: cImag.baseAddress!)

// Create a matrix with `m` rows and `n` columns.
let dReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * n))
let dImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * n))

var d = DSPSplitComplex(realp: dReal.baseAddress!,
                        imagp: dImag.baseAddress!)

vDSP_zmsm(&a, 1,
          &b, 1,
          &c, 1,
          &d, 1,
          m, n, p)

print(Array(dReal)) // Prints "[28.0]".
print(Array(dImag)) // Prints "[-80.0]".
```

**Objective-C**:

```objc
// Compute the following:
//                                   [ 4+5i,
// [ 4+5i ] - [ 1+2i, 2+3i, 3+4i ] *   5+6i,  = [ 28-80i ]
//                                     6+7i ]
vDSP_Length m = 1, n = 1, p = 3;

// Create a matrix with `m` rows and `p` columns.
float aRealp[3] = {1, 2, 3};
float aImagp[3] = {2, 3, 4};
DSPSplitComplex a = { .realp = aRealp, .imagp = aImagp };

// Create a matrix with `p` rows and `n` columns.
float bRealp[3] = {4, 5, 6};
float bImagp[3] = {5, 6, 7};
DSPSplitComplex b = { .realp = bRealp, .imagp = bImagp };

// Create a matrix with `m` rows and `n` columns.
float cRealp[1] = {4};
float cImagp[1] = {5};
DSPSplitComplex c = { .realp = cRealp, .imagp = cImagp };

// Create a matrix with `m` rows and `n` columns.
float dRealp[1];
float dImagp[1];
DSPSplitComplex d = { .realp = dRealp, .imagp = dImagp };

vDSP_zmsm(&a, 1, &b, 1, &c, 1, &d, 1, m, n, p);

// Prints "realp [28], imagp [-80]".
printf("realp [%g]\n", dRealp[0]);
printf("imagp [%g]\n", dImagp[0]);
```

## Parameters

- `__A`: The single-precision complex `M` x `P` input matrix `a` in `d = c - (a * b)`.
- `__IA`: The distance between the elements in the matrix `A`.
- `__B`: The single-precision complex `P` x `N` input matrix `b` in `d = c - (a * b)`.
- `__IB`: The distance between the elements in the matrix `B`.
- `__C`: The single-precision complex `M` x `N` input matrix `c` in `d = c - (a * b)`.
- `__IC`: The distance between the elements in the matrix `C`.
- `__D`: The single-precision complex `M` x `N` output matrix `d` in `d = c - (a * b)`.
- `__ID`: The distance between the elements in the matrix `D`.
- `__M`: The number of rows in matrices `A`, `C`, and `D`.
- `__N`: The number of columns in matrix `B`, `C`, and `D`.
- `__P`: The number of columns in matrix `A` and the number of rows in matrix `B`.

## See Also

### Multiplying and subtracting complex matrices
- [vDSP_zmms](./vdsp_zmms.md)
  Subtracts a single-precision complex matrix from the product of two single-precision complex matrices.
- [vDSP_zmmsD](./vdsp_zmmsd.md)
  Subtracts a double-precision complex matrix from the product of two double-precision complex matrices.
- [vDSP_zmsmD](./vdsp_zmsmd.md)
  Subtracts the product of two double-precision complex matrices from a double-precision complex matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zmsm)*