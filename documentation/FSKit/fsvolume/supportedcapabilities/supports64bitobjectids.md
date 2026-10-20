# supports64BitObjectIDs

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates whether the volume supports 64-bit object IDs.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supports64BitObjectIDs: Bool { get set }
```

```objc
@property (nonatomic) BOOL supports64BitObjectIDs;
```

## See Also

### Declaring identifier capabilities
- [var supportsPersistentObjectIDs: Bool](./supportspersistentobjectids.md)
  A Boolean property that indicates whether the volume supports persistent object identifiers and can look up file system objects by their IDs.
- [var supportsDocumentID: Bool](./supportsdocumentid.md)
  A Boolean property that indicates whether the volume supports document IDs for document revisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/supports64bitobjectids)*