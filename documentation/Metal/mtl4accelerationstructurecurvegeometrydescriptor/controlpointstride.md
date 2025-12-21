# controlPointStride

**Framework**: Metal  
**Kind**: property

Sets the stride, in bytes, between control points in the control point buffer the control point buffer references.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var controlPointStride: Int { get set }
```

#### Discussion

You are responsible for ensuring this stride is a multiple of the control point format’s element size, and at a minimum exactly the control point format’s size.

This property defaults to `0`, indicating that the control points are tightly-packed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointstride)*