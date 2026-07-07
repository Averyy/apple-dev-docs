# NSFileProviderError.Code.domainDisabled

**Framework**: File Provider  
**Kind**: case

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case domainDisabled
```

## See Also

- [NSFileProviderError.Code.filenameCollision](nsfileprovidererror/code/filenamecollision.md)
  An error indicating that an item with the same name already exists in the same directory.
- [NSFileProviderError.Code.insufficientQuota](nsfileprovidererror/code/insufficientquota.md)
  An error indicating that the File Provider extension can’t upload the item because it would push the account over its quota.
- [NSFileProviderError.Code.noSuchItem](nsfileprovidererror/code/nosuchitem.md)
  An error indicating that the specified item doesn’t exist.
- [NSFileProviderError.Code.notAuthenticated](nsfileprovidererror/code/notauthenticated.md)
  An error indicating that you can’t verify the user’s credentials.
- [NSFileProviderError.Code.serverUnreachable](nsfileprovidererror/code/serverunreachable.md)
  An error indicating that the File Provider extension can’t reach the remote server.
- [NSFileProviderError.Code.syncAnchorExpired](nsfileprovidererror/code/syncanchorexpired.md)
  An error indicating that the sync anchor is too old, and that the system must restart the sync operation from the beginning.
- [static var pageExpired: NSFileProviderError.Code](nsfileprovidererror/code/pageexpired.md)
  An error indicating that the page is too old, and that the system must restart the enumeration operation from the beginning.
- [NSFileProviderError.Code.directoryNotEmpty](nsfileprovidererror/code/directorynotempty.md)
  An error indicating an attempt to nonrecursively delete a directory that isn’t empty.
- [NSFileProviderError.Code.providerNotFound](nsfileprovidererror/code/providernotfound.md)
  An error indicating that the File Provider manager can’t find the specified provider.
- [NSFileProviderError.Code.providerTranslocated](nsfileprovidererror/code/providertranslocated.md)
  An error indicating the File Provider extension is in a disabled state due to Gatekeeper’s restrictions for apps from outside the App Store.
- [NSFileProviderError.Code.olderExtensionVersionRunning](nsfileprovidererror/code/olderextensionversionrunning.md)
  An error indicating that the registered provider in the system is an older version than the one the app uses.
- [NSFileProviderError.Code.newerExtensionVersionFound](nsfileprovidererror/code/newerextensionversionfound.md)
  An error indicating that the registered provider in the system is a newer version than the one the app uses.
- [NSFileProviderError.Code.nonEvictable](nsfileprovidererror/code/nonevictable.md)
  An error indicating that the File Provider extension can’t evict an item.
- [NSFileProviderError.Code.nonEvictableChildren](nsfileprovidererror/code/nonevictablechildren.md)
  An error indicating that the File Provider extension can’t evict a directory because it contains nonevictable items.
- [NSFileProviderError.Code.unsyncedEdits](nsfileprovidererror/code/unsyncededits.md)
  An error indicating that the item contains unsynced changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererror/code/domaindisabled)*