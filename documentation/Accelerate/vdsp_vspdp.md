# vDSP_vspdp

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts a single-precision vector to a double-precision vector.

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
extern void vDSP_vspdp(const float *__A, vDSP_Stride __IA, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [1.5, 2.5, 3.5]
var c = [Double](repeating: 0, count: a.count)

// Convert each single-precision element of `a` to double precision.
vDSP_vspdp(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1.5, 2.5, 3.5]".
print(c)
```

**Objective-C**:

```objc
float a[3] = {1.5, 2.5, 3.5};
double c[3];

// Convert each single-precision element of `a` to double precision.
vDSP_vspdp(a, 1, c, 1, 3);

// Prints "[1.5, 2.5, 3.5]".
printf("[%g, %g, %g]\n", c[0], c[1], c[2]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Conversion between floating-point types
- [vDSP_vdpsp](./vdsp_vdpsp.md)
  Converts a double-precision vector to a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vspdp)*