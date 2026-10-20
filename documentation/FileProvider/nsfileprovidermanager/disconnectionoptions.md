# NSFileProviderManager.DisconnectionOptions

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Options for disconnecting a domain from the extension.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct DisconnectionOptions
```

```c
enum NSFileProviderManagerDisconnectionOptions : NSUInteger;
```

#### Overview

Use an empty set to indicate that the disconnection isn’t temporary, such as when the user logs out.

## Topics

### Choosing Disconnection Options
- [static var temporary: NSFileProviderManager.DisconnectionOptions](./disconnectionoptions/temporary.md)
  A temporary disconnection.
### Creating Disconnection Options
- [init(rawValue: UInt)](./disconnectionoptions/init%28rawvalue%29.md)
  Initializes the options from the raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

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
- [func reconnect(completionHandler: ((any Error)?) -> Void)](./reconnect%28completionhandler%29.md)
  Reconnects the domain with the extension.
- [func waitForStabilization(completionHandler: ((any Error)?) -> Void)](./waitforstabilization%28completionhandler%29.md)
  Requests a notification after the domain stabilizes.
- [func temporaryDirectoryURL() throws -> URL](./temporarydirectoryurl%28%29.md)
  Returns the URL of a directory that the File Provider extension can use to temporarily store files before passing them to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/disconnectionoptions)*