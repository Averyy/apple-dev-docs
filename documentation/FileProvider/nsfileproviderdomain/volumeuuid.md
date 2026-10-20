# volumeUUID

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 15.0+

## Declaration

```swift
var volumeUUID: UUID? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSUUID * volumeUUID;
```

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
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines whether the domain is visible to users.
- [var userEnabled: Bool](./userenabled.md)
  A Boolean value that indicates whether the user has enabled or disabled the domain.
- [var isDisconnected: Bool](./isdisconnected.md)
  A Boolean value indicating that the domain is present, but disconnected from the file extension.
- [var supportsSyncingTrash: Bool](./supportssyncingtrash.md)
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/volumeuuid)*