# Content and Change Tracking

**Framework**: File Provider

Create enumerators to specify your file provider’s content, and track changes to that content.

#### Overview

To display your file provider’s items to the user, you tell the system about those items and any changes to their contents. You do this by providing enumerators.

To provide an enumerator, create a class that adopts the [`NSFileProviderEnumerator`](nsfileproviderenumerator.md) protocol. The system uses this enumerator to represent an item (a folder or a document) managed by your file provider. In addition, the system uses the enumerator to track any changes to the item.

The system also uses an enumerator to track the working set (a set of special items like Recents or Favorites).

You create enumerators to handle these use cases:

| When… | You are passed… | Your enumerator returns… |
| --- | --- | --- |
| The user begins browsing your file provider’s content | The [`rootContainer`](nsfileprovideritemidentifier/rootcontainer.md) constant | The content of your file provider’s root directory, and any changes to that content |
| The user opens a new folder while browsing your file provider’s content | The folder’s persistent identifier | The content of the specified folder, and any changes to its content |
| The user opens a document from your file provider | The document’s persistent identifier | Changes to the open document |
| The system is alerted to changes to the working set | The [`workingSet`](nsfileprovideritemidentifier/workingset.md) constant | The content of your working set, and any changes to that content |

Once requested, an enumerator provides both the content and any changes for an item. When the system stops accessing the item, it calls the enumerator’s [`invalidate()`](nsfileproviderenumerator/invalidate().md) method. For example, if you return an enumerator that provides the content of a directory, as long as the enumerator is active, the system also uses it to enumerate changes to the directory.

The system may have multiple, active enumerators for different items. Some of these may represent items that are currently displayed on screen. Others may be items that are no longer displayed, but the system has retained the enumerator for performance reasons. You need to inform the system of any changes to the content managed by any of the active enumerators, as well as any changes to the working set (whether or not it has an active enumerator).

## Topics

### Essentials
- [protocol NSFileProviderEnumerator](nsfileproviderenumerator.md)
  A protocol for enumerating items and changes.
### Content
- [Defining Your File Provider’s Content](defining-your-file-provider-s-content.md)
  Create enumerators to specify your file provider’s content.
- [protocol NSFileProviderEnumerationObserver](nsfileproviderenumerationobserver.md)
  An observer that receives batches of items during enumeration.
- [struct NSFileProviderPage](nsfileproviderpage.md)
  A synchronization point that represents the next batch of items to be returned by an enumerator.
### Change Tracking
- [Tracking Your File Provider’s Changes](tracking-your-file-provider-s-changes.md)
  Create an enumerator to track changes to your file provider’s content.
- [protocol NSFileProviderChangeObserver](nsfileproviderchangeobserver.md)
  An observer that receives changes and deletions during enumeration.
- [struct NSFileProviderSyncAnchor](nsfileprovidersyncanchor.md)
  A synchronization point that represents the last batch of changes returned by the enumerator.

## See Also

- [class NSFileProviderExtension](nsfileproviderextension.md)
  The principal class for the nonreplicated File Provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/content-and-change-tracking)*