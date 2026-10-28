# vDSP_vthr

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates single-precision vector threshold to the specified range.

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
extern void vDSP_vthr(const float *__A, vDSP_Stride __IA, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

Performs the following operation:

```objc
for (n = 0; n < N; ++n){
    if (A[n*IA] >= *B)
        C[n*IC] = A[n*IA];
    else
        C[n*IC] = *B;
}
```

Creates vector `C` by comparing each input from vector `A` with scalar `*B`. If  an input value is less than `*B`, `*B` is copied to `C`; otherwise, the input value from `A` is  copied to `C`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [-2, -0.5, 0.5, 3]
var threshold: Float = -1
var c = [Float](repeating: 0, count: a.count)

// Clamp each element of `a` up to the lower `threshold`.
vDSP_vthr(a, 1, &threshold, &c, 1, vDSP_Length(a.count))

// Prints "[-1.0, -0.5, 0.5, 3.0]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {-2, -0.5, 0.5, 3};
float threshold = -1;
float c[4];

// Clamp each element of `a` up to the lower `threshold`.
vDSP_vthr(a, 1, &threshold, c, 1, 4);

// Prints "[-1, -0.5, 0.5, 3]".
printf("[%g, %g, %g, %g]\n", c[0], c[1], c[2], c[3]);
```

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for `A`
- `__B`: Pointer to single-precision real input scalar: lower threshold
- `__C`: Single-precision real output vector
- `__IC`: Stride for `C`
- `__N`: The number of elements to process

## See Also

### Clipping Operations
- [vDSP_vclip](./vdsp_vclip.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipD](./vdsp_vclipd.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [vDSP_vclipc](./vdsp_vclipc.md)
  Calculates and counts the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipcD](./vdsp_vclipcd.md)
  Calculates and counts the elements of a double-precision vector clipped to the specified range.
- [vDSP_viclip](./vdsp_viclip.md)
  Calculates the elements of a single-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_viclipD](./vdsp_viclipd.md)
  Calculates the elements of a double-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_vthrD](./vdsp_vthrd.md)
  Calculates double-precision vector threshold to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vthr)*