# isHidden

**Framework**: File Provider  
**Kind**: property

A Boolean value that determines whether the domain is visible to users.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isHidden: Bool { get set }
```

#### Discussion

The system stores the files on disk, but it doesn’t display them to the user. For example, you could set this value to [`false`](https://developer.apple.com/documentation/Swift/false) when performing a dry run of a migration.

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
- [var userEnabled: Bool](nsfileproviderdomain/userenabled.md)
  A Boolean value that indicates whether the user has enabled or disabled the domain.
- [var isDisconnected: Bool](nsfileproviderdomain/isdisconnected.md)
  A Boolean value indicating that the domain is present, but disconnected from the file extension.
- [var supportsSyncingTrash: Bool](nsfileproviderdomain/supportssyncingtrash.md)
- [var userInfo: [AnyHashable : Any]?](nsfileproviderdomain/userinfo.md)
- [var volumeUUID: UUID?](nsfileproviderdomain/volumeuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/ishidden)*