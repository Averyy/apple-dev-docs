# vDSP_mmulD

**Framework**: Accelerate  
**Kind**: func

Performs an out-of-place multiplication of two double-precision real matrices.

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
extern void vDSP_mmulD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Stride __IC, vDSP_Length __M, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

The following code multiplies the matrices `a` and `b`, and writes the result to matrix `c`:

```swift
    let m: vDSP_Length = 2
    let n: vDSP_Length = 5
    let p: vDSP_Length = 3
    
    // `m` rows x `p` columns.
    let a: [Double] = [ 1, 2, 3,
                        4, 5, 6 ]
    
    // `p` rows x `n` columns.
    let b: [Double] = [ 10, 11, 12, 13, 14,
                       15, 16, 17, 18, 19,
                       20, 21, 22, 23, 24 ]
    

    
    // `m` rows x `n` columns.
    var c = [Double](repeating: 0,
                    count: Int(m * n))
    
    let stride = 1
    
    vDSP_mmulD(a, stride,
              b, stride,
              &c, stride,
              m,
              n,
              p)
    
    // Prints:
    // "[ 100.0, 106.0, 112.0, 118.0, 124.0,
    //    235.0, 250.0, 265.0, 280.0, 295.0 ]".
    print(c)
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

- [vDSP_mmul](vdsp_mmul.md)
  Performs an out-of-place multiplication of two single-precision real matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_mmuld)*