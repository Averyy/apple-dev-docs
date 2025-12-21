# updateMappings(texture:heap:operations:)

**Framework**: Metal  
**Kind**: method

Updates multiple regions within a placement sparse texture to alias specific tiles of a Metal heap.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func updateMappings(texture: any MTLTexture, heap: (any MTLHeap)?, operations: [MTL4UpdateSparseTextureMappingOperation])
```

#### Discussion

You can provide a `nil` parameter to the `heap` argument only if when you perform unmap operations. Otherwise, you are responsible for ensuring the heap is non-nil and has a [`maxCompatiblePlacementSparsePageSize`](mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) of at least the texture’s [`placementSparsePageSize`](mtltexturedescriptor/placementsparsepagesize.md).

When performing a sparse mapping update, you are responsible for issuing a barrier against stage `MTLStageResourceState`.

You can determine the sparse texture tier by calling `MTLTexture/sparseTextureTier`.

## Parameters

- `texture`: A placement sparse  .
- `heap`:   you allocate with type  .
- `operations`: An array of   instances to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/updatemappings(texture:heap:operations:))*