# isDisconnected

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating that the domain is present, but disconnected from the file extension.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isDisconnected: Bool { get }
```

```objc
@property (readonly, getter=isDisconnected) BOOL disconnected;
```

## Discussion

Users can continue to browse the content from a disconnected domain; however, the File Provider extension no longer sends or receives updates about modifications to the files.

To change the disconnected state, create a new [`NSFileProviderDomain`](../nsfileproviderdomain.md) using the same identifier, and pass it to [`add(_:completionHandler:)`](../nsfileprovidermanager/add%28_,completionhandler%29.md).

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
- [var supportsSyncingTrash: Bool](./supportssyncingtrash.md)
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
- [var volumeUUID: UUID?](./volumeuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/isdisconnected)*