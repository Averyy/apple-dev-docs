# supportsDocumentID

**Framework**: FSKit  
**Kind**: property

A Boolean property that indicates whether the volume supports document IDs for document revisions.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportsDocumentID: Bool { get set }
```

#### Discussion

A document ID is an identifier that persists across object ID changes.

## See Also

- [var supportsPersistentObjectIDs: Bool](fsvolume/supportedcapabilities/supportspersistentobjectids.md)
  A Boolean property that indicates whether the volume supports persistent object identifiers and can look up file system objects by their IDs.
- [var supports64BitObjectIDs: Bool](fsvolume/supportedcapabilities/supports64bitobjectids.md)
  A Boolean property that indicates whether the volume supports 64-bit object IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supportsdocumentid)*