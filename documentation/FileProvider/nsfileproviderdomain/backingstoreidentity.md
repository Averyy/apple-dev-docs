# backingStoreIdentity

**Framework**: File Provider  
**Kind**: property

A unique identifier for the backing store used by the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var backingStoreIdentity: Data? { get }
```

#### Discussion

Changes to this identifier indicate that the system has dropped its backing store and is creating a new one. The system may create a new backing store if the old store becomes corrupted. The file provider extension can also request a new backing store by calling [`reimportItems(below:completionHandler:)`](nsfileprovidermanager/reimportitems(below:completionhandler:).md).

While rebuilding the backing store, the system invalidates any extension instances associated with the domain. As a result, the system guarantees that the [`backingStoreIdentity`](nsfileproviderdomain/backingstoreidentity.md) remains stable throughout the lifetime of an [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) instance.

> **Note**:  This property is only available on file provider extensions based on the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) protocol.

## See Also

- [var displayName: String](nsfileproviderdomain/displayname.md)
  The name of the domain displayed in the user interface.
- [var identifier: NSFileProviderDomainIdentifier](nsfileproviderdomain/identifier.md)
  The domain’s unique identifier.
- [var isReplicated: Bool](nsfileproviderdomain/isreplicated.md)
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
- [var volumeUUID: UUID?](nsfileproviderdomain/volumeuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/backingstoreidentity)*