# NSFileProviderError.Code.nonEvictable

**Framework**: File Provider  
**Kind**: case  
**Role**: Case

An error indicating that the File Provider extension can’t evict an item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
case nonEvictable
```

```c
NSFileProviderErrorNonEvictable
```

#### Discussion

The [`NSFileProviderManager`](../../nsfileprovidermanager.md) throws this error when you attempt to evict an item that doesn’t have the [`allowsEvicting`](../../nsfileprovideritemcapabilities/allowsevicting.md) capability. The system sets the error’s [`NSURLErrorKey`](../../../Foundation/nsurlerrorkey.md) to the URL of the item that the error affects.

## See Also

### Error codes
- [NSFileProviderError.Code.filenameCollision](./filenamecollision.md)
  An error indicating that an item with the same name already exists in the same directory.
- [NSFileProviderError.Code.insufficientQuota](./insufficientquota.md)
  An error indicating that the File Provider extension can’t upload the item because it would push the account over its quota.
- [NSFileProviderError.Code.noSuchItem](./nosuchitem.md)
  An error indicating that the specified item doesn’t exist.
- [NSFileProviderError.Code.notAuthenticated](./notauthenticated.md)
  An error indicating that you can’t verify the user’s credentials.
- [NSFileProviderError.Code.serverUnreachable](./serverunreachable.md)
  An error indicating that the File Provider extension can’t reach the remote server.
- [NSFileProviderError.Code.syncAnchorExpired](./syncanchorexpired.md)
  An error indicating that the sync anchor is too old, and that the system must restart the sync operation from the beginning.
- [static var pageExpired: NSFileProviderError.Code](./pageexpired.md)
  An error indicating that the page is too old, and that the system must restart the enumeration operation from the beginning.
- [NSFileProviderError.Code.directoryNotEmpty](./directorynotempty.md)
  An error indicating an attempt to nonrecursively delete a directory that isn’t empty.
- [NSFileProviderError.Code.providerNotFound](./providernotfound.md)
  An error indicating that the File Provider manager can’t find the specified provider.
- [NSFileProviderError.Code.providerTranslocated](./providertranslocated.md)
  An error indicating the File Provider extension is in a disabled state due to Gatekeeper’s restrictions for apps from outside the App Store.
- [NSFileProviderError.Code.olderExtensionVersionRunning](./olderextensionversionrunning.md)
  An error indicating that the registered provider in the system is an older version than the one the app uses.
- [NSFileProviderError.Code.newerExtensionVersionFound](./newerextensionversionfound.md)
  An error indicating that the registered provider in the system is a newer version than the one the app uses.
- [NSFileProviderError.Code.nonEvictableChildren](./nonevictablechildren.md)
  An error indicating that the File Provider extension can’t evict a directory because it contains nonevictable items.
- [NSFileProviderError.Code.unsyncedEdits](./unsyncededits.md)
  An error indicating that the item contains unsynced changes.
- [NSFileProviderError.Code.cannotSynchronize](./cannotsynchronize.md)
  An error indicating a failed sync attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererror/code/nonevictable)*