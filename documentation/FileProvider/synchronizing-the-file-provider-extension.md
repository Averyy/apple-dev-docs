# Synchronizing the File Provider Extension

**Framework**: File Provider

Keep the local and remote copies of your File Provider extension’s content in sync.

#### Overview

The system manages a local copy of the items—both documents and folders—stored on your file provider’s remote storage. The local copy can contain either  or  copies of these items. A dataless copy just stores the information needed to display the item in the UI, while a materialized copy includes the item’s content.

For documents, a dataless copy means the system just saves the item’s metadata—such as its name, file size, and last used date—while a materialized document includes both the metadata and the content. For folders, the situation is somewhat more abstract. For a dataless folder, the system knows the folder exists, but it hasn’t enumerated its content yet. If the user opens the folder, the system needs to enumerate the content before displaying it to the user. A materialized folder means the system has already enumerated the folder. Therefore, it has either a dataless or a materialized copy of every item in the folder and can display the folder’s content without requiring any additional information.

The system uses dataless copies where possible to preserve both disk space and bandwidth. However, users can open materialized copies immediately, without requiring additional access to your remote storage. It’s important, therefore, to keep materialized copies of any items the user is likely to access frequently or when they’re offline. For more information, see Specify the Working Set in  [`Synchronizing the File Provider Extension`](synchronizing-the-file-provider-extension.md).

##### Provide Content From Your Remote Server

The system communicates with your extension whenever it needs additional information about the contents of your remote storage. For example, whenever the user opens a new folder, the system calls [`enumerator(for:request:)`](nsfileproviderenumerating/enumerator(for:request:).md) to populate that folder.

In response, your file provider must create an object that adopts the [`NSFileProviderEnumerator`](nsfileproviderenumerator.md) protocol. This object then provides the contents of the container specified by the method’s `containerItemIdentifier` parameter. The container can be your file provider’s root folder, one of its subfolders, its trash, or its _working set—_a set of files particularly relevant to the user.

As the system receives the content, it saves a dataless copy of each item, based on the metadata contained in the [`NSFileProviderItemProtocol`](nsfileprovideritemprotocol.md) objects provided by your enumerator.

The system can also convert dataless copies to materialized copies, as needed. For example, if the user opens a dataless file, the system calls [`fetchContents(for:version:request:completionHandler:)`](nsfileproviderreplicatedextension/fetchcontents(for:version:request:completionhandler:).md) and saves the file’s content. For a dataless folder, the system calls [`enumerator(for:request:)`](nsfileproviderenumerating/enumerator(for:request:).md) to enumerate the folder’s content.

The system typically requests information as a response to either user actions or updates from your remote storage. However, it can also enumerate your file provider’s content or materialize items as needed. For example, the system can enumerate and materialize the content of your working set in the background, so that Spotlight can index it. It can also convert materialized items back into dataless items to free disk space.

> **Note**:  To avoid possible data loss, the system won’t convert a materialized item into a dataless item if the item has pending changes that the File Provider extension needs to sync.

##### Specify the Working Set

The working set is a list of items that the user may find particularly interesting. Your file provider must maintain its own working set. For a consistent experience across file providers, the working set typically includes the following:

- Recently used items
- Tagged items
- Favorites
- Shared items
- Recently deleted items

You may add other documents or folders to the working set, if you think they’re particularly relevant to the user. To provide a consistent view of the user’s data, propagate any changes to the working set across all of the user’s devices.

To ensure that the system applies remote updates to local copies, the working set must also include all materialized items managed by the system when using a replicated file provider. If your file provider doesn’t explicitly track materialized items, the working set must include all items (documents and directories) on your remote storage.

To access the working set, the system calls your File Provider extension’s [`enumerator(for:request:)`](nsfileproviderenumerating/enumerator(for:request:).md) method, passing [`workingSet`](nsfileprovideritemidentifier/workingset.md) as the container identifier. You must provide an enumerator that returns all of the items and changes for your working set.

Unlike other containers, the user doesn’t drive the enumeration of the working set as they browse through your file provider’s content. Instead, the system typically updates the working set as needed in the background. The system saves materialized copies of the working set’s content—letting the user access the content when offline. The device’s Spotlight database also indexes the working set’s contents. The system updates the Spotlight database whenever you notify it of changes to the working set.

##### Track Materialized Items

When a remote update occurs, your file provider only needs to alert the system if the item or its parent are in the working set. To optimize remote updates, your File Provider extension can track items as the system materializes them or renders them dataless, adding or removing those items from the working set. If you don’t track the materialized items, your working set must include all items on your remote storage, and you must alert the system to all changes.

The system calls your file provider’s [`materializedItemsDidChange(completionHandler:)`](nsfileproviderreplicatedextension/materializeditemsdidchange(completionhandler:).md) method and posts a [`NSFileProviderMaterializedSetDidChange`](nsfileprovidermaterializedsetdidchange.md) notification when it materializes a new item or when it renders a materialized item dataless. Your file provider must then enumerate the changes by calling [`enumeratorForMaterializedItems()`](nsfileprovidermanager/enumeratorformaterializeditems().md) on the file provider manager for the corresponding domain, and use the provided enumerator to access the changes since the previous sync anchor. Update your working set based on these changes.

##### Update the Local Copy

When the user, an app, or some other event creates, modifies, or deletes an item on your remote storage, your File Provider extension should check the working set to determine whether you need to signal an update. If your file provider doesn’t track materialized items, the working set includes all items on your remote storage, and you must signal an update for every change.

For file providers that track the materialized items, check whether the item’s [`itemIdentifier`](nsfileprovideritemprotocol/itemidentifier.md) or [`parentItemIdentifier`](nsfileprovideritemprotocol/parentitemidentifier.md) is in the working set. If you find a matching identifier, signal an update for that identifier:

- Call the [`NSFileProviderManager`](nsfileprovidermanager.md) class’s [`signalEnumerator(for:completionHandler:)`](nsfileprovidermanager/signalenumerator(for:completionhandler:).md) method to notify the system of the change. Pass the matching identifier as the `containerItemIdentifier` property.
- Call [`signalEnumerator(for:completionHandler:)`](nsfileprovidermanager/signalenumerator(for:completionhandler:).md) a second time. Pass the [`workingSet`](nsfileprovideritemidentifier/workingset.md) constant as the `containerItemIdentifier` property. This tells the system to update the working set.

When moving an item, check both its new and old [`parentItemIdentifier`](nsfileprovideritemprotocol/parentitemidentifier.md). If the old [`parentItemIdentifier`](nsfileprovideritemprotocol/parentitemidentifier.md) is in the working set, signal a change for the new [`parentItemIdentifier`](nsfileprovideritemprotocol/parentitemidentifier.md), even if the new parent isn’t in the working set.

Alternatively, instead of having your File Provider extension call [`signalEnumerator(for:completionHandler:)`](nsfileprovidermanager/signalenumerator(for:completionhandler:).md), your remote storage can signal an update directly by sending a push notification to the device. For more information, see [`Using push notifications to signal changes`](using-push-notifications-to-signal-changes.md).

## See Also

- [Synchronizing files using file provider extensions](synchronizing-files-using-file-provider-extensions.md)
  Make remote files available in macOS and iOS, and synchronize their states by using file provider extensions.
- [Setting the Finder Sidebar Icon](setting-the-finder-sidebar-icon.md)
  Specify a standard or custom symbol as a sidebar icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/synchronizing-the-file-provider-extension)*