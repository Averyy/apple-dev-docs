# vDSP_vfrac

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Truncates the elements of a single-precision vector to fractions.

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
extern void vDSP_vfrac(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

Performs the following operation:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557732@2x.png)

The “function” truncate(x) is the integer farthest from 0 but not farther than x. Thus, for example, `vDSP_vFrac(-3.25)` produces the result -0.25.

Sets each element of vector `C` to the signed fractional part of the corresponding element of `A`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [-2, -0.5, 0.5, 3]
var c = [Float](repeating: 0, count: a.count)

// Take the fractional part of each element of `a`, truncating toward zero.
vDSP_vfrac(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[0.0, -0.5, 0.5, 0.0]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {-2, -0.5, 0.5, 3};
float c[4];

// Take the fractional part of each element of `a`, truncating toward zero.
vDSP_vfrac(a, 1, c, 1, 4);

// Prints "[0, -0.5, 0.5, 0]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for `A`
- `__C`: Single-precision real output vector
- `__IC`: Stride for `C`
- `__N`: The number of elements to process

## See Also

### Single-Vector Fractional Part Extraction
- [vDSP_vfracD](./vdsp_vfracd.md)
  Truncates the elements of a double-precision vector to fractions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfrac)*