# radiusStride

**Framework**: Metal  
**Kind**: property

The stride, in bytes, between the radius elements in the radius buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var radiusStride: Int { get set }
```

#### Discussion

The stride needs to be a multiple of the radius format size you configure with the [`radiusFormat`](mtlaccelerationstructurecurvegeometrydescriptor/radiusformat.md) property. The default value is `0`, which indicates that the radius elements in the buffer have zero bytes of padding between them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusstride)*