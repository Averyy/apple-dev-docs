# vDSP_maxmgvD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision maximum magnitude of a vector.

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
extern void vDSP_maxmgvD(const double *__A, vDSP_Stride __IA, double *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the maximum magnitude of the first `N` elements of input vector `A`, and writes the result to output scalar `C`.

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector, A, with three boxes. The middle row represents the operation a boxes that contains the absolute-maximum function. The bottom row represents the output scalar value C as a  box. The diagram has connecting lines from the input vector to the operation, and from the operation to the output scalar value.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4465876@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
    let stride = vDSP_Stride(1)
    
    let a: [Double] = [-1.5, 2.25, 3.6,
                        0.2, -0.1, -4.3]
    let n = vDSP_Length(a.count)
    
    var c = Double()
    
    vDSP_maxmgvD(a,
                 stride,
                 &c,
                 n)
    
    print("max magnitude", c) // Prints "max magnitude 4.3".
```

**Objective-C**:

```objc
vDSP_Stride stride = 1;
double a[6] = {-1.5, 2.25, 3.6, 0.2, -0.1, -4.3};
vDSP_Length n = 6;
double c = 0;

vDSP_maxmgvD(a, stride, &c, n);

// Prints "max magnitude 4.3".
printf("max magnitude %g\n", c);
```

## Parameters

- `__A`: The input vector, `A`.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output scalar value, `C`. If `N` is zero, the function sets `C` to `0`.
- `__N`: The number of elements that the function processes.

## See Also

### Calculating the maximum value of a vector
- [vDSP_maxv](./vdsp_maxv.md)
  Calculates the single-precision maximum value of a vector.
- [vDSP_maxvD](./vdsp_maxvd.md)
  Calculates the double-precision maximum value of a vector.
- [vDSP_maxmgv](./vdsp_maxmgv.md)
  Calculates the single-precision maximum magnitude of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_maxmgvd)*