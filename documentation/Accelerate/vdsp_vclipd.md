# vDSP_vclipD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the elements of a double-precision vector clipped to the specified range.

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
extern void vDSP_vclipD(const double *__A, vDSP_Stride __IA, const double *__B, const double *__C, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

This function performs the operation below:

```objc
for (n = 0; n < N; ++n) {
    if (A[n*IA] < *B)
        D[n*ID] = *B;
    else if (A[n*IA] > *C)
        D[n*ID] = *C;
    else
        D[n*ID] = A[n*IA];
}
```

On return, the output contains the clipped elements of the input. The function sets elements that are less than the low-clipping threshold to `__B`, and sets elements that are greater than the high-clipping threshold to `__C`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-2, -0.5, 0.5, 3]
var low: Double = -1
var high: Double = 1
var d = [Double](repeating: 0, count: a.count)

// Clip each element of `a` to the range `low` through `high`.
vDSP_vclipD(a, 1, &low, &high, &d, 1, vDSP_Length(a.count))

// Prints "[-1.0, -0.5, 0.5, 1.0]".
print(d)
```

**Objective-C**:

```objc
double a[4] = {-2, -0.5, 0.5, 3};
double low = -1;
double high = 1;
double d[4];

// Clip each element of `a` to the range `low` through `high`.
vDSP_vclipD(a, 1, &low, &high, d, 1, 4);

// Prints "[-1, -0.5, 0.5, 1]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The stride for the input vector.
- `__B`: A pointer to the scalar low-clipping threshold. If the low-clipping threshold is greater than the high-clipping threshold, the function calculates an undefined result.
- `__C`: A pointer to the scalar high-clipping threshold. If the high-clipping threshold is less than the low-clipping threshold, the function calculates an undefined result.
- `__D`: The output vector.
- `__ID`: The stride for the output vector.
- `__N`: The number of elements that the function clips to the specified range.

## See Also

### Clipping Operations
- [vDSP_vclip](./vdsp_vclip.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipc](./vdsp_vclipc.md)
  Calculates and counts the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipcD](./vdsp_vclipcd.md)
  Calculates and counts the elements of a double-precision vector clipped to the specified range.
- [vDSP_viclip](./vdsp_viclip.md)
  Calculates the elements of a single-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_viclipD](./vdsp_viclipd.md)
  Calculates the elements of a double-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_vthr](./vdsp_vthr.md)
  Calculates single-precision vector threshold to the specified range.
- [vDSP_vthrD](./vdsp_vthrd.md)
  Calculates double-precision vector threshold to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vclipd)*