# vDSP_vfixr16

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts a vector of single-precision floating-point values to signed 16-bit integer values, and rounds towards the nearest integer.

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
extern void vDSP_vfixr16(const float *__A, vDSP_Stride __IA, short *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [1.4, 2.6, -1.6, 3.5]
var c = [Int16](repeating: 0, count: a.count)

// Convert each single-precision element of `a` to a 16-bit integer, rounding to nearest.
vDSP_vfixr16(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1, 3, -2, 4]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {1.4, 2.6, -1.6, 3.5};
short c[4];

// Convert each single-precision element of `a` to a 16-bit integer, rounding to nearest.
vDSP_vfixr16(a, 1, c, 1, 4);

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

### Floating point to 16-bit integer conversion
- [vDSP_vfix16](./vdsp_vfix16.md)
  Converts a vector of single-precision floating-point values to signed 16-bit integer values, and rounds towards zero.
- [vDSP_vfixu16](./vdsp_vfixu16.md)
  Converts a vector of single-precision floating-point values to unsigned 16-bit integer values, and rounds towards zero.
- [vDSP_vfixru16](./vdsp_vfixru16.md)
  Converts a vector of single-precision floating-point values to unsigned 16-bit integer values, and rounds towards the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfixr16)*