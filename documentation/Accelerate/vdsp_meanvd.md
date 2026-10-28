# vDSP_meanvD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the mean value of a double-precision vector.

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
extern void vDSP_meanvD(const double *__A, vDSP_Stride __IA, double *__C, vDSP_Length __N);
```

## Discussion

This function calculates the mean value of the first `N` elements of the input vector and writes the result to the output scalar parameter, `C`.

The following code shows an example of using [`vDSP_meanvD`](./vdsp_meanvd.md):

**Swift**:

```swift
   let stride = vDSP_Stride(1)

    let a: [Double] = [-8, -4, -2, 0, 2, 4, 8]
    let n = vDSP_Length(a.count)

    var c = Double()

    vDSP_meanvD(a,
               stride,
               &c,
               n)

    print(c) // Prints "0.0".
```

**Objective-C**:

```objc
double a[] = {-8.0, -4.0, -2.0, 0.0, 2.0, 4.0, 8.0};
vDSP_Stride stride = 1;
vDSP_Length n = 7;

double c = 0.0;

vDSP_meanvD(a, stride, &c, n);

// Prints "0".
printf("%g\n", c);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: On output, the mean value of the elements in the input vector.
- `__N`: The number of elements that the function processes.

## See Also

### Calculating the mean value of a vector
- [vDSP_meanv](./vdsp_meanv.md)
  Calculates the mean value of a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_meanvd)*