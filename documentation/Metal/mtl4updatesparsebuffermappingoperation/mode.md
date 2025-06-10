# mode

**Framework**: Metal  
**Kind**: property

The mode of the mapping operation to perform.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var mode: MTLSparseTextureMappingMode
```

#### Discussion

When mode is [`MTLSparseTextureMappingMode.map`](mtlsparsetexturemappingmode/map.md), Metal walks the tiles in the range in buffer offset order, assigning the next tile from the heap in increasing order, starting at [`heapOffset`](mtl4updatesparsebuffermappingoperation/heapoffset.md).

When mode is [`MTLSparseTextureMappingMode.unmap`](mtlsparsetexturemappingmode/unmap.md), Metal unmaps the tiles in the range, and ignores the value of member [`heapOffset`](mtl4updatesparsebuffermappingoperation/heapoffset.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4updatesparsebuffermappingoperation/mode)*