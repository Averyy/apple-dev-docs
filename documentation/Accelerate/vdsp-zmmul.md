# vDSP_zmmul

**Framework**: Accelerate  
**Kind**: func

Performs an out-of-place multiplication of two single-precision complex matrices.

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
extern void vDSP_zmmul(const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __B, vDSP_Stride __IB, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __M, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

The following code multiplies the matrices `a` and `b`, and writes the result to matrix `c`:

```swift
    //                        [ 4+5i,
    // [ 1+2i, 2+3i, 3+4i ] *   5+6i,  = [ -24+85i ]
    //                          6+7i ]
    
    let m: vDSP_Length = 1
    let n: vDSP_Length = 1
    let p: vDSP_Length = 3
    
    // `m` rows x `p` columns.
    let aReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * p))
    _ = aReal.initialize(from: [1, 2, 3])
    
    let aImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * p))
    _ = aImag.initialize(from: [2, 3, 4])
    
    var a = DSPSplitComplex(realp: aReal.baseAddress!, imagp: aImag.baseAddress!)
    
    // `p` rows x `n` columns.
    let bReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(p * n))
    _ = bReal.initialize(from: [4, 5, 6])
    
    let bImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(p * n))
    _ = bImag.initialize(from: [5, 6, 7])
    
    var b = DSPSplitComplex(realp: bReal.baseAddress!, imagp: bImag.baseAddress!)
    
    // `m` rows x `n` columns.
    let cReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * n))
    let cImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: Int(m * n))
    
    var c = DSPSplitComplex(realp: cReal.baseAddress!, imagp: cImag.baseAddress!)
    
    vDSP_zmmul(&a, 1,
               &b, 1,
               &c, 1,
               m, n, p)
    
    print(Array(cReal)) // Prints "[-24.0]".
    print(Array(cImag)) // Prints "[85.0]".
```

## Parameters

- `__A`: The   x   left-hand side input matrix.
- `__IA`: The distance between the elements in the left-hand side input matrix.
- `__B`: The   x   right-hand side input matrix.
- `__IB`: The distance between the elements in the right-hand side input matrix.
- `__C`: The   x   output matrix.
- `__IC`: The distance between the elements in the output matrix.
- `__M`: The number of rows in matrices   and  .
- `__N`: The number of columns in matrices   and  .
- `__P`: The number of columns in matrix   and the number of rows in matrix  .

## See Also

- [vDSP_zmmulD](vdsp_zmmuld.md)
  Performs an out-of-place multiplication of two double-precision complex matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zmmul)*