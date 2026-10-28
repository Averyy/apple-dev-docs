# waitForStabilization(completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Requests a notification after the domain stabilizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func waitForStabilization(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func waitForStabilization() async throws
```

```objc
- (void) waitForStabilizationWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func waitForStabilization() async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Use this method to enforce a consistent state for testing. The system calls the completion handler after all the pending changes to the local cache and the remote storage have completed. The system waits on any changes that requested before the call to [`waitForStabilization(completionHandler:)`](./waitforstabilization%28completionhandler%29.md), but which haven’t completed yet.

> ⚠️ **Warning**:  Only use [`waitForStabilization(completionHandler:)`](./waitforstabilization%28completionhandler%29.md) for testing and debugging. Don’t call this method in a production app, due to its high performance cost.

## Parameters

- `completionHandler`: A block that the system calls after pending changes to both the file system and the provider have completed. The system passes the following parameters:

  - **`error`**: If an error occurs, this object contains information about the error; otherwise, it’s `nil`.

## See Also

### Working with domains
- [convenience init?(for: NSFileProviderDomain)](./init%28for%29.md)
  Returns a newly created file provider manager for the specified domain.
- [class func `import`(NSFileProviderDomain, fromDirectoryAt: URL, completionHandler: ((any Error)?) -> Void)](./import%28_,fromdirectoryat,completionhandler%29.md)
  Creates a new domain that takes ownership of on-disk data that your app previously managed without a file provider.
- [class func add(NSFileProviderDomain, completionHandler: ((any Error)?) -> Void)](./add%28_,completionhandler%29.md)
  Adds a domain to the File Provider extension.
- [class func getDomainsWithCompletionHandler(([NSFileProviderDomain], (any Error)?) -> Void)](./getdomainswithcompletionhandler%28_%29.md)
  Returns all of the File Provider extension’s domains.
- [class func remove(NSFileProviderDomain, completionHandler: ((any Error)?) -> Void)](./remove%28_,completionhandler%29.md)
  Removes a domain from the File Provider extension.
- [class func remove(NSFileProviderDomain, mode: NSFileProviderManager.DomainRemovalMode, completionHandler: (URL?, (any Error)?) -> Void)](./remove%28_,mode,completionhandler%29.md)
  Removes a domain from the File Provider extension using the specified options.
- [class func removeAllDomains(completionHandler: ((any Error)?) -> Void)](./removealldomains%28completionhandler%29.md)
  Removes all domains from the File Provider extension.
- [NSFileProviderManager.DomainRemovalMode](./domainremovalmode.md)
  A mode indicating how the system handles user data when removing a domain.
- [func disconnect(reason: String, options: NSFileProviderManager.DisconnectionOptions, completionHandler: ((any Error)?) -> Void)](./disconnect%28reason,options,completionhandler%29.md)
  Disconnects the domain from the extension.
- [NSFileProviderManager.DisconnectionOptions](./disconnectionoptions.md)
  Options for disconnecting a domain from the extension.
- [func reconnect(completionHandler: ((any Error)?) -> Void)](./reconnect%28completionhandler%29.md)
  Reconnects the domain with the extension.
- [func temporaryDirectoryURL() throws -> URL](./temporarydirectoryurl%28%29.md)
  Returns the URL of a directory that the File Provider extension can use to temporarily store files before passing them to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/waitforstabilization(completionhandler:))*