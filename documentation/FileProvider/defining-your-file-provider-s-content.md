# Defining Your File Provider’s Content

**Framework**: File Provider

Create enumerators to specify your file provider’s content.

#### Overview

An enumerator can provide the content of either a folder or your file provider’s working set.

##### Enumerate a Folder

Create enumerators to specify the content of a folder (for example, your file provider’s root-level folder, or any of its subfolders).

![The flow of information between the document browser and your file provider.](https://docs-assets.developer.apple.com/published/3f792982f80bc99310603bbaa7f36ce0/media-2910270%402x.png)

When the user begins to browse a folder:

1. The system calls your file provider’s [`enumerator(for:)`](nsfileproviderextension/enumerator(for:).md)method and passes the persistent identifier for the folder. If the user is browsing your root-level folder, it passes the [`rootContainer`](nsfileprovideritemidentifier/rootcontainer.md) constant instead.
2. You must instantiate and return an object that adopts the [`NSFileProviderEnumerator`](nsfileproviderenumerator.md) protocol.
3. The system calls the enumerator’s [`enumerateItems(for:startingAt:)`](nsfileproviderenumerator/enumerateitems(for:startingat:).md) method to get the first batch of items from your file provider. This method is asynchronous.
4. Your enumerator gathers information about the first batch of items for the specified folder (perhaps from a remote server).
5. Your enumerator returns the results to the specified observer (an object that adopts the [`NSFileProviderEnumerationObserver`](nsfileproviderenumerationobserver.md) protocol).

- Return the items by calling the observer’s [`didEnumerate(_:)`](nsfileproviderenumerationobserver/didenumerate(_:).md) method.
- Call the observer’s [`finishEnumerating(upTo:)`](nsfileproviderenumerationobserver/finishenumerating(upto:).md) method when the batch is complete.
- If an error occurs, call the observer’s [`finishEnumeratingWithError(_:)`](nsfileproviderenumerationobserver/finishenumeratingwitherror(_:).md) method.

As the user navigates through the items, the system calls [`enumerateItems(for:startingAt:)`](nsfileproviderenumerator/enumerateitems(for:startingat:).md) as needed to fetch additional items. If the user navigates to a new directory, the system calls the file provider’s [`enumerator(for:)`](nsfileproviderextension/enumerator(for:).md) method to create a new enumerator for that directory. The previous enumerator is then invalidated.

##### Create the Working Set and Enumerate Its Content

The working set is a list of items (documents or folders) of particular interest to the user. Your file provider must maintain its own working set. For a consistent experience across file providers, the working set must include all of the following:

- Recent items (items with a last-used date)
- Tagged items
- Favorites
- Shared items
- Recently deleted items

You may add other documents to the working set, if you think they are particularly relevant to the user.

The documents in the working set are indexed in the device’s Spotlight database. The system updates this database as changes are enumerated. It is vital, therefore, that the working sets be kept in sync across all of the user’s devices. Any changes made to the working set must be propagated to all of the user’s devices, and each device must keep a local cache of the working set, letting it enumerate the working set when offline.

Create an enumerator to specify the working set’s content. This enumerator uses the same basic procedure as used for enumerating a folder, with the following exceptions:

- The working set’s enumerator isn’t driven by the user browsing through your file provider’s content. Instead, the system updates the Spotlight database in the background.
- To get the working set enumerator, the system calls the file provider’s [`enumerator(for:)`](nsfileproviderextension/enumerator(for:).md) method and passes in the [`workingSet`](nsfileprovideritemidentifier/workingset.md) constant. You must provide an enumerator that returns all of the items and changes for your working set.
- The system always responds to changes to the working set. If a change arrives and you don’t have an active enumerator, the system requests a new one.

## See Also

- [protocol NSFileProviderEnumerationObserver](nsfileproviderenumerationobserver.md)
  An observer that receives batches of items during enumeration.
- [struct NSFileProviderPage](nsfileproviderpage.md)
  A synchronization point that represents the next batch of items to be returned by an enumerator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/defining-your-file-provider-s-content)*