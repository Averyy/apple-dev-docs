# vDSP_vrampmuladd2_s8_24

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Multiplies a fixed-point, 8.24 format, stereo input vector by a value that ramps on successive calls, and adds the result to the output vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
void vDSP_vrampmuladd2_s8_24(const int *__I0, const int *__I1, vDSP_Stride __IS, int *__Start, const int *__Step, int *__O0, int *__O1, vDSP_Stride __OS, vDSP_Length __N);
```

## Discussion

The functions in this group are similar to [`vDSP_vrampmul`](./vdsp_vrampmul.md), but rather than overwriting the output vector, they add the results to the existing values in the output vector. The following code describes the calculation:

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

![Visualization of a sine wave.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3239803@2x.png)

The following code fills the output array, o, with increasing powers of two:

```swift
var o = (0 ..< n).map {
    return pow(Float($0), 2) * 0.0001
}
```

The following illustrates the values of `o`:

![Visualization of the exponential curve.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3239819@2x.png)

Pass `i` as the input vector, and `o` as the output vector to [`vDSP_vrampmuladd`](./vdsp_vrampmuladd.md)…

**Swift**:

```swift
let i0: [Int32] = [10, 20, 30, 40, 50, 60, 70, 80]
let i1: [Int32] = [80, 70, 60, 50, 40, 30, 20, 10]
var o0: [Int32] = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
var o1: [Int32] = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

var start: Int32 = 0
var step: Int32 = 1 << 24   // 1.0 in Q8.24

vDSP_vrampmuladd2_s8_24(i0, i1, 1,
                        &start,
                        &step,
                        &o0, &o1, 1,
                        8)

// Prints "[1000, 1020, 1060, 1120, 1200, 1300, 1420, 1560]".
print(o0)

// Prints "[1000, 1070, 1120, 1150, 1160, 1150, 1120, 1070]".
print(o1)
```

**Objective-C**:

```objc
int i0[8] = {10, 20, 30, 40, 50, 60, 70, 80};
int i1[8] = {80, 70, 60, 50, 40, 30, 20, 10};
int o0[8] = {1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000};
int o1[8] = {1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000};

int start = 0;
int step = 1 << 24;   // 1.0 in Q8.24

vDSP_vrampmuladd2_s8_24(i0, i1, 1,
                        &start,
                        &step,
                        o0, o1, 1,
                        8);

// Prints "o0=[1000, 1020, 1060, 1120, 1200, 1300, 1420, 1560]".
printf("o0=[%d, %d, %d, %d, %d, %d, %d, %d]\n",
       o0[0], o0[1], o0[2], o0[3],
       o0[4], o0[5], o0[6], o0[7]);

// Prints "o1=[1000, 1070, 1120, 1150, 1160, 1150, 1120, 1070]".
printf("o1=[%d, %d, %d, %d, %d, %d, %d, %d]\n",
       o1[0], o1[1], o1[2], o1[3],
       o1[4], o1[5], o1[6], o1[7]);
```

On return, the output vector, `o`, is overwritten with a ramped-sine wave, based on its original exponential curve:

![Visualization of the generated vector.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3239797@2x.png)

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

### Stereo ramp generation
- [vDSP_vrampmul2](./vdsp_vrampmul2.md)
  Generates a single-precision, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2D](./vdsp_vrampmul2d.md)
  Generates a double-precision, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2_s1_15](./vdsp_vrampmul2_s1_15.md)
  Generates a fixed-point, 1.15 format, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmul2_s8_24](./vdsp_vrampmul2_s8_24.md)
  Generates a fixed-point, 8.24 format, stereo ramped vector and multiplies that vector by an input vector.
- [vDSP_vrampmuladd2](./vdsp_vrampmuladd2.md)
  Multiplies a single-precision, stereo input vector by a value that ramps up on successive calls, and cumulatively adds the result to the output vector.
- [vDSP_vrampmuladd2D](./vdsp_vrampmuladd2d.md)
  Multiplies a double-precision, stereo input vector by a value that ramps up on successive calls, and cumulatively adds the result to the output vector.
- [vDSP_vrampmuladd2_s1_15](./vdsp_vrampmuladd2_s1_15.md)
  Multiplies a fixed-point, 1.15 format, stereo input vector by a value that ramps on successive calls, and adds the result to the output vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrampmuladd2_s8_24)*