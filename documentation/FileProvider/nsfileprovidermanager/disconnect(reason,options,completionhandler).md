# disconnect(reason:options:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Disconnects the domain from the extension.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func disconnect(reason localizedReason: String, options: NSFileProviderManager.DisconnectionOptions = [], completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func disconnect(reason localizedReason: String, options: NSFileProviderManager.DisconnectionOptions = []) async throws
```

```objc
- (void) disconnectWithReason:(NSString *) localizedReason options:(NSFileProviderManagerDisconnectionOptions) options completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func disconnect(reason localizedReason: String, options: NSFileProviderManager.DisconnectionOptions = []) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Call this method to disconnect the domain from the extension. While the domain is disconnected, the user can continue to browse its content, but the extension no longer receives updates about changes.

Call the [`reconnect(completionHandler:)`](./reconnect%28completionhandler%29.md) method to reconnect the domain.

## Parameters

- `localizedReason`: A localized string that describes the reason for disconnecting the domain.
- `options`: Options for the disconnection. For a complete list of valid options, see [`NSFileProviderManager.DisconnectionOptions`](./disconnectionoptions.md).
- `completionHandler`: A block that the system calls after disconnecting the domain. The block takes the following parameter:

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
- [NSFileProviderManager.DisconnectionOptions](./disconnectionoptions.md)
  Options for disconnecting a domain from the extension.
- [func reconnect(completionHandler: ((any Error)?) -> Void)](./reconnect%28completionhandler%29.md)
  Reconnects the domain with the extension.
- [func waitForStabilization(completionHandler: ((any Error)?) -> Void)](./waitforstabilization%28completionhandler%29.md)
  Requests a notification after the domain stabilizes.
- [func temporaryDirectoryURL() throws -> URL](./temporarydirectoryurl%28%29.md)
  Returns the URL of a directory that the File Provider extension can use to temporarily store files before passing them to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/disconnect(reason:options:completionhandler:))*