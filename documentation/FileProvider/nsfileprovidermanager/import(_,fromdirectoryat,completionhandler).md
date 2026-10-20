# import(_:fromDirectoryAt:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Type Method

Creates a new domain that takes ownership of on-disk data that your app previously managed without a file provider.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func `import`(_ domain: NSFileProviderDomain, fromDirectoryAt url: URL, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
class func `import`(_ domain: NSFileProviderDomain, fromDirectoryAt url: URL) async throws
```

```objc
+ (void) importDomain:(NSFileProviderDomain *) domain fromDirectoryAtURL:(NSURL *) url completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func `import`(_ domain: NSFileProviderDomain, fromDirectoryAt url: URL) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Use this method to migrate an existing file hierarchy on disk to a [`NSFileProviderExtension`](../nsfileproviderextension.md) without redownloading the data. After you call the method, the provided URL is no longer valid. The system has moved and now manages all of its contents.

If a domain with the same name already exists, the method fails with an [`NSFileWriteFileExistsError`](../../Foundation/nsfilewritefileexistserror-swift.var.md) error. The URL remains untouched. If the system doesn’t allow the extension to request a migration, the method fails with an [`NSFeatureUnsupportedError`](../../Foundation/nsfeatureunsupportederror-swift.var.md) error.

The system starts by moving the provided directory into its local cache, and then calls the completion handler. Then, for each item in the directory, it calls your extension’s [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](../nsfileproviderreplicatedextension/createitem%28basedon,fields,contents,options,request,completionhandler%29.md) with the [`mayAlreadyExist`](../nsfileprovidercreateitemoptions/mayalreadyexist.md) option.

When the import finishes, the system calls your extension’s [`importDidFinish(completionHandler:)`](../nsfileproviderreplicatedextension/importdidfinish%28completionhandler%29.md) method. If you call [`reimportItems(below:completionHandler:)`](./reimportitems%28below,completionhandler%29.md) before the import finishes, the system makes a single call to [`importDidFinish(completionHandler:)`](../nsfileproviderreplicatedextension/importdidfinish%28completionhandler%29.md) for both imports.

## Parameters

- `domain`: The domain to import.
- `url`: A URL that points to the directory to import.
- `completionHandler`: A block that the system calls as soon as it creates the new domain. It takes the following parameters:

  - **`error`**: If an error occurs, this object contains information about the error; otherwise, it’s `nil`.

## See Also

### Working with domains
- [convenience init?(for: NSFileProviderDomain)](./init%28for%29.md)
  Returns a newly created file provider manager for the specified domain.
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
- [func waitForStabilization(completionHandler: ((any Error)?) -> Void)](./waitforstabilization%28completionhandler%29.md)
  Requests a notification after the domain stabilizes.
- [func temporaryDirectoryURL() throws -> URL](./temporarydirectoryurl%28%29.md)
  Returns the URL of a directory that the File Provider extension can use to temporarily store files before passing them to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/import(_:fromdirectoryat:completionhandler:))*