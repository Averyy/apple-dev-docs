# indexType

**Framework**: Metal  
**Kind**: property

The size of each index in the index buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var indexType: MTLIndexType { get set }
```

#### Discussion

Set this property to a value that reflects the size of the indices in the [`indexBuffer`](mtlaccelerationstructurecurvegeometrydescriptor/indexbuffer.md) property, such as [`MTLIndexType.uint16`](mtlindextype/uint16.md) or [`MTLIndexType.uint32`](mtlindextype/uint32.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/indextype)*