# isHidden

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the domain is visible to users.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (assign, readwrite, getter=isHidden) BOOL hidden;
```

#### Discussion

The system stores the files on disk, but it doesn’t display them to the user. For example, you could set this value to [`false`](../../Swift/false.md) when performing a dry run of a migration.

## See Also

### Accessing data
- [var displayName: String](./displayname.md)
  The name of the domain displayed in the user interface.
- [var identifier: NSFileProviderDomainIdentifier](./identifier.md)
  The domain’s unique identifier.
- [var isReplicated: Bool](./isreplicated.md)
- [var backingStoreIdentity: Data?](./backingstoreidentity.md)
  A unique identifier for the backing store used by the system.
- [var pathRelativeToDocumentStorage: String](./pathrelativetodocumentstorage.md)
  The path of the domain’s subdirectory relative to the file provider’s shared container.
- [var userEnabled: Bool](./userenabled.md)
  A Boolean value that indicates whether the user has enabled or disabled the domain.
- [var isDisconnected: Bool](./isdisconnected.md)
  A Boolean value indicating that the domain is present, but disconnected from the file extension.
- [var supportsSyncingTrash: Bool](./supportssyncingtrash.md)
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
- [var volumeUUID: UUID?](./volumeuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/ishidden)*