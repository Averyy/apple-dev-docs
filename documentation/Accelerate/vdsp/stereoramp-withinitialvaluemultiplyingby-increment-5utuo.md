# stereoRamp(withInitialValue:multiplyingBy:_:increment:)

**Framework**: Accelerate  
**Kind**: method

Returns two double-precision vectors that contain stereo monotonically incrementing or decrementing values multiplied by two source vectors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func stereoRamp<U>(withInitialValue initialValue: inout Double, multiplyingBy multiplierOne: U, _ multiplierTwo: U, increment: Double) -> (firstOutput: [Double], secondOutput: [Double]) where U : AccelerateBuffer, U.Element == Double
```

#### Discussion

Use this function to create two vectors by multiplying the values in two input vectors with the corresponding values of a ramp.

For example, the following code fills the arrays `multiplierOne` and `multiplierTwo` with sine values:

```swift
let n = vDSP_Length(1024)

let multiplierOne: [Double] = (0 ..< n).map {
    return sin(Double($0) / 20) * 2
}

let multiplierTwo: [Double] = (0 ..< n).map {
    return sin(Double($0) / 40)
}
```

The following figure illustrates the values of `multiplierOne`, as a solid line, and `multiplierTwo`, as a dashed line:

![A graphic shows two sine waves. The first sine wave appears as a solid line and the second sine wave appears as a dashed line. The first sine wave has a higher freqency and a higher amplitude than the second sine wave. ](https://docs-assets.developer.apple.com/published/07d841cbd0f14afc7222e9a7b93aba50/media-3732282%402x.png)

Pass `multiplierOne` and `multiplierTwo` as the `multiplyingBy` parameter of [`stereoRamp(withInitialValue:multiplyingBy:_:increment:)`](vdsp/stereoramp(withinitialvalue:multiplyingby:_:increment:)-18f8z.md):

```swift
var start: Double = 0
let step: Double = 0.1

let results = vDSP.stereoRamp(withInitialValue: &start,
                              multiplyingBy: multiplierOne, multiplierTwo,
                              increment: step)
```

On return, the output vectors, `results.firstOutput` and `results.secondOutput`, contain ramped-sine waves. The figure below shows the first output as a solid line and the second output as a dashed line:

![A graphic shows two sine waves. The first sine wave appears as a solid line and the second sine wave appears as a dashed line. The first sine wave and has a higher freqency and a higher amplitude than the second sine wave.  Both sine waves are tapered, that is, they begin on the left with a very low amplitude and their amplitudes ramp up towards the right of the image.](https://docs-assets.developer.apple.com/published/e4e631a2cffd2e94d7be845c1d26a6ca/media-3732279%402x.png)

## Parameters

- `initialValue`: The initial value of the ramp.
- `multiplierOne`: The first input vector that’s multiplied by the ramp function.
- `multiplierTwo`: The second input vector that’s multiplied by the ramp function.
- `increment`: The increment, or decrement if negative, between each generated element.

## See Also

- [static func absolute<U>(U) -> [Double]](vdsp/absolute(_:)-9c3ge.md)
  Returns the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U>(U) -> [Float]](vdsp/absolute(_:)-5ehc1.md)
  Returns the absolute value of each element in the supplied single-precision vector.
- [static func absolute<V>(DSPSplitComplex, result: inout V)](vdsp/absolute(_:result:)-9x5jn.md)
  Calculates the absolute value of each element in the supplied single-precision complex vector.
- [static func absolute<V>(DSPDoubleSplitComplex, result: inout V)](vdsp/absolute(_:result:)-1wu9x.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-657bd.md)
  Calculates the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-4pigo.md)
  Calculates the absolute value of each element in the supplied single-precision vector.
- [static func add<U>(Double, U) -> [Double]](vdsp/add(_:_:)-9mv1a.md)
  Returns the double-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Double]](vdsp/add(_:_:)-2ftxc.md)
  Returns the double-precision element-wise sum of two vectors.
- [static func add<U>(Float, U) -> [Float]](vdsp/add(_:_:)-53nh9.md)
  Returns the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U>(T, U) -> [Float]](vdsp/add(_:_:)-7swvf.md)
  Returns the single-precision element-wise sum of two vectors.
- [static func add<U, V>(Double, U, result: inout V)](vdsp/add(_:_:result:)-2531u.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<U, V>(Float, U, result: inout V)](vdsp/add(_:_:result:)-2w0o9.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-338hl.md)
  Calculates the double-precision element-wise sum of two vectors.
- [static func add<T, U, V>(T, U, result: inout V)](vdsp/add(_:_:result:)-3vzwi.md)
  Calculates the single-precision element-wise sum of two vectors.
- [static func add(DSPSplitComplex, to: DSPSplitComplex, count: Int, result: inout DSPSplitComplex)](vdsp/add(_:to:count:result:)-g1dk.md)
  Calculates the single-precision elementwise sum of the supplied complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/stereoramp(withinitialvalue:multiplyingby:_:increment:)-5utuo)*