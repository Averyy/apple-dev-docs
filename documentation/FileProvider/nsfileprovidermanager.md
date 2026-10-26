# NSFileProviderManager

**Framework**: File Provider  
**Kind**: class  
**Role**: Class

A manager object that you use to communicate with the file provider from either your app or your File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderManager
```

```objc
@interface NSFileProviderManager : NSObject
```

## Mentions

- [Signaling Changes for User-Driven Actions](./signaling-changes-for-user-driven-actions.md)
- [Synchronizing the File Provider Extension](./synchronizing-the-file-provider-extension.md)

## Topics

### Accessing File Provider data
- [class var `default`: NSFileProviderManager](./nsfileprovidermanager/default.md)
  A property that returns the shared file provider manager object.
- [var documentStorageURL: URL](./nsfileprovidermanager/documentstorageurl.md)
  The root URL for all shared documents.
- [var providerIdentifier: String](./nsfileprovidermanager/provideridentifier.md)
  A purpose identifier for coordinated reads and writes.
### Translating user-visible URLs
- [func getUserVisibleURL(for: NSFileProviderItemIdentifier, completionHandler: (URL?, (any Error)?) -> Void)](./nsfileprovidermanager/getuservisibleurl%28for,completionhandler%29.md)
  Returns the user-visible URL for an item.
- [class func getIdentifierForUserVisibleFile(at: URL, completionHandler: (NSFileProviderItemIdentifier?, NSFileProviderDomainIdentifier?, (any Error)?) -> Void)](./nsfileprovidermanager/getidentifierforuservisiblefile%28at,completionhandler%29.md)
  Returns the identifier and domain for a user-visible URL.
### Working with items
- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/reimportitems%28below,completionhandler%29.md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/evictitem%28identifier,completionhandler%29.md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](./nsfileprovidermanager/requestdownloadforitem%28withidentifier,requestedrange%29.md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/requestdownloadforitem%28withidentifier,requestedrange,completionhandler%29.md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/requestmodification%28of,foritemwithidentifier,options,completionhandler%29.md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](./nsfileprovidermanager/enumeratorformaterializeditems%28%29.md)
  Returns an enumerator for all the items the system currently stores on disk.
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](./nsfileprovidermanager/enumeratorforpendingitems%28%29.md)
  Returns an enumerator for the set of pending items.
- [- requestDownloadForItemWithIdentifier:requestedRange:completionHandler:](./nsfileprovidermanager/requestdownloadforitemwithidentifier_requestedrange_completionhandler_.md)
### Performing actions
- [class func placeholderURL(for: URL) -> URL](./nsfileprovidermanager/placeholderurl%28for%29.md)
  Returns a placeholder URL for a given document URL.
- [class func writePlaceholder(at: URL, withMetadata: NSFileProviderItem) throws](./nsfileprovidermanager/writeplaceholder%28at,withmetadata%29.md)
  Writes a document placeholder with the provided metadata.
- [func register(URLSessionTask, forItemWithIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/register%28_,foritemwithidentifier,completionhandler%29.md)
  Registers the URL session task responsible for the specified item.
- [func signalEnumerator(for: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/signalenumerator%28for,completionhandler%29.md)
  Alerts the system to changes in the specified folder’s content.
- [func waitForChanges(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/waitforchanges%28below,completionhandler%29.md)
  Requests a notification after the system completes all the specified changes.
- [func globalProgress(for: Progress.FileOperationKind) -> Progress](./nsfileprovidermanager/globalprogress%28for%29.md)
  Returns a progress object that tracks either the uploading or downloading of items from the File Provider extension’s remote storage.
### Working with domains
- [convenience init?(for: NSFileProviderDomain)](./nsfileprovidermanager/init%28for%29.md)
  Returns a newly created file provider manager for the specified domain.
- [class func `import`(NSFileProviderDomain, fromDirectoryAt: URL, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/import%28_,fromdirectoryat,completionhandler%29.md)
  Creates a new domain that takes ownership of on-disk data that your app previously managed without a file provider.
- [class func add(NSFileProviderDomain, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/add%28_,completionhandler%29.md)
  Adds a domain to the File Provider extension.
- [class func getDomainsWithCompletionHandler(([NSFileProviderDomain], (any Error)?) -> Void)](./nsfileprovidermanager/getdomainswithcompletionhandler%28_%29.md)
  Returns all of the File Provider extension’s domains.
- [class func remove(NSFileProviderDomain, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/remove%28_,completionhandler%29.md)
  Removes a domain from the File Provider extension.
- [class func remove(NSFileProviderDomain, mode: NSFileProviderManager.DomainRemovalMode, completionHandler: (URL?, (any Error)?) -> Void)](./nsfileprovidermanager/remove%28_,mode,completionhandler%29.md)
  Removes a domain from the File Provider extension using the specified options.
- [class func removeAllDomains(completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/removealldomains%28completionhandler%29.md)
  Removes all domains from the File Provider extension.
- [NSFileProviderManager.DomainRemovalMode](./nsfileprovidermanager/domainremovalmode.md)
  A mode indicating how the system handles user data when removing a domain.
- [func disconnect(reason: String, options: NSFileProviderManager.DisconnectionOptions, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/disconnect%28reason,options,completionhandler%29.md)
  Disconnects the domain from the extension.
- [NSFileProviderManager.DisconnectionOptions](./nsfileprovidermanager/disconnectionoptions.md)
  Options for disconnecting a domain from the extension.
- [func reconnect(completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/reconnect%28completionhandler%29.md)
  Reconnects the domain with the extension.
- [func waitForStabilization(completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/waitforstabilization%28completionhandler%29.md)
  Requests a notification after the domain stabilizes.
- [func temporaryDirectoryURL() throws -> URL](./nsfileprovidermanager/temporarydirectoryurl%28%29.md)
  Returns the URL of a directory that the File Provider extension can use to temporarily store files before passing them to the system.
### Syncing Desktop and Documents folders
- [func claimKnownFolders(NSFileProviderKnownFolderLocations, localizedReason: String, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/claimknownfolders%28_,localizedreason,completionhandler%29.md)
  Asks the domain to sync the specified known folders.
- [func releaseKnownFolders(NSFileProviderKnownFolders, localizedReason: String, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/releaseknownfolders%28_,localizedreason,completionhandler%29.md)
  Asks the system to stop replicating the specified known folders in the domain.
- [struct NSFileProviderKnownFolders](./nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [class NSFileProviderKnownFolderLocations](./nsfileproviderknownfolderlocations.md)
  A class for working with known-folder locations.
- [protocol NSFileProviderKnownFolderSupporting](./nsfileproviderknownfoldersupporting.md)
  A protocol that defines the interface for sharing known-folder locations with the system.
### Working with external volumes
- [func stateDirectoryURL() throws -> URL](./nsfileprovidermanager/statedirectoryurl%28%29.md)
  Returns a URL for a directory for storing state information for the domain.
- [class func checkDomainsCanBeStoredOnVolume(at: URL) throws -> NSFileProviderManager.EligibilityResult](./nsfileprovidermanager/checkdomainscanbestoredonvolume%28at%29.md)
  Checks whether the specified URL is eligible for storing a domain.
- [NSFileProviderManager.EligibilityResult](./nsfileprovidermanager/eligibilityresult.md)
  Constants that specify whether a URL is eligible for storing a domain.
- [protocol NSFileProviderExternalVolumeHandling](./nsfileproviderexternalvolumehandling.md)
  A protocol that defines the interface for handling external volumes.
- [+ checkDomainsCanBeStored:onVolumeAtURL:unsupportedReason:error:](./nsfileprovidermanager/checkdomainscanbestored_onvolumeaturl_unsupportedreason_error_.md)
  Check if a URL is eligible for storing a domain.
### Using services
- [func getService(named: NSFileProviderServiceName, for: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderService?, (any Error)?) -> Void)](./nsfileprovidermanager/getservice%28named,for,completionhandler%29.md)
### Testing
- [func listAvailableTestingOperations() throws -> [any NSFileProviderTestingOperation]](./nsfileprovidermanager/listavailabletestingoperations%28%29.md)
  Lists all the operations that are ready for scheduling.
- [func run([any NSFileProviderTestingOperation]) throws -> [AnyHashable : any Error]](./nsfileprovidermanager/run%28_%29.md)
  Asks the system to schedule and execute the specified operations.
### Handling errors
- [func signalErrorResolved(any Error, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/signalerrorresolved%28_,completionhandler%29.md)
  Indicates a resolved error.
### Collecting diagnostic reports
- [func requestDiagnosticCollection(for: NSFileProviderItemIdentifier, errorReason: any Error, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/requestdiagnosticcollection%28for,errorreason,completionhandler%29.md)
  Requests a diagnostics collection for use when working directly with Apple to improve sync behavior.
### Initializers
- [convenience init?(forDomain: NSFileProviderDomain)](./nsfileprovidermanager/init%28fordomain%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager)*