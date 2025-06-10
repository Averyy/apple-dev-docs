# doubleToFloat(_:)

**Framework**: Accelerate  
**Kind**: method

Returns single-precision values converted from a double-precision source.

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
static func doubleToFloat<U>(_ source: U) -> [Float] where U : AccelerateBuffer, U.Element == Double
```

## Parameters

- `source`: The source vector.

## See Also

- [static func floatToDouble<U>(U) -> [Double]](vdsp/floattodouble(_:).md)
  Returns double-precision values converted from a single-precision source.
- [static func convertElements<U, V>(of: U, to: inout V)](vdsp/convertelements(of:to:)-2ejgr.md)
  Converts single-precision values to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](vdsp/convertelements(of:to:)-698ye.md)
  Converts double-precision values to single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/doubletofloat(_:))*