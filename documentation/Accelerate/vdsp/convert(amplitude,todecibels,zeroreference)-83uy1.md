# convert(amplitude:toDecibels:zeroReference:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Converts single-precision amplitude values to decibel values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
static func convert<U, V>(amplitude: U, toDecibels decibels: inout V, zeroReference: Float) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
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

### Converting single-precision power or amplitude values to decibel values
- [static func amplitudeToDecibels<U>(U, zeroReference: Float) -> [Float]](./amplitudetodecibels%28_,zeroreference%29-88bpy.md)
  Returns single-precision amplitude values converted to decibels.
- [static func powerToDecibels<U>(U, zeroReference: Float) -> [Float]](./powertodecibels%28_,zeroreference%29-861j5.md)
  Returns single-precision power values converted to decibel values.
- [static func convert<U, V>(power: U, toDecibels: inout V, zeroReference: Float)](./convert%28power,todecibels,zeroreference%29-5u3vs.md)
  Converts single-precision power values to decibel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convert(amplitude:todecibels:zeroreference:)-83uy1)*