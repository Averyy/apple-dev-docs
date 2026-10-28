# userEnabled

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user has enabled or disabled the domain.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var userEnabled: Bool { get }
```

```objc
@property (readonly) BOOL userEnabled;
```

## Discussion

By default, the property is [`true`](../../Swift/true.md); however, If the user disables the domain in the System Preferences, the property is [`false`](../../Swift/false.md).

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
- [var isDisconnected: Bool](./isdisconnected.md)
  A Boolean value indicating that the domain is present, but disconnected from the file extension.
- [var supportsSyncingTrash: Bool](./supportssyncingtrash.md)
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
- [var volumeUUID: UUID?](./volumeuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/userenabled)*