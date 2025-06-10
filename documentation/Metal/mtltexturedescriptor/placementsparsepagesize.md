# placementSparsePageSize

**Framework**: Metal  
**Kind**: property

Determines the page size for a placement sparse texture.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var placementSparsePageSize: MTLSparsePageSize { get set }
```

#### Discussion

Set this property to a non-zero value to create a .

Placement sparse textures are instances of [`MTLTexture`](mtltexture.md) that you assign memory to using a [`MTLHeap`](mtlheap.md) instance of type [`MTLHeapType.placement`](mtlheaptype/placement.md) and a [`maxCompatiblePlacementSparsePageSize`](mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) at least as large as the [`MTLSparsePageSize`](mtlsparsepagesize.md) value you assign to this property.

This value is 0 by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/placementsparsepagesize)*