# vDSP_vfixu32

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts a vector of single-precision floating-point values to unsigned 32-bit integer values, and rounds towards zero.

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
extern void vDSP_vfixu32(const float *__A, vDSP_Stride __IA, unsigned int *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

If the resulting value is outside the bounds of the output type, the behavior is undefined. If you need to handle out-of-bounds data, you should use one of the functions in Clipping Operations on the data first.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [1.4, 2.6, 3.5, 7.9]
var c = [UInt32](repeating: 0, count: a.count)

// Convert each single-precision element of `a` to an unsigned 32-bit integer, truncating toward zero.
vDSP_vfixu32(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1, 2, 3, 7]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {1.4, 2.6, 3.5, 7.9};
unsigned int c[4];

// Convert each single-precision element of `a` to an unsigned 32-bit integer, truncating toward zero.
vDSP_vfixu32(a, 1, c, 1, 4);

// Prints "[1, 2, 3, 7]".
printf("[%u, %u, %u, %u]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Floating point to 32-bit integer conversion
- [vDSP_vfix32](./vdsp_vfix32.md)
  Converts a vector of single-precision floating-point values to signed 32-bit integer values, and rounds towards zero.
- [vDSP_vfixr32](./vdsp_vfixr32.md)
  Converts a vector of single-precision floating-point values to signed 32-bit integer values, and rounds towards the nearest integer.
- [vDSP_vfixru32](./vdsp_vfixru32.md)
  Converts a vector of single-precision floating-point values to unsigned 32-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfixu32)*