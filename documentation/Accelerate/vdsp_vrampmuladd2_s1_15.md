# vDSP_vrampmuladd2_s1_15

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Multiplies a fixed-point, 1.15 format, stereo input vector by a value that ramps on successive calls, and adds the result to the output vector.

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
void vDSP_vrampmuladd2_s1_15(const short *__I0, const short *__I1, vDSP_Stride __IS, short *__Start, const short *__Step, short *__O0, short *__O1, vDSP_Stride __OS, vDSP_Length __N);
```

#### Discussion

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

![Visualization of a sine wave.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3239826@2x.png)

The following code fills the output array, o, with increasing powers of two:

```swift
var o = (0 ..< n).map {
    return pow(Float($0), 2) * 0.0001
}
```

The following illustrates the values of `o`:

![Visualization of the exponential curve.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3239941@2x.png)

Pass `i` as the input vector, and `o` as the output vector to [`vDSP_vrampmuladd`](./vdsp_vrampmuladd.md)…

**Swift**:

```swift
let i0: [Int16] = [100, 200, 300, 400, 500, 600, 700, 800]
let i1: [Int16] = [800, 700, 600, 500, 400, 300, 200, 100]
var o0: [Int16] = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
var o1: [Int16] = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

var start: Int16 = 0
var step: Int16 = 32767   // approx 1.0 in Q1.15

vDSP_vrampmuladd2_s1_15(i0, i1, 1,
                        &start,
                        &step,
                        &o0, &o1, 1,
                        8)

// Prints "[1000, 1199, 999, 1399, 999, 1599, 999, 1799]".
print(o0)

// Prints "[1000, 1699, 999, 1499, 999, 1299, 999, 1099]".
print(o1)
```

**Objective-C**:

```objc
short i0[8] = {100, 200, 300, 400, 500, 600, 700, 800};
short i1[8] = {800, 700, 600, 500, 400, 300, 200, 100};
short o0[8] = {1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000};
short o1[8] = {1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000};

short start = 0;
short step = 32767;   // approx 1.0 in Q1.15

vDSP_vrampmuladd2_s1_15(i0, i1, 1,
                        &start,
                        &step,
                        o0, o1, 1,
                        8);

// Prints "o0=[1000, 1199, 999, 1399, 999, 1599, 999, 1799]".
printf("o0=[%d, %d, %d, %d, %d, %d, %d, %d]\n",
      (int)o0[0], (int)o0[1], (int)o0[2], (int)o0[3],
      (int)o0[4], (int)o0[5], (int)o0[6], (int)o0[7]);

// Prints "o1=[1000, 1699, 999, 1499, 999, 1299, 999, 1099]".
printf("o1=[%d, %d, %d, %d, %d, %d, %d, %d]\n",
      (int)o1[0], (int)o1[1], (int)o1[2], (int)o1[3],
      (int)o1[4], (int)o1[5], (int)o1[6], (int)o1[7]);
```

On return, the output vector, `o`, is overwritten with a ramped-sine wave, based on its original exponential curve:

![Visualization of the generated vector.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3239950@2x.png)

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
- [vDSP_vrampmuladd2_s8_24](./vdsp_vrampmuladd2_s8_24.md)
  Multiplies a fixed-point, 8.24 format, stereo input vector by a value that ramps on successive calls, and adds the result to the output vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrampmuladd2_s1_15)*