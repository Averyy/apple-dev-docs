# radiusBuffer

**Framework**: Metal  
**Kind**: property

A buffer that contains the curve radius for each control point.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var radiusBuffer: (any MTLBuffer)? { get set }
```

#### Discussion

The buffer contains values that are greater than or equal to `0.0` in the format you configure with the [`radiusFormat`](mtlaccelerationstructurecurvegeometrydescriptor/radiusformat.md) property. This property needs to have a non-nil value when you build an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusbuffer)*