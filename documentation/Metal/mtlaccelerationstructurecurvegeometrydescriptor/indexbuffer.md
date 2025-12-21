# indexBuffer

**Framework**: Metal  
**Kind**: property

A buffer that contains references to control points in the control point buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var indexBuffer: (any MTLBuffer)? { get set }
```

#### Discussion

This property needs to have a non-nil value when you build an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indexbuffer)*