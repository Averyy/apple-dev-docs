# vDSP_zmsmD

**Framework**: Accelerate  
**Kind**: func

Subtracts the product of two double-precision complex matrices from a double-precision complex matrix.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zmsmD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __B, vDSP_Stride __IB, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, const DSPDoubleSplitComplex * __D, vDSP_Stride __ID, vDSP_Length __M, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

The following code subtracts the product of matrices `a` and `b from` the matrix `c`, and writes the result to matrix `d`:

```swift
    /// Compute the following:
    /// ```
    ///                                   [ 4+5i,
    /// [ 4+5i ] - [ 1+2i, 2+3i, 3+4i ] *   5+6i,  = [ 28-80i ]
    ///                                     6+7i ]
    /// ```
    
    let m: vDSP_Length = 1
    let n: vDSP_Length = 1
    let p: vDSP_Length = 3
    
    // `m` rows x `p` columns.
    let aReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * p))
    _ = aReal.initialize(from: [1, 2, 3])
    
    let aImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * p))
    _ = aImag.initialize(from: [2, 3, 4])
    
    var a = DSPSplitComplex(realp: aReal.baseAddress!,
                            imagp: aImag.baseAddress!)
    
    // `p` rows x `n` columns.
    let bReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(p * n))
    _ = bReal.initialize(from: [4, 5, 6])
    
    let bImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(p * n))
    _ = bImag.initialize(from: [5, 6, 7])
    
    var b = DSPSplitComplex(realp: bReal.baseAddress!,
                            imagp: bImag.baseAddress!)
    
    // `m` rows x `n` columns.
    let cReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * n))
    _ = cReal.initialize(from: [4])
    
    let cImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * n))
    _ = cImag.initialize(from: [5])
    
    var c = DSPSplitComplex(realp: cReal.baseAddress!,
                            imagp: cImag.baseAddress!)
    
    // `m` rows x `n` columns.
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

## Parameters

- `__A`: The single-precision complex   x   input matrix   in  .
- `__IA`: The distance between the elements in the matrix  .
- `__B`: The single-precision complex   x   input matrix   in  .
- `__IB`: The distance between the elements in the matrix  .
- `__C`: The single-precision complex   x   input matrix   in  .
- `__IC`: The distance between the elements in the matrix  .
- `__D`: The single-precision complex   x   output matrix   in  .
- `__ID`: The distance between the elements in the matrix  .
- `__M`: The number of rows in matrices  ,  , and  .
- `__N`: The number of columns in matrix  ,  , and  .
- `__P`: The number of columns in matrix   and the number of rows in matrix  .

## See Also

- [vDSP_zmms](vdsp_zmms.md)
  Subtracts a single-precision complex matrix from the product of two single-precision complex matrices.
- [vDSP_zmmsD](vdsp_zmmsd.md)
  Subtracts a double-precision complex matrix from the product of two double-precision complex matrices.
- [vDSP_zmsm](vdsp_zmsm.md)
  Subtracts the product of two single-precision complex matrices from a single-precision complex matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zmsmd)*