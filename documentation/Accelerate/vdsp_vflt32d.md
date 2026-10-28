# vDSP_vflt32D

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts a vector of signed 32-bit integers to double-precision floating-point values.

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
extern void vDSP_vflt32D(const int *__A, vDSP_Stride __IA, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Int32] = [1, 2, 3, 4]
var c = [Double](repeating: 0, count: a.count)

// Convert each element of the integer vector `a` to double-precision floating point.
vDSP_vflt32D(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[1.0, 2.0, 3.0, 4.0]".
print(c)
```

**Objective-C**:

```objc
int a[4] = {1, 2, 3, 4};
double c[4];

// Convert each element of the integer vector `a` to double-precision floating point.
vDSP_vflt32D(a, 1, c, 1, 4);

// Prints "[1, 2, 3, 4]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### 32-bit integer to floating point conversion
- [vDSP_vfltu32D](./vdsp_vfltu32d.md)
  Converts an array of unsigned 32-bit integers to double-precision floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vflt32d)*