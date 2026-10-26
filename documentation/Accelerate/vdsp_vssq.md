# vDSP_vssq

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Computes the signed squared value of each element in the supplied single-precision vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_vssq(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This performs the following operation:

![mathematical formula](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-2557726@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [-2, -0.5, 0.5, 3]
var c = [Float](repeating: 0, count: a.count)

// Signed-square each element of `a`, preserving the sign of the input.
vDSP_vssq(a, 1, &c, 1, vDSP_Length(a.count))

// Prints "[-4.0, -0.25, 0.25, 9.0]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {-2, -0.5, 0.5, 3};
float c[4];

// Signed-square each element of `a`, preserving the sign of the input.
vDSP_vssq(a, 1, c, 1, 4);

// Prints "[-4, -0.25, 0.25, 9]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for `A`.
- `__C`: Single-precision real output vector.
- `__IC`: Address stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Single-Vector Squaring
- [vDSP_vsq](./vdsp_vsq.md)
  Computes the squared value of each element in the supplied single-precision vector.
- [vDSP_vsqD](./vdsp_vsqd.md)
  Computes the squared value of each element in the supplied double-precision vector.
- [vDSP_vssqD](./vdsp_vssqd.md)
  Computes the signed squared value of each element in the supplied double-precision vector.
- [vDSP_zvmags](./vdsp_zvmags.md)
  Computes the squared magnitude value of each element in the supplied complex single-precision vector.
- [vDSP_zvmagsD](./vdsp_zvmagsd.md)
  Computes the squared magnitude value of each element in the supplied complex double-precision vector.
- [vDSP_zvmgsa](./vdsp_zvmgsa.md)
  Complex vector magnitudes square and add; single precision.
- [vDSP_zvmgsaD](./vdsp_zvmgsad.md)
  Complex vector magnitudes square and add; double precision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vssq)*