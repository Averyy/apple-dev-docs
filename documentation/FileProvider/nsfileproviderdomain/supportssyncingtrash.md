# supportsSyncingTrash

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 13.0+
- visionOS 2.0+

## Declaration

```swift
var supportsSyncingTrash: Bool { get set }
```

```objc
@property (assign, readwrite) BOOL supportsSyncingTrash;
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
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
- [var volumeUUID: UUID?](./volumeuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/supportssyncingtrash)*