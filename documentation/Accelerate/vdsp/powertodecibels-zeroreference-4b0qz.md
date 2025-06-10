# powerToDecibels(_:zeroReference:)

**Framework**: Accelerate  
**Kind**: method

Returns double-precision power values converted to decibel values.

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
static func powerToDecibels<U>(_ power: U, zeroReference: Double) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

#### Discussion

The function uses the following calculation to perform the conversion:

```swift
alpha = 10;

for (n = 0; n < N; ++n)
    C[n] = alpha * log10(A[n] / B[0]);
```

## Parameters

- `power`: The input vector that defines the power values.
- `zeroReference`: The zero reference that the function uses for the conversion.

## See Also

- [static func amplitudeToDecibels<U>(U, zeroReference: Double) -> [Double]](vdsp/amplitudetodecibels(_:zeroreference:)-2cgik.md)
  Returns double-precision amplitude values converted to decibel values.
- [static func convert<U, V>(amplitude: U, toDecibels: inout V, zeroReference: Double)](vdsp/convert(amplitude:todecibels:zeroreference:)-4io4p.md)
  Converts double-precision amplitude values to decibel values.
- [static func convert<U, V>(power: U, toDecibels: inout V, zeroReference: Double)](vdsp/convert(power:todecibels:zeroreference:)-3aiv4.md)
  Converts double-precision power values to decibel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/powertodecibels(_:zeroreference:)-4b0qz)*