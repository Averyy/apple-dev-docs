# vDSP_meamgv

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the mean of magnitudes of a single-precision vector.

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
extern void vDSP_meamgv(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Length __N);
```

## Discussion

This function calculates the mean of magnitudes of the first `N` elements of the input vector and writes the result to the output scalar parameter, `C`.

The following code shows an example of using [`vDSP_meamgv`](./vdsp_meamgv.md):

**Swift**:

```swift
    let stride = vDSP_Stride(1)

    let a: [Float] = [-8, -4, -2, 0, 2, 4, 8]
    let n = vDSP_Length(a.count)

    var c = Float()

    vDSP_meamgv(a,
               stride,
               &c,
               n)

    print(c) // Prints "4.0".
```

**Objective-C**:

```objc
float a[] = {-8.0f, -4.0f, -2.0f, 0.0f, 2.0f, 4.0f, 8.0f};
vDSP_Stride stride = 1;
vDSP_Length n = 7;

float c = 0.0f;

vDSP_meamgv(a, stride, &c, n);

// Prints "4".
printf("%g\n", c);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: On output, the mean of magnitudes of the elements in the input vector.
- `__N`: The number of elements that the function processes.

## See Also

### Calculating the mean of magnitudes of a vector
- [vDSP_meamgvD](./vdsp_meamgvd.md)
  Calculates the mean of magnitudes of a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_meamgv)*