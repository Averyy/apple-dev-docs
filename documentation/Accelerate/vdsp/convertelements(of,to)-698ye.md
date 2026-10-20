# convertElements(of:to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Converts double-precision values to single-precision values.

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
static func convertElements<U, V>(of source: U, to destination: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Float
```

## Parameters

- `source`: The source vector.
- `destination`: On output, the source values converted to single-precision values.

## See Also

### Conversion between floating-point types
- [static func doubleToFloat<U>(U) -> [Float]](./doubletofloat%28_%29.md)
  Returns single-precision values converted from a double-precision source.
- [static func floatToDouble<U>(U) -> [Double]](./floattodouble%28_%29.md)
  Returns double-precision values converted from a single-precision source.
- [static func convertElements<U, V>(of: U, to: inout V)](./convertelements%28of,to%29-2ejgr.md)
  Converts single-precision values to double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/convertelements(of:to:)-698ye)*