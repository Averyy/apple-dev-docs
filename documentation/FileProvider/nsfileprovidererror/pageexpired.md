# pageExpired

**Framework**: File Provider  
**Kind**: property

An error indicating that the page is too old, and that the system must restart the enumeration operation from the beginning.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var pageExpired: NSFileProviderError.Code { get }
```

## See Also

- [NSFileProviderError.Code](nsfileprovidererror/code.md)
  The error codes for the File Provider extension.
- [static var filenameCollision: NSFileProviderError.Code](nsfileprovidererror/filenamecollision.md)
  An error indicating that an item with the same name already exists in the same directory.
- [static var insufficientQuota: NSFileProviderError.Code](nsfileprovidererror/insufficientquota.md)
  An error indicating that the File Provider extension can’t upload the item because it would push the account over its quota.
- [static var noSuchItem: NSFileProviderError.Code](nsfileprovidererror/nosuchitem.md)
  An error indicating that the specified item doesn’t exist.
- [static var notAuthenticated: NSFileProviderError.Code](nsfileprovidererror/notauthenticated.md)
  An error indicating that you can’t verify the user’s credentials.
- [static var serverUnreachable: NSFileProviderError.Code](nsfileprovidererror/serverunreachable.md)
  An error indicating that the File Provider extension can’t reach the remote server.
- [static var syncAnchorExpired: NSFileProviderError.Code](nsfileprovidererror/syncanchorexpired.md)
  An error indicating that the sync anchor is too old, and that the system must restart the sync operation from the beginning.
- [static var directoryNotEmpty: NSFileProviderError.Code](nsfileprovidererror/directorynotempty.md)
  An error indicating an attempt to nonrecursively delete a directory that isn’t empty.
- [static var providerNotFound: NSFileProviderError.Code](nsfileprovidererror/providernotfound.md)
  An error indicating that the File Provider manager can’t find the specified provider.
- [static var providerTranslocated: NSFileProviderError.Code](nsfileprovidererror/providertranslocated.md)
  An error indicating the File Provider extension is in a disabled state due to Gatekeeper’s restrictions for apps from outside the App Store.
- [static var olderExtensionVersionRunning: NSFileProviderError.Code](nsfileprovidererror/olderextensionversionrunning.md)
  An error indicating that the registered provider in the system is an older version than the one the app uses.
- [static var newerExtensionVersionFound: NSFileProviderError.Code](nsfileprovidererror/newerextensionversionfound.md)
  An error indicating that the registered provider in the system is a newer version than the one the app uses.
- [static var nonEvictable: NSFileProviderError.Code](nsfileprovidererror/nonevictable.md)
  An error indicating that the File Provider extension can’t evict an item.
- [static var nonEvictableChildren: NSFileProviderError.Code](nsfileprovidererror/nonevictablechildren.md)
  An error indicating that the File Provider extension can’t evict a directory because it contains nonevictable items.
- [static var unsyncedEdits: NSFileProviderError.Code](nsfileprovidererror/unsyncededits.md)
  An error indicating that the item contains unsynced changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererror/pageexpired)*