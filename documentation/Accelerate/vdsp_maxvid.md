# vDSP_maxviD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the maximum value and corresponding index in a double-precision vector.

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
extern void vDSP_maxviD(const double *__A, vDSP_Stride __IA, double *__C, vDSP_Length *__I, vDSP_Length __N);
```

## Discussion

This function calculates the maximum value and its corresponding index of the first `N` elements of the input vector and writes the results to the output scalar parameters, `C` and `I`, respectively.

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector, A, with three boxes. The middle row represents the operation as two boxes that contains maximum and argmax functions. The bottom row represents the output scalar values C and I as two  boxes. The diagram has connecting lines from the input vector to the operations, and from the operations to the output scalar values.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4465880@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
    let stride = vDSP_Stride(1)
    
    let a: [Double] = [-1.5, 2.25, 3.6,
                        0.2, -0.1, -4.3]
    let n = vDSP_Length(a.count)
    
    var c: Double = .nan
    var i: vDSP_Length = 0
    
    vDSP_maxviD(a,
                stride,
                &c,
                &i,
                n)
    
    print("max", c,
          "index", i) // Prints "max 3.6 index 2".
```

**Objective-C**:

```objc
double a[] = {-1.5, 2.25, 3.6, 0.2, -0.1, -4.3};
vDSP_Stride stride = 1;
vDSP_Length n = 6;

double c = NAN;
vDSP_Length i = 0;

vDSP_maxviD(a, stride, &c, &i, n);

// Prints "max 3.6 index 2".
printf("max %g index %lu\n", c, (unsigned long)i);
```

## Parameters

- `__A`: The input vector, `A`.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output scalar value, `C`. If `N` is zero, the function sets `C` to -`infinity`.
- `__I`: The output scalar value, `I`. If `N` is zero, the function sets `I` to `0`.
- `__N`: The number of elements that the function processes.

## See Also

### Calculating the index of the maximum value of a vector
- [vDSP_maxvi](./vdsp_maxvi.md)
  Calculates the maximum value and corresponding index in a single-precision vector.
- [vDSP_maxmgvi](./vdsp_maxmgvi.md)
  Calculates the maximum magnitude and corresponding index in a single-precision vector.
- [vDSP_maxmgviD](./vdsp_maxmgvid.md)
  Calculates the maximum magnitude and corresponding index in a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_maxvid)*