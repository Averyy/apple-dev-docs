# controlPointStride

**Framework**: Metal  
**Kind**: property

Sets the stride, in bytes, between control points in the control point buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var controlPointStride: Int { get set }
```

#### Discussion

All keyframes share the same control point stride.

You are responsible for ensuring this stride is a multiple of the control point format’s element size, and at a minimum exactly the control point format’s size.

This property defaults to `0`, indicating that the control points are tightly-packed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointstride)*