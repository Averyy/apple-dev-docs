# vDSP_mmul

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs an out-of-place multiplication of two single-precision real matrices.

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
extern void vDSP_mmul(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __M, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

The following code multiplies the matrices `a` and `b`, and writes the result to matrix `c`:

**Swift**:

```swift
    let m: vDSP_Length = 2
    let n: vDSP_Length = 5
    let p: vDSP_Length = 3
    
    // Create a matrix with `m` rows and `p` columns.
    let a: [Float] = [ 1, 2, 3,
                       4, 5, 6 ]
    
    // Create a matrix with `p` rows and `n` columns.
    let b: [Float] = [ 10, 11, 12, 13, 14,
                       15, 16, 17, 18, 19,
                       20, 21, 22, 23, 24 ]
    
    
    
    // Create a matrix with `m` rows and `n` columns.
    var c = [Float](repeating: 0,
                    count: Int(m * n))
    
    let stride = 1
    
    vDSP_mmul(a, stride,
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

**Objective-C**:

```objc
vDSP_Length m = 2;
vDSP_Length n = 5;
vDSP_Length p = 3;

// Create a matrix with `m` rows and `p` columns.
float a[] = { 1, 2, 3,
              4, 5, 6 };

// Create a matrix with `p` rows and `n` columns.
float b[] = { 10, 11, 12, 13, 14,
              15, 16, 17, 18, 19,
              20, 21, 22, 23, 24 };

// Create a matrix with `m` rows and `n` columns.
float c[10] = {0};

vDSP_Stride stride = 1;

vDSP_mmul(a, stride,
          b, stride,
          c, stride,
          m,
          n,
          p);

// Prints "[100, 106, 112, 118, 124, 235, 250, 265, 280, 295]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g, %g, %g]\n",
       c[0], c[1], c[2], c[3], c[4],
       c[5], c[6], c[7], c[8], c[9]);
```

## Parameters

- `__A`: The `M` x `P` left-hand side input matrix.
- `__IA`: The distance between the elements in the left-hand side input matrix.
- `__B`: The `P` x `N` right-hand side input matrix.
- `__IB`: The distance between the elements in the right-hand side input matrix.
- `__C`: The `M` x `N` output matrix.
- `__IC`: The distance between the elements in the output matrix.
- `__M`: The number of rows in matrices `A` and `C`.
- `__N`: The number of columns in matrices `B` and `C`.
- `__P`: The number of columns in matrix `A` and the number of rows in matrix `B`.

## See Also

### Multiplying real matrices
- [vDSP_mmulD](./vdsp_mmuld.md)
  Performs an out-of-place multiplication of two double-precision real matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_mmul)*