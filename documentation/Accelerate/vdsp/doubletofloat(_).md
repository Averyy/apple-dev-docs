# doubleToFloat(_:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns single-precision values converted from a double-precision source.

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
static func doubleToFloat<U>(_ source: U) -> [Float] where U : AccelerateBuffer, U.Element == Double
```

## Parameters

- `source`: The source vector.

## See Also

### Conversion between floating-point types
- [static func floatToDouble<U>(U) -> [Double]](./floattodouble%28_%29.md)
  Returns double-precision values converted from a single-precision source.
- [static func convertElements<U, V>(of: U, to: inout V)](./convertelements%28of,to%29-2ejgr.md)
  Converts single-precision values to double-precision values.
- [static func convertElements<U, V>(of: U, to: inout V)](./convertelements%28of,to%29-698ye.md)
  Converts double-precision values to single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/doubletofloat(_:))*