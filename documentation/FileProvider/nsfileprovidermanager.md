# NSFileProviderManager

**Framework**: File Provider  
**Kind**: class

A manager object that you use to communicate with the file provider from either your app or your File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderManager
```

## Mentions

- [Signaling Changes for User-Driven Actions](signaling-changes-for-user-driven-actions.md)
- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)

## Topics

### Accessing File Provider data
- [class var `default`: NSFileProviderManager](nsfileprovidermanager/default.md)
  A property that returns the shared file provider manager object.
- [var documentStorageURL: URL](nsfileprovidermanager/documentstorageurl.md)
  The root URL for all shared documents.
- [var providerIdentifier: String](nsfileprovidermanager/provideridentifier.md)
  A purpose identifier for coordinated reads and writes.
### Translating user-visible URLs
- [func getUserVisibleURL(for: NSFileProviderItemIdentifier, completionHandler: (URL?, (any Error)?) -> Void)](nsfileprovidermanager/getuservisibleurl(for:completionhandler:).md)
  Returns the user-visible URL for an item.
- [class func getIdentifierForUserVisibleFile(at: URL, completionHandler: (NSFileProviderItemIdentifier?, NSFileProviderDomainIdentifier?, (any Error)?) -> Void)](nsfileprovidermanager/getidentifierforuservisiblefile(at:completionhandler:).md)
  Returns the identifier and domain for a user-visible URL.
### Working with items
- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/reimportitems(below:completionhandler:).md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/evictitem(identifier:completionhandler:).md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:).md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:completionhandler:).md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestmodification(of:foritemwithidentifier:options:completionhandler:).md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](nsfileprovidermanager/enumeratorformaterializeditems.md)
  Returns an enumerator for all the items the system currently stores on disk.
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](nsfileprovidermanager/enumeratorforpendingitems.md)
  Returns an enumerator for the set of pending items.
### Performing actions
- [class func placeholderURL(for: URL) -> URL](nsfileprovidermanager/placeholderurl(for:).md)
  Returns a placeholder URL for a given document URL.
- [class func writePlaceholder(at: URL, withMetadata: NSFileProviderItem) throws](nsfileprovidermanager/writeplaceholder(at:withmetadata:).md)
  Writes a document placeholder with the provided metadata.
- [func register(URLSessionTask, forItemWithIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/register(_:foritemwithidentifier:completionhandler:).md)
  Registers the URL session task responsible for the specified item.
- [func signalEnumerator(for: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/signalenumerator(for:completionhandler:).md)
  Alerts the system to changes in the specified folder’s content.
- [func waitForChanges(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/waitforchanges(below:completionhandler:).md)
  Requests a notification after the system completes all the specified changes.
- [func globalProgress(for: Progress.FileOperationKind) -> Progress](nsfileprovidermanager/globalprogress(for:).md)
  Returns a progress object that tracks either the uploading or downloading of items from the File Provider extension’s remote storage.
### Working with domains
- [convenience init?(for: NSFileProviderDomain)](nsfileprovidermanager/init(for:).md)
  Returns a newly created file provider manager for the specified domain.
- [class func `import`(NSFileProviderDomain, fromDirectoryAt: URL, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/import(_:fromdirectoryat:completionhandler:).md)
  Creates a new domain that takes ownership of on-disk data that your app previously managed without a file provider.
- [class func add(NSFileProviderDomain, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/add(_:completionhandler:).md)
  Adds a domain to the File Provider extension.
- [class func getDomainsWithCompletionHandler(([NSFileProviderDomain], (any Error)?) -> Void)](nsfileprovidermanager/getdomainswithcompletionhandler(_:).md)
  Returns all of the File Provider extension’s domains.
- [class func remove(NSFileProviderDomain, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/remove(_:completionhandler:).md)
  Removes a domain from the File Provider extension.
- [class func remove(NSFileProviderDomain, mode: NSFileProviderManager.DomainRemovalMode, completionHandler: (URL?, (any Error)?) -> Void)](nsfileprovidermanager/remove(_:mode:completionhandler:).md)
  Removes a domain from the File Provider extension using the specified options.
- [class func removeAllDomains(completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/removealldomains(completionhandler:).md)
  Removes all domains from the File Provider extension.
- [NSFileProviderManager.DomainRemovalMode](nsfileprovidermanager/domainremovalmode.md)
  A mode indicating how the system handles user data when removing a domain.
- [func disconnect(reason: String, options: NSFileProviderManager.DisconnectionOptions, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/disconnect(reason:options:completionhandler:).md)
  Disconnects the domain from the extension.
- [NSFileProviderManager.DisconnectionOptions](nsfileprovidermanager/disconnectionoptions.md)
  Options for disconnecting a domain from the extension.
- [func reconnect(completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/reconnect(completionhandler:).md)
  Reconnects the domain with the extension.
- [func waitForStabilization(completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/waitforstabilization(completionhandler:).md)
  Requests a notification after the domain stabilizes.
- [func temporaryDirectoryURL() throws -> URL](nsfileprovidermanager/temporarydirectoryurl.md)
  Returns the URL of a directory that the File Provider extension can use to temporarily store files before passing them to the system.
### Syncing Desktop and Documents folders
- [func claimKnownFolders(NSFileProviderKnownFolderLocations, localizedReason: String, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/claimknownfolders(_:localizedreason:completionhandler:).md)
  Asks the domain to sync the specified known folders.
- [func releaseKnownFolders(NSFileProviderKnownFolders, localizedReason: String, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/releaseknownfolders(_:localizedreason:completionhandler:).md)
  Asks the system to stop replicating the specified known folders in the domain.
- [struct NSFileProviderKnownFolders](nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [class NSFileProviderKnownFolderLocations](nsfileproviderknownfolderlocations.md)
  A class for working with known-folder locations.
- [protocol NSFileProviderKnownFolderSupporting](nsfileproviderknownfoldersupporting.md)
  A protocol that defines the interface for sharing known-folder locations with the system.
### Working with external volumes
- [func stateDirectoryURL() throws -> URL](nsfileprovidermanager/statedirectoryurl.md)
  Returns a URL for a directory for storing state information for the domain.
- [class func checkDomainsCanBeStoredOnVolume(at: URL) throws -> NSFileProviderManager.EligibilityResult](nsfileprovidermanager/checkdomainscanbestoredonvolume(at:).md)
  Checks whether the specified URL is eligible for storing a domain.
- [NSFileProviderManager.EligibilityResult](nsfileprovidermanager/eligibilityresult.md)
  Constants that specify whether a URL is eligible for storing a domain.
- [protocol NSFileProviderExternalVolumeHandling](nsfileproviderexternalvolumehandling.md)
  A protocol that defines the interface for handling external volumes.
### Using services
- [func getService(named: NSFileProviderServiceName, for: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderService?, (any Error)?) -> Void)](nsfileprovidermanager/getservice(named:for:completionhandler:).md)
### Testing
- [func listAvailableTestingOperations() throws -> [any NSFileProviderTestingOperation]](nsfileprovidermanager/listavailabletestingoperations.md)
  Lists all the operations that are ready for scheduling.
- [func run([any NSFileProviderTestingOperation]) throws -> [AnyHashable : any Error]](nsfileprovidermanager/run(_:).md)
  Asks the system to schedule and execute the specified operations.
### Handling errors
- [func signalErrorResolved(any Error, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/signalerrorresolved(_:completionhandler:).md)
  Indicates a resolved error.
### Collecting diagnostic reports
- [func requestDiagnosticCollection(for: NSFileProviderItemIdentifier, errorReason: any Error, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestdiagnosticcollection(for:errorreason:completionhandler:).md)
  Requests a diagnostics collection for use when working directly with Apple to improve sync behavior.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager)*