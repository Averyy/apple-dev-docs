# vDSP_vfixr8D

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts a vector of double-precision floating-point values to signed 8-bit integer values, and rounds towards the nearest integer.

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
extern void vDSP_vfixr8D(const double *__A, vDSP_Stride __IA, char *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [1.4, 2.6, -1.6, 3.5]
var c = [CChar](repeating: 0, count: a.count)

// Convert each double-precision element of `a` to an 8-bit integer, rounding to nearest.
vDSP_vfixr8D(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1, 3, -2, 4]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {1.4, 2.6, -1.6, 3.5};
char c[4];

// Convert each double-precision element of `a` to an 8-bit integer, rounding to nearest.
vDSP_vfixr8D(a, 1, c, 1, 4);

// Prints "[1, 3, -2, 4]".
printf("[%d, %d, %d, %d]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Floating point to 8-bit integer conversion
- [vDSP_vfix8D](./vdsp_vfix8d.md)
  Converts a vector of double-precision floating-point values to signed 8-bit integer values, and rounds towards zero.
- [vDSP_vfixu8D](./vdsp_vfixu8d.md)
  Converts a vector of double-precision floating-point values to unsigned 8-bit integer values, and rounds towards zero.
- [vDSP_vfixru8D](./vdsp_vfixru8d.md)
  Converts a vector of double-precision floating-point values to unsigned 8-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfixr8d)*