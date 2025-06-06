# removeAllDomains(completionHandler:)

**Framework**: File Provider  
**Kind**: method

Removes all domains from the File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func removeAllDomains() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func removeAllDomains() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func removeAllDomains() async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A block that the system calls after removing the domains. It takes the following parameters:

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/removealldomains(completionhandler:))*