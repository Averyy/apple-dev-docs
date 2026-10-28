# vDSP_mvessqD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the mean of signed squares of a double-precision vector.

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
extern void vDSP_mvessqD(const double *__A, vDSP_Stride __IA, double *__C, vDSP_Length __N);
```

## Discussion

This function calculates the mean of squares of the first `N` elements of the input vector and writes the result to the output scalar parameter, `C`.

The following code shows an example of using [`vDSP_mvessqD`](./vdsp_mvessqd.md):

**Swift**:

```swift
    let stride = vDSP_Stride(1)
    
    let a: [Double] = [-8, -4, -2, 0, 2, 4, 8]
    let n = vDSP_Length(a.count)
    
    var c = Double()
    
    vDSP_mvessqD(a,
                 stride,
                 &c,
                 n)
    
    print(c) // Prints "0.0".
```

**Objective-C**:

```objc
vDSP_Stride stride = 1;

double a[] = {-8, -4, -2, 0, 2, 4, 8};
vDSP_Length n = 7;

double c = 0;

vDSP_mvessqD(a,
             stride,
             &c,
             n);

// Prints "0".
printf("%g\n", c);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for `A.`
- `__C`: Output scalar.
- `__N`: The number of elements to process. If `N` is zero (`0`), this function returns `-INFINITY`.

## See Also

### Calculating the mean of squares of a vector
- [vDSP_measqv](./vdsp_measqv.md)
  Calculates the mean of squares of a single-precision vector.
- [vDSP_measqvD](./vdsp_measqvd.md)
  Calculates the mean of squares of a double-precision vector.
- [vDSP_mvessq](./vdsp_mvessq.md)
  Calculates the mean of signed squares of a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_mvessqd)*