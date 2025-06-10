# linearInterpolate(elementsOf:using:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the interpolation between the neighboring elements of a double-precision vector.

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
static func linearInterpolate<T, U, V>(elementsOf vector: T, using controlVector: U, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Double, U.Element == Double, V.Element == Double
```

#### Discussion

Single-precision and double-precision [`linearInterpolate(elementsOf:using:result:)`](vdsp/linearinterpolate(elementsof:using:result:)-4n3lr.md) functions calculate an array of an arbitrary length that’s constructed from the linearly interpolated values in a source array. Pass [`linearInterpolate(elementsOf:using:result:)`](vdsp/linearinterpolate(elementsof:using:result:)-4n3lr.md) a control vector that defines the interpolation: the integer part of each element in the control vector is the zero-based index of the first element of a pair of adjacent values in the source array, and the fractional part defines the linear interpolation between the values at those indices.

For example, the following code generates a five-element vector by interpolating three values:

```swift
let result = vDSP.linearInterpolate(elementsOf: [100, 200, 300],
                                    using: [0, 0.5, 1, 1.5, 2])
```

On return, `result` contains `[100.0, 150.0, 200.0, 250.0, 300.0]`.

To compute longer interpolation results, use [`ramp(in:count:)`](vdsp/ramp(in:count:)-79aw7.md) to generate the control vector. The following code creates 1024 interpolated values from 10 source values:

```swift
let values: [Float] = [50, 90, 55, 10, 40, 85, 65, 15, 30, 80]
let controlVector: [Float] = vDSP.ramp(in: 0 ... Float(values.count) - 1,
                                       count: 1024)

let result = vDSP.linearInterpolate(elementsOf: values,
                                    using: controlVector)
```

The following figure visualizes the elements in `result`.

![A graph of the linearly interpolated values based on a control vector created with a ramp.](https://docs-assets.developer.apple.com/published/0d5856610f65ab0f6294cdb17a50010d/media-3512160%402x.png)

By changing the technique used to form the fractional parts of the control vector, you change the interpolation between the values in the source vector. The following code uses a sigmoid function—that is, a function that has an “S” shaped curve—to populate the control vector:

```swift
let values: [Float] = [50, 90, 55, 10, 40, 85, 65, 15, 30, 80]

let denominator = 1024 / Float(values.count - 1)
let tau = Float.pi * 2
let controlVector: [Float] = (0 ..< 1024).map {
    let x = modf(Float($0) / denominator)
    
    return x.0 + (tanh((x.1 - 0.5) * tau) * 0.5) + 0.5
}

let result = vDSP.linearInterpolate(elementsOf: values,
                                    using: controlVector)
```

The following figure visualizes the elements in `result` using hyperbolic tangent for the sigmoid function.

![A graph of the linearly interpolated values based on a control vector created with a sigmoid function.](https://docs-assets.developer.apple.com/published/4678ecddd904bcf461a943c01486a70b/media-3512155%402x.png)

## Parameters

- `vector`: An array that contains the values to interpolate.
- `controlVector`: An array that defines the interpolation: integer parts are indices into   and fractional parts are interpolation constants.
- `result`: An array that receives the result of the calculation.

## See Also

- [Using linear interpolation to construct new data points](using-linear-interpolation-to-construct-new-data-points.md)
  Fill the gaps in arrays of numerical data using linear interpolation.
- [static func linearInterpolate<T, U>(elementsOf: T, using: U) -> [Double]](vdsp/linearinterpolate(elementsof:using:)-5i3jc.md)
  Returns the interpolation between the neighboring elements of a double-precision vector.
- [static func linearInterpolate<T, U>(elementsOf: T, using: U) -> [Float]](vdsp/linearinterpolate(elementsof:using:)-49r3c.md)
  Returns the interpolation between the neighboring elements of a single-precision vector.
- [static func linearInterpolate<T, U, V>(elementsOf: T, using: U, result: inout V)](vdsp/linearinterpolate(elementsof:using:result:)-9y61c.md)
  Calculates the interpolation between the neighboring elements of a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/linearinterpolate(elementsof:using:result:)-4n3lr)*