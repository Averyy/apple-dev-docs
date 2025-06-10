# linearInterpolate(_:_:using:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the linear interpolation between the supplied double-precision vectors.

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
static func linearInterpolate<T, U, V>(_ vectorA: T, _ vectorB: U, using interpolationConstant: Double, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Double, U.Element == Double, V.Element == Double
```

#### Discussion

Single-precision and double-precision [`linearInterpolate(_:_:using:result:)`](vdsp/linearinterpolate(_:_:using:result:)-6o7a9.md) functions calculate a vector that’s the elementwise linear interpolation between the two supplied vectors.

For example, the following code creates two arrays, vectorA and vectorB, that contain sine waves:

```swift
let n = 1024

let vectorA: [Float] = (0 ... n).map {
    return 2 + sin(Float($0) * 0.07)
}

let vectorB: [Float] = (0 ... n).map {
    return -2 + sin(Float($0) * 0.03)
}
```

Use [`linearInterpolate(_:_:using:)`](vdsp/linearinterpolate(_:_:using:)-71as1.md) with an interpolation constant of 0.5 to generate a new vector that’s the average of the two sine waves:

```swift
let result = vDSP.linearInterpolate(vectorA, vectorB,
                                    using: 0.5)
```

The following figure visualizes the two source vectors: the blue lines at the top and bottom, and the interpolation result: the red line in the center:

![Graphic illustrating two sine waves and a third vector that’s the linear interpolation between them.](https://docs-assets.developer.apple.com/published/80d7655938ef049813f9ca5edd8e745e/media-3521345%402x.png)

## See Also

- [static func linearInterpolate<T, U>(T, U, using: Double) -> [Double]](vdsp/linearinterpolate(_:_:using:)-3j5d2.md)
  Returns the linear interpolation between the supplied double-precision vectors.
- [static func linearInterpolate<T, U>(T, U, using: Float) -> [Float]](vdsp/linearinterpolate(_:_:using:)-71as1.md)
  Returns the linear interpolation between the supplied single-precision vectors.
- [static func linearInterpolate<T, U, V>(T, U, using: Float, result: inout V)](vdsp/linearinterpolate(_:_:using:result:)-55avl.md)
  Calculates the linear interpolation between the supplied single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/linearinterpolate(_:_:using:result:)-6o7a9)*