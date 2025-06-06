# NSFileProviderPendingSetEnumerator

**Framework**: File Provider  
**Kind**: protocol

A protocol for enumerating pending items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderPendingSetEnumerator : NSFileProviderEnumerator
```

#### Overview

Items are pending when they’ve changed but the File Provider extension hasn’t yet synced the changes. Examples include local changes that the extension hasn’t uploaded to its remote storage and items that the extension has marked as changed in the working set but hasn’t yet downloaded. The system calls [`pendingItemsDidChange(completionHandler:)`](nsfileproviderreplicatedextension/pendingitemsdidchange(completionhandler:).md) and posts a [`NSFileProviderPendingSetDidChange`](nsfileproviderpendingsetdidchange.md) notification whenever the set of pending items changes.

To enumerate items in the pending set, call the [`enumeratorForPendingItems()`](nsfileprovidermanager/enumeratorforpendingitems().md) method, which returns an object that adopts the [`NSFileProviderPendingSetEnumerator`](nsfileproviderpendingsetenumerator.md) protocol.

The pending enumerator lists the items that meet all of the following criteria:

- The system observed a change, either on disk or in the working set.
- The change occurred more than one second ago.
- The File Provider extension hasn’t yet synced the change with its remote storage.

An item can appear in the pending set for many different reasons, including:

- The system is under load and can’t process all the events in a timely manner.
- The system is performing a long-running operation on the item, such as downloading or uploading new content.
- Pending changes to the item have raised an error.

The pending set only contains items that are already known to the File Provider extension and that remain queued for change longer than the system’s refresh interval. A new file in the local storage won’t appear in the pending set, even if the upload to the remote storage takes several minutes to complete.

## Topics

### Accessing Refresh Data
- [var domainVersion: NSFileProviderDomainVersion?](nsfileproviderpendingsetenumerator/domainversion.md)
  The domain version when the system last refreshed the pending set.
- [var refreshInterval: TimeInterval](nsfileproviderpendingsetenumerator/refreshinterval.md)
  The amount of time, in seconds, between updates to the pending set.
### Instance Properties
- [var isMaximumSizeReached: Bool](nsfileproviderpendingsetenumerator/ismaximumsizereached.md)

## Relationships

### Inherits From
- [NSFileProviderEnumerator](nsfileproviderenumerator.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSFileProviderReplicatedExtension](nsfileproviderreplicatedextension.md)
  A File Provider extension in which the system replicates the contents on disk.
- [protocol NSFileProviderEnumerating](nsfileproviderenumerating.md)
  Support for enumerating the file provider’s contents.
- [protocol NSFileProviderIncrementalContentFetching](nsfileproviderincrementalcontentfetching.md)
  Support for fetching changes to the item’s content.
- [protocol NSFileProviderPartialContentFetching](nsfileproviderpartialcontentfetching.md)
  Support for fetching part of a file’s content.
- [protocol NSFileProviderServicing](nsfileproviderservicing.md)
  Support for providing a custom service source.
- [protocol NSFileProviderCustomAction](nsfileprovidercustomaction.md)
  Support for custom actions.
- [struct NSFileProviderExtensionActionIdentifier](nsfileproviderextensionactionidentifier.md)
  An identifier for custom actions.
- [protocol NSFileProviderThumbnailing](nsfileproviderthumbnailing.md)
  Support for item thumbnails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderpendingsetenumerator)*