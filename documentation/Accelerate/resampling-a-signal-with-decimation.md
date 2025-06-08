# Resampling a signal with decimation

**Framework**: Accelerate

Reduce the sample rate of a signal by specifying a decimation factor and applying a custom antialiasing filter.

#### Overview

vDSP provides functions for decimating a signal. A decimated signal has a lower sample rate compared to its original. Decimation can be advantageous when, for example, you are transmitting a signal, creating a visual representation of a large dataset, or reducing the memory overhead when processing data.

In the following pair of images, the original signal on the left contains 1024 samples. After decimation by a factor of two, the result on the right contains 512 samples.

![Diagram showing two signals. The original signal is on the left. The decimated signal, on the right, has the same shape, but is half the width.](https://docs-assets.developer.apple.com/published/88c6aff1a721e1dba492922b19e4077a/media-3123032%402x.png)

##### Create the Input Signal

The following code creates an array and populates it with a composite sine wave:

```swift
let inputLength = 1024
let inputSignal = (0 ..< inputLength).map {
    let x = Float($0)
    return sin(x * 0.007) + sin(x * 0.03)
}
```

The following image shows a visualization of the values in `inputSignal`:

![A line graph showing the original signal as a composite sine wave.](https://docs-assets.developer.apple.com/published/5a9989cc916da8e5bffc0abf9783c63e/media-3122882%402x.png)

vDSP provides the single-precision function [`downsample(_:decimationFactor:filter:)`](vdsp/downsample(_:decimationfactor:filter:)-40d8o.md) and the double-precision function [`downsample(_:decimationFactor:filter:)`](vdsp/downsample(_:decimationfactor:filter:)-1o8it.md) to decimate the elements in an array. These function wrap [`vDSP_desamp`](vdsp_desamp.md) and [`vDSP_desampD`](vdsp_desampd.md), respectively.

##### Define the Antialiasing Filter

The vDSP decimation functions accept a filter that controls how adjacent samples combine. Each decimated value is the sum of the combined original values multiplied by the corresponding filter value.

The following code creates a filter that contains `[0.5, 0.5]`:

```swift
let filterLength = 2
let filter = [Float](repeating: 1 / Float(filterLength),
                     count: filterLength)
```

The resulting filter averages pairs of adjacent values in the original signal.

For the most complete result, set the filter length to the same value as the decimation factor, which indicates how much the original signal is decimated. For example, consider an input signal containing 18 values.

```swift
let originalSignal: [Float] = [10, 15, 20, 25, 50, 25, 20, 15, 10,
                               10, 15, 20, 25, 50, 25, 20, 15, 10]
```

The following images visualize the original and decimated signals and illustrate the effects of different antialiasing filters. The graph below visualizes the signal.

![A line graph showing eighteen points that are joined by lines. The lines form two peaks.](https://docs-assets.developer.apple.com/published/425307266170fc8ad1522c480a5419c7/media-3122893%402x.png)

A filter that contains a single value `[1.0]` combined with a decimation factor of `2` will sample only the even values of the original signal. The decimation functions return a result that misses the second `50` at position `13`, as shown below.

![Diagram showing nine points that are joined by lines. The lines form two peaks, but the peak on the right is truncated.](https://docs-assets.developer.apple.com/published/3ea2758cd04e40861c0ef9f16bff78df/media-3122895%402x.png)

However, a filter with two values, `[0.5, 0.5]` considers all values in the original signal, as illustrated below.

![Diagram showing nine points that are joined by lines. The lines form two fully-formed peaks.](https://docs-assets.developer.apple.com/published/3c0d9503f5944e2dcd47664e4f8ed157/media-3122894%402x.png)

##### Perform the Decimation

The [`downsample(_:decimationFactor:filter:)`](vdsp/downsample(_:decimationfactor:filter:)-40d8o.md) function performs the decimation.

```swift
// The output signal contains `(source.count - filter.count) / decimationFactor + 1`
// elements.
let outputSignal = vDSP.downsample(inputSignal,
                                   decimationFactor: decimationFactor,
                                   filter: filter)
```

On return, `outputSignal` contains the result.

![Diagram showing the decimated signal as a composite sine wave that is half the width of the original signal.](https://docs-assets.developer.apple.com/published/45a2e86d0dfde9ed4a44839999f3be64/media-3122887%402x.png)

## See Also

- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)
  Operate selectively on the elements of a vector at regular intervals.
- [Using linear interpolation to construct new data points](using-linear-interpolation-to-construct-new-data-points.md)
  Fill the gaps in arrays of numerical data using linear interpolation.
- [Using vDSP for vector-based arithmetic](using-vdsp-for-vector-based-arithmetic.md)
  Increase the performance of common mathematical tasks with vDSP vector-vector and vector-scalar operations.
- [vDSP](vdsp-library.md)
  Perform basic arithmetic operations and common digital signal processing (DSP) routines on large vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/resampling-a-signal-with-decimation)*