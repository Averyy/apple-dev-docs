# isDisconnected

**Framework**: File Provider  
**Kind**: property

A Boolean value indicating that the domain is present, but disconnected from the file extension.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isDisconnected: Bool { get }
```

#### Discussion

Users can continue to browse the content from a disconnected domain; however, the File Provider extension no longer sends or receives updates about modifications to the files.

To change the disconnected state, create a new [`NSFileProviderDomain`](nsfileproviderdomain.md) using the same identifier, and pass it to [`add(_:completionHandler:)`](nsfileprovidermanager/add(_:completionhandler:).md).

## See Also

- [var displayName: String](nsfileproviderdomain/displayname.md)
  The name of the domain displayed in the user interface.
- [var identifier: NSFileProviderDomainIdentifier](nsfileproviderdomain/identifier.md)
  The domain’s unique identifier.
- [var isReplicated: Bool](nsfileproviderdomain/isreplicated.md)
- [var backingStoreIdentity: Data?](nsfileproviderdomain/backingstoreidentity.md)
  A unique identifier for the backing store used by the system.
- [var pathRelativeToDocumentStorage: String](nsfileproviderdomain/pathrelativetodocumentstorage.md)
  The path of the domain’s subdirectory relative to the file provider’s shared container.
- [var isHidden: Bool](nsfileproviderdomain/ishidden.md)
  A Boolean value that determines whether the domain is visible to users.
- [var userEnabled: Bool](nsfileproviderdomain/userenabled.md)
  A Boolean value that indicates whether the user has enabled or disabled the domain.
- [var supportsSyncingTrash: Bool](nsfileproviderdomain/supportssyncingtrash.md)
- [var userInfo: [AnyHashable : Any]?](nsfileproviderdomain/userinfo.md)
- [var volumeUUID: UUID?](nsfileproviderdomain/volumeuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/isdisconnected)*