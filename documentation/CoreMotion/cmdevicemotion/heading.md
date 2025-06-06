# heading

**Framework**: Core Motion  
**Kind**: property

The heading angle (measured in degrees) relative to the current reference frame.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 4.0+

## Declaration

```swift
var heading: Double { get }
```

#### Discussion

This property contains a value in the range of `0.0` to `360.0` degrees. This value is available only when the frame of reference is [`xMagneticNorthZVertical`](cmattitudereferenceframe/xmagneticnorthzvertical.md) or [`xTrueNorthZVertical`](cmattitudereferenceframe/xtruenorthzvertical.md). If the reference frame is [`xArbitraryZVertical`](cmattitudereferenceframe/xarbitraryzvertical.md) or [`xArbitraryCorrectedZVertical`](cmattitudereferenceframe/xarbitrarycorrectedzvertical.md), this property contains a negative number to indicate the heading is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotion/heading)*