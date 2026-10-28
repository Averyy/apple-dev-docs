# vDSP_vadd

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the single-precision element-wise sum of two vectors, using the specified stride.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_vadd(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Mentions

- [Controlling vDSP operations with stride](./controlling-vdsp-operations-with-stride.md)
- [Using vDSP for vector-based arithmetic](./using-vdsp-for-vector-based-arithmetic.md)

## Discussion

This function calculates the sums of the first `N` elements of input vectors `A` and `B`, and writes the result to output vector `C`, as follows:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] + B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vectors, A and B, with three boxes of each. The middle row represents the operation as three boxes with plus signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vectors.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4389091@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
    let stride = 1
    let count = 5

    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: [Float] = [10, 20, 30, 40, 50]

    let c = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vadd(a, stride,
                  b, stride,
                  buffer.baseAddress!, stride,
                  vDSP_Length(count))
        
        initializedCount = count
    }
   
    // Prints "[11.0, 22.0, 33.0, 44.0, 55.0]".
    print(c)
```

**Objective-C**:

```objc
    vDSP_Stride stride = 1;
    vDSP_Length count = 5;

    float a[] = { 1,  2,  3,  4,  5};
    float b[] = {10, 20, 30, 40, 50};
    float c[5];

    vDSP_vadd(a, stride,
              b, stride,
              c, stride,
              count);

    // Prints "[11, 22, 33, 44, 55]".
    printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
```

## Parameters

- `__A`: The first input vector, `A`.
- `__IA`: The distance between the elements in the first input vector.
- `__B`: The second input vector, `B`.
- `__IB`: The distance between the elements in the second input vector.
- `__C`: The output vector, `C`.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Binary addition operations
- [vDSP_vaddD](./vdsp_vaddd.md)
  Calculates the double-precision element-wise sum of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vadd)*