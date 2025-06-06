# volumeUUID

**Framework**: File Provider  
**Kind**: property

**Availability**:
- macOS 15.0+

## Declaration

```swift
var volumeUUID: UUID? { get }
```

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
- [var isDisconnected: Bool](nsfileproviderdomain/isdisconnected.md)
  A Boolean value indicating that the domain is present, but disconnected from the file extension.
- [var supportsSyncingTrash: Bool](nsfileproviderdomain/supportssyncingtrash.md)
- [var userInfo: [AnyHashable : Any]?](nsfileproviderdomain/userinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/volumeuuid)*