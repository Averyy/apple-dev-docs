# vDSP_vdivD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision element-wise division of two vectors, using the specified stride.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_vdivD(const double *__B, vDSP_Stride __IB, const double *__A, vDSP_Stride __IA, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function calculates the division of the first `N` elements of input vectors `A` and `B`, and writes the result to output vector `C`, as follows:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vectors, A and B, with three boxes of each. The middle row represents the operation as three boxes with division signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vectors.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4336935@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
    let stride = 1
    let count = 5
    
    let a: [Double] = [10, 20, 30, 40, 50]
    let b: [Double] = [ 1,  2,  3,  4,  5]
    
    let c = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vdivD(b, stride,
                   a, stride,
                   buffer.baseAddress!, stride,
                   vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Operand-order trap: `vDSP_vdivD` divides the second input by the first, so passing `(B, A)` computes `C = A / B`.
    // Prints "[10.0, 10.0, 10.0, 10.0, 10.0]".
    print(c)
```

**Objective-C**:

```objc
    vDSP_Stride stride = 1;
    vDSP_Length count = 5;

    double a[5] = {10, 20, 30, 40, 50};
    double b[5] = {1, 2, 3, 4, 5};

    double c[5] = {0};

    vDSP_vdivD(b, stride,
               a, stride,
               c, stride,
               count);

    // Operand-order trap: `vDSP_vdivD` divides the second input by the first, so passing `(B, A)` computes `C = A / B`.
    // Prints "[10, 10, 10, 10, 10]".
    printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
```

## Parameters

- `__B`: The first input vector, `B`.
- `__IB`: The distance between the elements in the first input vector.
- `__A`: The second input vector, `A`.
- `__IA`: The distance between the elements in the second input vector.
- `__C`: The output vector, `C`.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Binary division operations
- [vDSP_vdiv](./vdsp_vdiv.md)
  Calculates the single-precision element-wise division of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vdivd)*