# temporaryDirectoryURL()

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Returns the URL of a directory that the File Provider extension can use to temporarily store files before passing them to the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func temporaryDirectoryURL() throws -> URL
```

```objc
- (NSURL *) temporaryDirectoryURLWithError:(NSError **) error;
```

#### Discussion

The system guarantees that the temporary URL refers to a directory on the same volume as the user-visible URL so that the system can automatically clone or move files between the temporary URL and the user-visible URL. For example, the File Provider extension can use the temporary directory to store content passed to the [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](../nsfileproviderreplicatedextension/createitem%28basedon,fields,contents,options,request,completionhandler%29.md) or [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](../nsfileproviderreplicatedextension/modifyitem%28_,baseversion,changedfields,contents,options,request,completionhandler%29.md) methods.

When you implement your File Provider extension’s [`fetchContents(for:version:request:completionHandler:)`](../nsfileproviderreplicatedextension/fetchcontents%28for,version,request,completionhandler%29.md) method, the URL you pass to the completion handler must be on the same volume as the temporary directory, so the system can clone it to provide the content for the dataless item.

This method fails if the system can’t find a suitable directory, for example, if the domain doesn’t exist. However, it can’t fail if the file provider has an active instance for the specified domain.

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
- [func waitForStabilization(completionHandler: ((any Error)?) -> Void)](./waitforstabilization%28completionhandler%29.md)
  Requests a notification after the domain stabilizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/temporarydirectoryurl())*