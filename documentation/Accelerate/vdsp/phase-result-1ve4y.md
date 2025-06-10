# phase(_:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the single-precision element-wise phase values, in radians, of the supplied complex vector.

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
static func phase<V>(_ splitComplex: DSPSplitComplex, result: inout V) where V : AccelerateMutableBuffer, V.Element == Float
```

## See Also

- [static func phase<V>(DSPDoubleSplitComplex, result: inout V)](vdsp/phase(_:result:)-56qb1.md)
  Calculates the double-precision element-wise phase values, in radians, of the supplied complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/phase(_:result:)-1ve4y)*