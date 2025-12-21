# radiusStride

**Framework**: Metal  
**Kind**: property

Configures the stride, in bytes, between radii in the radius buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var radiusStride: Int { get set }
```

#### Discussion

You are responsible for ensuring this property is set to a multiple of the size corresponding to the [`radiusFormat`](mtl4accelerationstructurecurvegeometrydescriptor/radiusformat.md).

This property defaults to `0` bytes, indicating that the radii are tightly packed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/radiusstride)*