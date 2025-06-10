# phase(_:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the double-precision element-wise phase values, in radians, of the supplied complex vector.

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
static func phase<V>(_ splitComplex: DSPDoubleSplitComplex, result: inout V) where V : AccelerateMutableBuffer, V.Element == Double
```

## See Also

- [static func phase<V>(DSPSplitComplex, result: inout V)](vdsp/phase(_:result:)-1ve4y.md)
  Calculates the single-precision element-wise phase values, in radians, of the supplied complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/phase(_:result:)-56qb1)*