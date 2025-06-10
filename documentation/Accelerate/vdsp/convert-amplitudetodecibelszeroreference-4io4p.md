# convert(amplitude:toDecibels:zeroReference:)

**Framework**: Accelerate  
**Kind**: method

Converts double-precision amplitude values to decibel values.

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
static func convert<U, V>(amplitude: U, toDecibels decibels: inout V, zeroReference: Double) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

#### Discussion

The function uses the following calculation to perform the conversion:

```swift
alpha = 20;

for (n = 0; n < N; ++n)
    C[n] = alpha * log10(A[n] / B[0]);
```

## Parameters

- `amplitude`: The input vector that defines the amplitude values.
- `decibels`: The output vector that contains the decibel values.
- `zeroReference`: The zero reference that the function uses for the conversion.

## See Also

- [static func amplitudeToDecibels<U>(U, zeroReference: Double) -> [Double]](vdsp/amplitudetodecibels(_:zeroreference:)-2cgik.md)
  Returns double-precision amplitude values converted to decibel values.
- [static func powerToDecibels<U>(U, zeroReference: Double) -> [Double]](vdsp/powertodecibels(_:zeroreference:)-4b0qz.md)
  Returns double-precision power values converted to decibel values.
- [static func convert<U, V>(power: U, toDecibels: inout V, zeroReference: Double)](vdsp/convert(power:todecibels:zeroreference:)-3aiv4.md)
  Converts double-precision power values to decibel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convert(amplitude:todecibels:zeroreference:)-4io4p)*