# Using linear interpolation to construct new data points

**Framework**: Accelerate

Fill the gaps in arrays of numerical data using linear interpolation.

#### Overview

Linear interpolation is a method of calculating intermediate data between known values by conceptually drawing a straight line between two adjacent known values. An interpolated value is any point along that line. You use linear interpolation to, for example, draw graphs or animate between keyframes. The following figure shows an example interpolated value between two points:

![An illustration containing two points joined by a straight line. The first point is at the bottom left of the illustration and the second point is at the top right of the illustration. A point on the line represents an interpolated value.](https://docs-assets.developer.apple.com/published/e5d40e6d782fb5fd618590f925934e0a/media-3122762%402x.png)

vDSP provides the following functions to linearly interpolate between the elements in an array:

- The single-precision function [`linearInterpolate(values:atIndices:)`](vdsp/linearinterpolate(values:atindices:)-5mbnu.md) and the double-precision function [`linearInterpolate(values:atIndices:)`](vdsp/linearinterpolate(values:atindices:)-9rxb4.md) that provide a simple interface for generating interpolated data. These functions wrap [`vDSP_vgenp`](vdsp_vgenp.md) and [`vDSP_vgenpD`](vdsp_vgenpd.md), respectively.
- The single-precision function [`linearInterpolate(elementsOf:using:)`](vdsp/linearinterpolate(elementsof:using:)-49r3c.md) and the double-precision function [`linearInterpolate(elementsOf:using:)`](vdsp/linearinterpolate(elementsof:using:)-5i3jc.md) that provide fine control over the interpolation. These functions wrap [`vDSP_vlint`](vdsp_vlint.md) and [`vDSP_vlintD`](vdsp_vlintd.md), respectively.

This article discusses using these functions to draw a continuous line graph based on a set of discrete data points.

##### Create the Data

In this example, the code interpolates the data that the `values` and `indices` arrays represent.

```swift
let values: [Float] = [50,  90,  55,  10,  40,  85,  65,  15,  30,   80]
let indices: [Float] = [0, 113, 227, 341, 455, 568, 682, 796, 910, 1024]
```

Each array consists of 10 elements. A pair of corresponding elements in the two arrays defines a single point in the diagram as follows:

- Elements in the `values` array denote the vertical position.
- Elements in the `indices` array denote the horizontal position.

![A scatter chart showing a plot of the data points as small circles formed by the corresponding elements in vectors values and indices. ](https://docs-assets.developer.apple.com/published/a658658d3fc93c24761ba8a51c79f234/media-3122542%402x.png)

##### Define the Constant That Represents the Number of Elements

The following code defines `count` as the number of elements in the interpolation result:

```swift
let count = 1024
```

##### Generate a Vector By Interpolation

The [`linearInterpolate(values:atIndices:)`](vdsp/linearinterpolate(values:atindices:)-5mbnu.md) function accepts the `values` and `indices` arrays and returns the interpolation result.

```swift
let result = vDSP.linearInterpolate(values: values,
                                    atIndices: indices)
```

On return, `result` contains the interpolated values. The following graph shows the values in `result` as a line between the known values that the `values` and `indices` arrays describe:

![A line graph showing the known values as small circles joined together by a series of lines that represent the interpolation result.](https://docs-assets.developer.apple.com/published/f63663a39c97078fc7191f42f69a0e52/media-3122764%402x.png)

##### Interpolate with Fine Control

The [`linearInterpolate(elementsOf:using:)`](vdsp/linearinterpolate(elementsof:using:)-49r3c.md) function requires a control vector array that includes fractional parts. The fractional parts define the interpolation between the pair of values in the `values` array, starting at the index that the integer part defines.

Use [`ramp(in:count:)`](vdsp/ramp(in:count:)-79aw7.md) to generate a linear ramp from `0` to the number of elements in `values`, minus `1`. Note that the [`ramp(in:count:)`](vdsp/ramp(in:count:)-79aw7.md) function wraps [`vDSP_vgen`](vdsp_vgen.md).

```swift
let base: Float = 0
let end = Float(values.count - 1)

let control = vDSP.ramp(in: base ... end,
                        count: count)
```

On return, `control` contains the following:

        `[0]	Float	0.0000`

        `[1]	Float	0.0087`

        `[2]	Float	0.0175`

        `...`

        `[1021]	Float	8.9824`

        `[1022]	Float	8.9912`

        `[1023]	Float	9.0000`

The following figure shows a visualization of the values in `control`, with small circles indicating each integer index:

![A line graph showing the linear ramp result as a line from the bottom left to the top right and a series of ten small circles along the line’s length that represent the known values.](https://docs-assets.developer.apple.com/published/4e51407e907ca6096167ee55c36a20d6/media-3122765%402x.png)

The following code passes the control values to [`linearInterpolate(elementsOf:using:)`](vdsp/linearinterpolate(elementsof:using:)-49r3c.md) to calculate the interpolated values:

```swift
let result = vDSP.linearInterpolate(elementsOf: values,
                                    using: control)
```

On return, `result` contains the interpolated values. The graph below shows the values in `result` as a line between the known values that the `values` and `indices` arrays describe:

![A line graph showing the known values as small circles joined together by a series of lines that represent the interpolation result.](https://docs-assets.developer.apple.com/published/f63663a39c97078fc7191f42f69a0e52/media-3122535%402x.png)

The result of [`linearInterpolate(elementsOf:using:)`](vdsp/linearinterpolate(elementsof:using:)-49r3c.md) is equal to the result of [`linearInterpolate(values:atIndices:)`](vdsp/linearinterpolate(values:atindices:)-5mbnu.md).

##### Add Smoothing to the Interpolation Result

You can change the way that you generate the control array to alter the interpolated result. For example, you may want to add smoothing between the segments of a line graph or add easing to an animation. The following code uses [`simd_smoothstep(_:_:_:)`](https://developer.apple.com/documentation/simd/simd_smoothstep(_:_:_:)-993b1) to smooth the fractional parts of `control` near the increments to the integer parts:

```swift
let denominator = Float(n) / Float(values.count - 1)

let control: [Float] = (0 ... count).map {
    let x = Float($0) / denominator
    return floor(x) + simd_smoothstep(0, 1, simd_fract(x))
}
```

The following graph shows a visualization of the values in `control`, with small circles indicating each integer index:

![A line graph showing the smoothed ramp result as a line from the bottom left to the top right. The line flattens near the circles that indicate the index positions.](https://docs-assets.developer.apple.com/published/daffca770b58e0483c3146b920a85869/media-3122763%402x.png)

Using the same call to  [`linearInterpolate(elementsOf:using:)`](vdsp/linearinterpolate(elementsof:using:)-49r3c.md) as above, the result, as shown below, shows a smoother transition between the known values.

![A line graph showing the known values as small circles joined together by a series of smoothly curved lines that represent the interpolation result. ](https://docs-assets.developer.apple.com/published/8128c0584c0f2e51ec4374c046989fb6/media-3122543%402x.png)

## See Also

- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)
  Operate selectively on the elements of a vector at regular intervals.
- [Using vDSP for vector-based arithmetic](using-vdsp-for-vector-based-arithmetic.md)
  Increase the performance of common mathematical tasks with vDSP vector-vector and vector-scalar operations.
- [Resampling a signal with decimation](resampling-a-signal-with-decimation.md)
  Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.
- [vDSP](vdsp-library.md)
  Perform basic arithmetic operations and common digital signal processing (DSP) routines on large vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/using-linear-interpolation-to-construct-new-data-points)*