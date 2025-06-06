# NSFileProviderError.Code

**Framework**: File Provider  
**Kind**: enum

The error codes for the File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error codes
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
- [NSFileProviderError.Code.cannotSynchronize](nsfileprovidererror/code/cannotsynchronize.md)
  An error indicating a failed sync attempt.
- [NSFileProviderError.Code.deletionRejected](nsfileprovidererror/code/deletionrejected.md)
  An error indicating a failed deletion action.
- [NSFileProviderError.Code.versionNoLongerAvailable](nsfileprovidererror/code/versionnolongeravailable.md)
  An error indicating that the specified version is no longer available.
- [NSFileProviderError.Code.domainDisabled](nsfileprovidererror/code/domaindisabled.md)
- [NSFileProviderError.Code.excludedFromSync](nsfileprovidererror/code/excludedfromsync.md)
- [NSFileProviderError.Code.applicationExtensionNotFound](nsfileprovidererror/code/applicationextensionnotfound.md)
  An error indicating that there isn’t an app extension within the app bundle.
- [NSFileProviderError.Code.providerDomainNotFound](nsfileprovidererror/code/providerdomainnotfound.md)
  An error indicating that there isn’t a registered domain for the corresponding identifier.
- [NSFileProviderError.Code.providerDomainTemporarilyUnavailable](nsfileprovidererror/code/providerdomaintemporarilyunavailable.md)
  An error indicating that the system is unable to service requests for the domain temporarily, and you can try again later.
### Initializers
- [init?(rawValue: Int)](nsfileprovidererror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct NSFileProviderError](nsfileprovidererror.md)
  A structure that contains information about File Provider extension errors.
- [let NSFileProviderErrorDomain: String](nsfileprovidererrordomain.md)
  The error domain for the File Provider extension.
- [let NSFileProviderErrorItemKey: String](nsfileprovidererroritemkey.md)
  The key for accessing information about sync-related errors.
- [let NSFileProviderErrorNonExistentItemIdentifierKey: String](nsfileprovidererrornonexistentitemidentifierkey.md)
  The key for accessing the specified item’s identifier when the item doesn’t exist.
- [let NSFileProviderErrorCollidingItemKey: String](nsfileprovidererrorcollidingitemkey.md)
  The key for accessing the existing item from a filename collision error’s user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererror/code)*