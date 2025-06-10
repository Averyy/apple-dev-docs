# vDSP_vrampmuladd2D

**Framework**: Accelerate  
**Kind**: func

Multiplies a double-precision, stereo input vector by a value that ramps up on successive calls, and cumulatively adds the result to the output vector.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
void vDSP_vrampmuladd2D(const double * __I0, const double * __I1, vDSP_Stride __IS, double * __Start, const double * __Step, double * __O0, double * __O1, vDSP_Stride __OS, vDSP_Length __N);
```

#### Discussion

The functions in this group are similar to [`vDSP_vrampmul`](vdsp_vrampmul.md), but rather than overwriting the output vector, they add the results to the existing values in the output vector. The following code describes the calculation:

```c
for (i = 0; i < N; ++i) {
    O[i*OS] += *Start * I[i*IS];
    *Start += *Step;
}
```

For example, the following code fills the array `i` with sine values:

```swift
let n = vDSP_Length(1024)

let i: [Float] = (0 ..< n).map {
    return sin(Float($0) / 20)
}
```

The following illustrates the values of `i`:

![Visualization of a sine wave.](https://docs-assets.developer.apple.com/published/84dcec7eed7b6ac76bda872718d5f479/media-3239835%402x.png)

The following code fills the output array, o, with increasing powers of two:

```swift
var o = (0 ..< n).map {
    return pow(Float($0), 2) * 0.0001
}
```

The following illustrates the values of `o`:

![Visualization of the exponential curve.](https://docs-assets.developer.apple.com/published/416eded57524f156137cd6433902f900/media-3239780%402x.png)

Pass `i` as the input vector, and `o` as the output vector to [`vDSP_vrampmuladd`](vdsp_vrampmuladd.md)…

```swift
let stride = vDSP_Stride(1)

var start: Float = 0
var step: Float = 0.1

vDSP_vrampmuladd(i,
                 stride,
                 &start,
                 &step,
                 &o,
                 stride,
                 n)
```

On return, the output vector, `o`, is overwritten with a ramped-sine wave, based on its original exponential curve:

![Visualization of the generated vector.](https://docs-assets.developer.apple.com/published/a3e4d91ba93596d284b1803a34ad4fdd/media-3239833%402x.png)

## Parameters

- `__I0`: The first input vector, multiplied by the ramp function.
- `__I1`: The second input vector, multiplied by the ramp function.
- `__IS`: The stride for both input vectors.
- `__Start`: On input, the initial value of the ramp. On output, the next value in the ramp.
- `__Step`: The increment, or decrement if negative, between each generated element.
- `__O0`: The first output vector.
- `__O1`: The second output vector.
- `__OS`: The stride for both output vectors.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vrampmul2](vdsp_vrampmul2.md)
  Generates a single-precision, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2D](vdsp_vrampmul2d.md)
  Generates a double-precision, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2_s1_15](vdsp_vrampmul2_s1_15.md)
  Generates a fixed-point, 1.15 format, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2_s8_24](vdsp_vrampmul2_s8_24.md)
  Generates a fixed-point, 8.24 format, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmuladd2](vdsp_vrampmuladd2.md)
  Multiplies a single-precision, stereo input vector by a value that ramps up on successive calls, and cumulatively adds the result to the output vector.
- [vDSP_vrampmuladd2_s1_15](vdsp_vrampmuladd2_s1_15.md)
  Multiplies a fixed-point, 1.15 format, stereo input vector by a value that ramps on successive calls, and adds the result to the output vector.
- [vDSP_vrampmuladd2_s8_24](vdsp_vrampmuladd2_s8_24.md)
  Multiplies a fixed-point, 8.24 format, stereo input vector by a value that ramps on successive calls, and adds the result to the output vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrampmuladd2d)*