# radiusBufferOffset

**Framework**: Metal  
**Kind**: property

The offset, in bytes, to the radius data in the buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var radiusBufferOffset: Int { get set }
```

#### Discussion

The offset needs to be a multiple of the radius format you configure with the [`radiusFormat`](mtlaccelerationstructurecurvegeometrydescriptor/radiusformat.md) property. You also need to align the offset to both the radius format’s size and the platform’s buffer alignment requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusbufferoffset)*