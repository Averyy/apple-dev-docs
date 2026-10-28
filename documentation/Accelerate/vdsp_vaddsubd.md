# vDSP_vaddsubD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision element-wise sum and subtraction of two vectors, using the specified stride.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
void vDSP_vaddsubD(const double *__I0, vDSP_Stride __I0S, const double *__I1, vDSP_Stride __I1S, double *__O0, vDSP_Stride __O0S, double *__O1, vDSP_Stride __O1S, vDSP_Length __N);
```

## Discussion

This function calculates the addition and subtraction of the first `N` elements of input vectors `A` and `B`, and writes the result to output vector `C`, as follows:

```c
 for (i = 0; i < N; ++i)
 {
     i1 = I1[i*I1S];
     i0 = I0[i*I0S];
     O0[i*O0S] = i1 + i0;
     O1[i*O1S] = i1 - i0;
 }
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vectors, A and B, with three boxes of each. The middle row represents the operation, addition and subtraction, with three boxes of each. The bottom row represents the output vectors, O0 and O1, as three boxes of each. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4336938@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
    let stride = 1
    let count = 5
    
    let b: [Double] = [10, 20, 30, 40, 50]
    let a: [Double] = [ 1,  2,  3,  4,  5]
    
    var o0 = [Double](repeating: 0, count: count)
    var o1 = [Double](repeating: 0, count: count)
    
    vDSP_vaddsubD(a, stride,
                  b, stride,
                  &o0, stride,
                  &o1, stride,
                  vDSP_Length(count))
    
    // Prints the addition result: "[11.0, 22.0, 33.0, 44.0, 55.0]".
    print(o0)
    
    // Prints the subtraction result: "[9.0, 18.0, 27.0, 36.0, 45.0]".
    print(o1)
```

**Objective-C**:

```objc
    vDSP_Stride stride = 1;
    vDSP_Length count = 5;

    double b[] = {10, 20, 30, 40, 50};
    double a[] = { 1,  2,  3,  4,  5};
    double o0[5] = {0, 0, 0, 0, 0};
    double o1[5] = {0, 0, 0, 0, 0};

    vDSP_vaddsubD(a, stride,
                  b, stride,
                  o0, stride,
                  o1, stride,
                  count);

    // Prints the addition result: "[11, 22, 33, 44, 55]".
    printf("[%g, %g, %g, %g, %g]\n", o0[0], o0[1], o0[2], o0[3], o0[4]);

    // Prints the subtraction result: "[9, 18, 27, 36, 45]".
    printf("[%g, %g, %g, %g, %g]\n", o1[0], o1[1], o1[2], o1[3], o1[4]);
```

## Parameters

- `__I0`: The first input vector, `A`.
- `__I0S`: The distance between the elements in the first input vector.
- `__I1`: The second input vector, `B`.
- `__I1S`: The distance between the elements in the second input vector.
- `__O0`: The addition output vector, `O0`.
- `__O0S`: The distance between the elements in the addition output vector.
- `__O1`: The subtraction output vector, `O1`.
- `__O1S`: The distance between the elements in the subtraction output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Binary addition and subtraction operations
- [vDSP_vaddsub](./vdsp_vaddsub.md)
  Calculates the single-precision element-wise sum and subtraction of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vaddsubd)*