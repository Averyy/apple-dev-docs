# maxCompatiblePlacementSparsePageSize

**Framework**: Metal  
**Kind**: property

Specifies the largest sparse page size that the Metal heap supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maxCompatiblePlacementSparsePageSize: MTLSparsePageSize { get set }
```

#### Discussion

This parameter only affects the heap if you set the [`type`](mtlheapdescriptor/type.md) property of this descriptor to [`MTLHeapType.placement`](mtlheaptype/placement.md).

The value you assign to this property determines the compatibility of the Metal heap with with placement sparse resources, because placement sparse resources require that their sparse page size be less than or equal to the placement sparse page of the Metal heap that this property controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor/maxcompatibleplacementsparsepagesize)*