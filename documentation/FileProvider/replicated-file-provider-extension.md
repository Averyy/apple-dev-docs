# Replicated File Provider extension

**Framework**: Fileprovider

Build a File Provider extension that syncs the local copies of your files with your remote storage.

#### Overview

When creating a replicated File Provider extension, the system takes responsibility for managing and storing the local copies of your documents and folders. Your extension syncs data between the local copy and the remote storage, providing the local system with the metadata and contents of the items in your remote storage. It also alerts the system to any remote changes to those items and uploads any local changes back to the remote storage. For more information, see [`Synchronizing the File Provider Extension`](synchronizing-the-file-provider-extension.md).

At a minimum, the File Provider extension needs to perform the following:

- Adopt both the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) and the [`NSFileProviderEnumerating`](nsfileproviderenumerating.md) protocols. You can add additional features by implementing the other protocols listed in the File Provider protocols listed below.
- Implement an object that adopts the [`NSFileProviderEnumerator`](nsfileproviderenumerator.md) protocol to enumerate the items from your remote storage when the system calls your [`enumerator(for:request:)`](nsfileproviderenumerating/enumerator(for:request:).md) method.
- Implement a class that adopts the [`NSFileProviderItemVersion`](nsfileprovideritemversion.md) protocol to represent the items (directories and files) enumerated by your file provider.

> **Note**:  The system uses two different enumerators. The first lets the system enumerate items from your remote storage. The second lets your app enumerate the items stored locally by the system. You must implement the first enumerator, returning it when the system calls your [`enumerator(for:request:)`](nsfileproviderenumerating/enumerator(for:request:).md) method. The system provides the second enumerator when you call methods like the [`NSFileProviderManager`](nsfileprovidermanager.md) class’s [`enumeratorForMaterializedItems()`](nsfileprovidermanager/enumeratorformaterializeditems().md) method.

Your File Provider extension can add custom actions to the file browser’s context menu using the [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI) framework. You can also define custom services to communicate with the host app using [`NSFileProviderService`](https://developer.apple.com/documentation/Foundation/NSFileProviderService). Use these interfaces to add features that aren’t provided by the base API.

## Topics

### Essentials
- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)
  Keep the local and remote copies of your File Provider extension’s content in sync.
- [Synchronizing files using file provider extensions](synchronizing-files-using-file-provider-extensions.md)
  Make remote files available in macOS and iOS, and synchronize their states by using file provider extensions.
- [Setting the Finder Sidebar Icon](setting-the-finder-sidebar-icon.md)
  Specify a standard or custom symbol as a sidebar icon.
### File Provider protocols
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
- [protocol NSFileProviderPendingSetEnumerator](nsfileproviderpendingsetenumerator.md)
  A protocol for enumerating pending items.
### Items and metadata
- [struct NSFileProviderItemFields](nsfileprovideritemfields.md)
  Fields that specify which of the item’s properties have changed.
- [class NSFileProviderItemVersion](nsfileprovideritemversion.md)
  The version of the item’s content and its metadata.
- [class NSFileProviderRequest](nsfileproviderrequest.md)
  An object that provides information about the application requesting data from the File Provider extension.
- [protocol NSFileProviderItemDecorating](nsfileprovideritemdecorating.md)
  Support for decorating items.
- [struct NSFileProviderItemDecorationIdentifier](nsfileprovideritemdecorationidentifier.md)
  A decoration identifier defined in the File Provider extension’s information property list.
### Domains
- [class NSFileProviderDomainVersion](nsfileproviderdomainversion.md)
  An opaque object that identifies a specific version of a domain.
- [protocol NSFileProviderDomainState](nsfileproviderdomainstate.md)
  An object that contains global state data about the domain.
### Testing protocols
- [protocol NSFileProviderTestingChildrenEnumeration](nsfileprovidertestingchildrenenumeration.md)
  An operation that lists a directory’s content.
- [protocol NSFileProviderTestingCollisionResolution](nsfileprovidertestingcollisionresolution.md)
  An operation that resolves a collision by renaming the new item.
- [protocol NSFileProviderTestingContentFetch](nsfileprovidertestingcontentfetch.md)
  An operation that fetches an item’s content.
- [protocol NSFileProviderTestingCreation](nsfileprovidertestingcreation.md)
  An operation that syncs the creation of the source item to the target location.
- [protocol NSFileProviderTestingDeletion](nsfileprovidertestingdeletion.md)
  An operation that syncs the deletion of the source item to the target location.
- [protocol NSFileProviderTestingIngestion](nsfileprovidertestingingestion.md)
  An operation that alerts the system to either local or remote storage changes.
- [protocol NSFileProviderTestingLookup](nsfileprovidertestinglookup.md)
  An operation that looks up an item.
- [protocol NSFileProviderTestingModification](nsfileprovidertestingmodification.md)
  An operation that syncs the modification of the source item to the target location.
- [protocol NSFileProviderTestingOperation](nsfileprovidertestingoperation.md)
  An operation that the system can schedule.
- [protocol NSFileProviderUserInteractionSuppressing](nsfileprovideruserinteractionsuppressing.md)
  Support for suppressing user-interaction alerts.
- [enum NSFileProviderTestingOperationSide](nsfileprovidertestingoperationside.md)
  The location where the operation takes place.
- [enum NSFileProviderTestingOperationType](nsfileprovidertestingoperationtype.md)
  The action that an operation performs.
- [com.apple.developer.fileprovider.testing-mode](../BundleResources/Entitlements/com.apple.developer.fileprovider.testing-mode.md)
  A Boolean value that indicates whether you can place domains in testing mode.
### Information property list keys
- [NSDownloadsUbiquitousContents](../BundleResources/Information-Property-List/NSDownloadsUbiquitousContents.md)
  A Boolean value that indicates whether the system should download documents before handing them over to the app.
- [com.apple.developer.fileprovider.testing-mode](../BundleResources/Entitlements/com.apple.developer.fileprovider.testing-mode.md)
  A Boolean value that indicates whether you can place domains in testing mode.
- [CFBundleSymbolName](../BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon/CFBundleSymbolName.md)
  The name of the symbol to show in the action sheet, and in Finder’s sidebar on macOS.

## See Also

- [Nonreplicated File Provider extension](nonreplicated-file-provider-extension.md)
  Build a File Provider extension that hosts and manages the user’s local files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FileProvider/replicated-file-provider-extension)*