# vDSP_vdpsp

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts a double-precision vector to a single-precision vector.

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
extern void vDSP_vdpsp(const double *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [1.5, 2.5, 3.5]
var c = [Float](repeating: 0, count: a.count)

// Convert each double-precision element of `a` to single precision.
vDSP_vdpsp(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1.5, 2.5, 3.5]".
print(c)
```

**Objective-C**:

```objc
double a[3] = {1.5, 2.5, 3.5};
float c[3];

// Convert each double-precision element of `a` to single precision.
vDSP_vdpsp(a, 1, c, 1, 3);

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
- [vDSP_vspdp](./vdsp_vspdp.md)
  Converts a single-precision vector to a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vdpsp)*