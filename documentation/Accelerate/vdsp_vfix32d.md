# vDSP_vfix32D

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts a vector of double-precision floating-point values to signed 32-bit integer values, and rounds towards zero.

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
extern void vDSP_vfix32D(const double *__A, vDSP_Stride __IA, int *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_vfix16`](../kernel/api-1532172-vdsp_vfix16.md), except for the type of vector `A`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [1.4, 2.6, -1.6, 3.5]
var c = [Int32](repeating: 0, count: a.count)

// Convert each double-precision element of `a` to a 32-bit integer, truncating toward zero.
vDSP_vfix32D(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1, 2, -1, 3]".
print(c)
```

**Objective-C**:

```objc
double a[4] = {1.4, 2.6, -1.6, 3.5};
int c[4];

// Convert each double-precision element of `a` to a 32-bit integer, truncating toward zero.
vDSP_vfix32D(a, 1, c, 1, 4);

// Prints "[1, 2, -1, 3]".
printf("[%d, %d, %d, %d]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Floating point to 32-bit integer conversion
- [vDSP_vfixr32D](./vdsp_vfixr32d.md)
  Converts a vector of double-precision floating-point values to signed 32-bit integer values, and rounds towards the nearest integer.
- [vDSP_vfixu32D](./vdsp_vfixu32d.md)
  Converts a vector of double-precision floating-point values to unsigned 32-bit integer values, and rounds towards zero.
- [vDSP_vfixru32D](./vdsp_vfixru32d.md)
  Converts a vector of double-precision floating-point values to unsigned 32-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfix32d)*