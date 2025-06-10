# radiusStride

**Framework**: Metal  
**Kind**: property

Configures the stride, in bytes, between radii in the radius buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var radiusStride: Int { get set }
```

#### Discussion

You are responsible for ensuring this property is set to a multiple of the size corresponding to the [`radiusFormat`](mtl4accelerationstructurecurvegeometrydescriptor/radiusformat.md).

This property defaults to `0` bytes, indicating that the radii are tightly packed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/radiusstride)*