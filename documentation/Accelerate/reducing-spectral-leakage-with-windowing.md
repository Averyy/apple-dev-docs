# Reducing spectral leakage with windowing

**Framework**: Accelerate

Multiply signal data by window sequence values when performing transforms with noninteger period signals.

#### Overview

Discrete Fourier and cosine transforms, which decompose a signal into its component frequencies and recreate a signal from a component frequency representation, work over vectors of specific lengths. For example, if you’re analyzing audio data, the data might be represented as pages of 1024 samples. Discrete Fourier and cosine transforms can accurately approximate the component frequencies that have an integer number of periods — that is, signals where the start and end points join to form a continuous waveform.

However, with noninteger period signals, where the endpoints don’t meet, the discontinuities appear as false frequency components in a forward transform. This smearing of data is called spectral leakage.

You can use an approach called windowing to reduce spectral leakage when performing transforms over data that includes noninteger period signals.  multiplies a signal by a vector that represents a smooth curve with boundary values of zero or near zero. This technique ensures that the endpoints of a signal meet and reduces the discontinuities.

##### Synthesize a Test Signal

The code examples in this article synthesize the signal data from a series of sine waves. In a real-world app, you’ll most likely acquire signal data from a sensor such as a microphone.

Use the `synthesizeSignal` function to generate a composite sine wave from a supplied array of component frequencies and amplitudes:

```swift
static func synthesizeSignal(frequencyAmplitudePairs: [(f: Float, a: Float)],
                             count: Int) -> [Float] {
    
    let tau: Float = .pi * 2
    let signal: [Float] = (0 ..< count).map { index in
        frequencyAmplitudePairs.reduce(0) { accumulator, frequenciesAmplitudePair in
            let normalizedIndex = Float(index) / Float(count)
            return accumulator + sin(normalizedIndex * frequenciesAmplitudePair.f * tau) * frequenciesAmplitudePair.a
        }
    }
    
    return signal
}
```

##### Create a Signal with an Integer Number of Periods

Using the code below, generate  a Fourier series approximation of a square wave that’s built from a series of sine waves. Each component sine wave has an integer number of periods over the length of the data.

```swift
let n = 2048

let baseFrequency: Float = 5

let frequencyAmplitudePairs = stride(from: 1, to: 50, by: 2).map { i in
    return(f: baseFrequency * Float(i), a: (1 / Float(i)))
}

var signal = synthesizeSignal(frequencyAmplitudePairs: frequencyAmplitudePairs,
                              count: n)
```

Use the vDSP fast Fourier transform (FFT), like in the example below, to compute the component frequencies of `signal`:

```swift
let count = n / 2
var realParts = [Float](repeating: 0,
                        count: count)
var imagParts = [Float](repeating: 0,
                        count: count)

realParts.withUnsafeMutableBufferPointer { realPtr in
    imagParts.withUnsafeMutableBufferPointer { imagPtr in
        
        var complexSignal = DSPSplitComplex(realp: realPtr.baseAddress!,
                                            imagp: imagPtr.baseAddress!)
               
        signal.withUnsafeBytes {
            vDSP.convert(interleavedComplexVector: [DSPComplex]($0.bindMemory(to: DSPComplex.self)),
                         toSplitComplexVector: &complexSignal)
        }
        
        let log2n = vDSP_Length(log2(Float(n)))
        let fft = vDSP.FFT(log2n: log2n,
                           radix: .radix2,
                           ofType: DSPSplitComplex.self)
        
        fft?.forward(input: complexSignal,
                     output: &complexSignal)
    }
}
```

To learn more about computing the frequency components of a signal, see [`Finding the component frequencies in a composite sine wave`](finding-the-component-frequencies-in-a-composite-sine-wave.md).

The FFT treats the data set as a single period of a continuous signal. The visualization below wraps the signal around a virtual cylinder to illustrate how the FFT interprets the data. This figure also shows that the endpoints meet:

![A diagram showing a square wave wrapped around a cylinder. The signal’s endpoints meet.](https://docs-assets.developer.apple.com/published/534773563e330418a842cf29546dd230/media-3375140%402x.png)

The illustration below shows a representation of the original signal in blue, and the imaginary parts of the frequency-domain data in yellow:

![A diagram showing a square wave and its frequency domain representation. The frequency domain consists of 25 discrete peaks that represent the 25 component sine waves.](https://docs-assets.developer.apple.com/published/9328e5c195fc55a3861bde0af80b84f4/media-3375147%402x.png)

> **Note**:  The visualizations of the frequency-domain data in this article are transformed to improve visibility. Each visualization is actually the square root of the absolute value of each element of `imagParts`.

The FFT result shows that the signal is composed of 25 sine waves, represented as spikes in the graph.

##### Create a Signal with a Noninteger Number of Periods

Use the code below to define a series of sine waves with noninteger periods:

```swift
let n = 2048

let baseFrequency: Float = 5.75

let frequencyAmplitudePairs = stride(from: 1, to: 50, by: 2).map { i in
    return(f: baseFrequency * Float(i), a: (1 / Float(i)))
}

var signal = synthesizeSignal(frequencyAmplitudePairs: frequencyAmplitudePairs,
                              count: n)
```

The visualization below wraps the noninteger-period signal around a virtual cylinder and shows the endpoint discontinuities:

![A diagram showing a square wave wrapped around a cylinder. The signal’s endpoints do not meet.](https://docs-assets.developer.apple.com/published/3e0ac977f9cbab5dba8f44e55257e0a0/media-3375141%402x.png)

The image below shows the results of a transform of this data. The results shows additional, intermediate values that are the result of spectral leakage.

![A diagram showing a square wave and its frequency domain representation. The frequency domain peaks are smeared across the component frequencies.](https://docs-assets.developer.apple.com/published/814ca6a46771924587acf58591cd4565/media-3375145%402x.png)

##### Create a Windowed Signal with a Noninteger Number of Periods

The code below shows the same noninteger period signal, but in this example, you multiply the signal by the result of [`window(ofType:usingSequence:count:isHalfWindow:)`](vdsp/window(oftype:usingsequence:count:ishalfwindow:).md):

```swift
let n = 2048

let baseFrequency: Float = 5.75

let frequencyAmplitudePairs = stride(from: 1, to: 50, by: 2).map { i in
    return(f: baseFrequency * Float(i), a: (1 / Float(i)))
}

var signal = synthesizeSignal(frequencyAmplitudePairs: frequencyAmplitudePairs,
                              count: n)
 
let window = vDSP.window(ofType: Float.self,
                         usingSequence: .hanningDenormalized,
                         count: n, 
                         isHalfWindow: false)

signal = vDSP.multiply(signal, window)
```

The illustration below shows the windowed signal in blue, with its boundaries tapered toward zero, and the transformed version with reduced spectral leakage in yellow:

![A diagram showing a square wave and its frequency domain representation. The square wave is tapered toward the boundaries and the smearing of frequencies is reduced.](https://docs-assets.developer.apple.com/published/92b809a96edbfb0b10e0ffa6924eb597/media-3375148%402x.png)

##### Select a Window Sequence

vDSP provides functions for generating three different windows:

The image below provides a visual comparison of the different window sequence types:

![Diagram showing the curves generated by Hamming, Hann, and Blackman window functions.](https://docs-assets.developer.apple.com/published/2fab8e8190e861a57ce18331c485060a/media-3379482%402x.png)

##### Create a Sine Wave with a Noninteger Period

To understand the different effects of the different windows provided by vDSP, create a signal that’s composed of a signal sine wave with a noninteger period:

```swift
let frequencyAmplitudePairs = [(f: Float(32.25), a: Float(1))]
```

The illustration below shows the sine wave and the frequency-domain result:

![A diagram showing a sine wave and its frequency domain representation. The frequency domain representation shows a main central peak that’s surrounded by peaks that decrease toward the edges.](https://docs-assets.developer.apple.com/published/b52bd9b3182d5a872fcbe2af4ff6a623/media-3375146%402x.png)

Spectral leakage is apparent throughout the rendered FFT result.

##### Reduce the Spectral Leakage By Using a Hann Window

The illustration below shows the time- and frequency-domain representations of the noninteger period sine wave with the Hann window applied:

![A diagram showing a sine wave and its frequency domain representation. The signal tapers toward zero at the edges. The frequency domain representation shows a main central peak that’s surrounded by peaks that rapidly decrease toward the edges.](https://docs-assets.developer.apple.com/published/9e3a0cce4503db686a3627af98c948dd/media-3375143%402x.png)

##### Reduce the Spectral Leakage By Using a Hamming Window

Create a Hamming window by passing [`vDSP.WindowSequence.hamming`](vdsp/windowsequence/hamming.md) to the [`window(ofType:usingSequence:count:isHalfWindow:)`](vdsp/window(oftype:usingsequence:count:ishalfwindow:).md) function. Unlike the Hann window, the Hamming window doesn’t reach zero at its boundaries.

The figure below shows the result of multiplying the signal by a Hamming window: high values around the base frequency in the forward FFT are tighter than the Hann-windowed result, but there’s low-level spectral leakage across the entire forward FFT:

![A diagram showing a sine wave and its frequency domain representation. The signal tapers toward zero at the edges. The frequency domain representation shows a main central peak that’s surrounded by peaks that rapidly decrease toward the edges.](https://docs-assets.developer.apple.com/published/a4e0152ce1918beb9655a4632aa7fd12/media-3375142%402x.png)

##### Reduce the Spectral Leakage By Using a Blackman Window

Create a Blackman window by passing [`vDSP.WindowSequence.blackman`](vdsp/windowsequence/blackman.md) to the [`window(ofType:usingSequence:count:isHalfWindow:)`](vdsp/window(oftype:usingsequence:count:ishalfwindow:).md) function.

The illustration below shows the time- and frequency-domain representations of the noninteger period sine wave with the Blackman window applied:

![A diagram showing a sine wave and its frequency domain representation. The signal tapers toward zero at the edges. The frequency domain representation shows a main central peak that’s surrounded by peaks that rapidly decrease toward the edges.](https://docs-assets.developer.apple.com/published/275b161d7fd33c943c77bfe2ec7bc75c/media-3375144%402x.png)

## See Also

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Finding the component frequencies in a composite sine wave](finding-the-component-frequencies-in-a-composite-sine-wave.md)
  Use 1D fast Fourier transform to compute the frequency components of a signal.
- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
  Optimize discrete Fourier transform (DFT) performance with the vDSP interleaved DFT routines.
- [Signal extraction from noise](signal-extraction-from-noise.md)
  Use Accelerate’s discrete cosine transform to remove noise from a signal.
- [Performing Fourier Transforms on Multiple Signals](performing-fourier-transforms-on-multiple-signals.md)
  Use Accelerate’s multiple-signal fast Fourier transform (FFT) functions to transform multiple signals with a single function call.
- [Halftone descreening with 2D fast Fourier transform](halftone-descreening-with-2d-fast-fourier-transform.md)
  Reduce or remove periodic artifacts from images.
- [Fast Fourier transforms](fast-fourier-transforms.md)
  Transform vectors and matrices of temporal and spatial domain complex values to the frequency domain, and vice versa.
- [Discrete Fourier transforms](discrete-fourier-transforms.md)
  Transform vectors of temporal and spatial domain complex values to the frequency domain, and vice versa.
- [Discrete Cosine transforms](discrete-cosine-transforms.md)
  Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/reducing-spectral-leakage-with-windowing)*