# vDSP_viclip

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the elements of a single-precision vector inverted-clipped to the specified range using the specified stride.

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
extern void vDSP_viclip(const float *__A, vDSP_Stride __IA, const float *__B, const float *__C, float *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

Performs the following operation:

```objc
for (int n = 0; n < N; ++n) {
    if (A[nIA] <= *B || A[nIA] >= *C)
        D[nID] = A[nIA];
    else if (A[nIA] < 0)
        D[nID] = *B;
    else
        D[nID] = *C;
 
}
```

Performs an inverted clip of vector `A` using lower-threshold and  upper-threshold input scalars `*B` and `*C`. Note that negative values in `A` are clipped to `*B`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [-2, -0.5, 0.5, 3]
var low: Float = -1
var high: Float = 1
var d = [Float](repeating: 0, count: a.count)

// Inverted-clip each element of `a`; values within `low` through `high` move out to the nearer bound.
vDSP_viclip(a, 1, &low, &high, &d, 1, vDSP_Length(a.count))

// Prints "[-2.0, -1.0, 1.0, 3.0]".
print(d)
```

**Objective-C**:

```objc
float a[4] = {-2, -0.5, 0.5, 3};
float low = -1;
float high = 1;
float d[4];

// Inverted-clip each element of `a`; values within `low` through `high` move out to the nearer bound.
vDSP_viclip(a, 1, &low, &high, d, 1, 4);

// Prints "[-2, -1, 1, 3]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for `A`
- `__B`: Pointer to single-precision real input scalar: lower threshold
- `__C`: Pointer to single-precision real input scalar: upper threshold
- `__D`: Single-precision real output vector
- `__ID`: Stride for `D`
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
- [vDSP_viclipD](./vdsp_viclipd.md)
  Calculates the elements of a double-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_vthr](./vdsp_vthr.md)
  Calculates single-precision vector threshold to the specified range.
- [vDSP_vthrD](./vdsp_vthrd.md)
  Calculates double-precision vector threshold to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_viclip)*