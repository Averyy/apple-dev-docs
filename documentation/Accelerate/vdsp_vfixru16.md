# vDSP_vfixru16

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts a vector of single-precision floating-point values to unsigned 16-bit integer values, and rounds towards the nearest integer.

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
extern void vDSP_vfixru16(const float *__A, vDSP_Stride __IA, unsigned short *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [1.4, 2.6, 3.5, 7.9]
var c = [UInt16](repeating: 0, count: a.count)

// Convert each single-precision element of `a` to an unsigned 16-bit integer, rounding to nearest.
vDSP_vfixru16(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1, 3, 4, 8]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {1.4, 2.6, 3.5, 7.9};
unsigned short c[4];

// Convert each single-precision element of `a` to an unsigned 16-bit integer, rounding to nearest.
vDSP_vfixru16(a, 1, c, 1, 4);

// Prints "[1, 3, 4, 8]".
printf("[%u, %u, %u, %u]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Floating point to 16-bit integer conversion
- [vDSP_vfix16](./vdsp_vfix16.md)
  Converts a vector of single-precision floating-point values to signed 16-bit integer values, and rounds towards zero.
- [vDSP_vfixr16](./vdsp_vfixr16.md)
  Converts a vector of single-precision floating-point values to signed 16-bit integer values, and rounds towards the nearest integer.
- [vDSP_vfixu16](./vdsp_vfixu16.md)
  Converts a vector of single-precision floating-point values to unsigned 16-bit integer values, and rounds towards zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfixru16)*