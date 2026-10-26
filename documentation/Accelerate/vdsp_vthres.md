# vDSP_vthres

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates single-precision vector threshold with zero fill to the specified range.

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
extern void vDSP_vthres(const float *__A, vDSP_Stride __IA, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Performs the following operation:

```objc
for (n = 0; n < N; ++n){
    if (A[n*IA] >= *B)
        C[n*IC] = A[n*IA];
    else
        C[n*IC] = 0;
}
```

Creates vector `C` by comparing each input from vector `A` with scalar `*B`. If  an input value is less than `*B`, zero is written to `C`; otherwise, the input value from `A` is  copied to `C`.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [-2, -0.5, 0.5, 3]
var threshold: Float = 0
var c = [Float](repeating: 0, count: a.count)

// Apply a threshold with zero fill: Keep elements at least `threshold`, and set the rest to `0`.
vDSP_vthres(a, 1, &threshold, &c, 1, vDSP_Length(a.count))

// Prints "[0.0, 0.0, 0.5, 3.0]".
print(c)
```

**Objective-C**:

```objc
float a[4] = {-2, -0.5, 0.5, 3};
float threshold = 0;
float c[4];

// Apply a threshold with zero fill: Keep elements at least `threshold`, and set the rest to `0`.
vDSP_vthres(a, 1, &threshold, c, 1, 4);

// Prints "[0, 0, 0.5, 3]".
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

### Threshold Operations
- [vDSP_vthresD](./vdsp_vthresd.md)
  Calculates double-precision vector threshold with zero fill to the specified range.
- [vDSP_vthrsc](./vdsp_vthrsc.md)
  Calculates single-precision vector threshold with signed constant to the specified range.
- [vDSP_vthrscD](./vdsp_vthrscd.md)
  Calculates double-precision vector threshold with signed constant to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vthres)*