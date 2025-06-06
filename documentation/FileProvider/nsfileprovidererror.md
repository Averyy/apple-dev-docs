# NSFileProviderError

**Framework**: File Provider  
**Kind**: struct

A structure that contains information about File Provider extension errors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderError
```

## Topics

### Accessing error codes
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
- [static var pageExpired: NSFileProviderError.Code](nsfileprovidererror/pageexpired.md)
  An error indicating that the page is too old, and that the system must restart the enumeration operation from the beginning.
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
- [static var cannotSynchronize: NSFileProviderError.Code](nsfileprovidererror/cannotsynchronize.md)
  An error indicating a failed sync attempt.
- [static var deletionRejected: NSFileProviderError.Code](nsfileprovidererror/deletionrejected.md)
  An error indicating a failed deletion action.
- [static var versionNoLongerAvailable: NSFileProviderError.Code](nsfileprovidererror/versionnolongeravailable.md)
  An error that indicates whether the specified version is no longer available.
- [static var domainDisabled: NSFileProviderError.Code](nsfileprovidererror/domaindisabled.md)
- [static var excludedFromSync: NSFileProviderError.Code](nsfileprovidererror/excludedfromsync.md)
- [static var applicationExtensionNotFound: NSFileProviderError.Code](nsfileprovidererror/applicationextensionnotfound.md)
  An error indicating that there isn’t an app extension within the app bundle.
- [static var providerDomainNotFound: NSFileProviderError.Code](nsfileprovidererror/providerdomainnotfound.md)
  An error indicating that there isn’t a registered domain for the corresponding identifier.
- [static var providerDomainTemporarilyUnavailable: NSFileProviderError.Code](nsfileprovidererror/providerdomaintemporarilyunavailable.md)
  An error indicating that the system is unable to service requests for the domain temporarily, and you can try again later.
### Type Properties
- [static var errorDomain: String](nsfileprovidererror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSFileProviderError.Code](nsfileprovidererror/code.md)
  The error codes for the File Provider extension.
- [let NSFileProviderErrorDomain: String](nsfileprovidererrordomain.md)
  The error domain for the File Provider extension.
- [let NSFileProviderErrorItemKey: String](nsfileprovidererroritemkey.md)
  The key for accessing information about sync-related errors.
- [let NSFileProviderErrorNonExistentItemIdentifierKey: String](nsfileprovidererrornonexistentitemidentifierkey.md)
  The key for accessing the specified item’s identifier when the item doesn’t exist.
- [let NSFileProviderErrorCollidingItemKey: String](nsfileprovidererrorcollidingitemkey.md)
  The key for accessing the existing item from a filename collision error’s user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererror)*