# NSFileProviderExternalVolumeHandling

**Framework**: File Provider  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the interface for handling external volumes.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol NSFileProviderExternalVolumeHandling : NSObjectProtocol
```

```objc
@protocol NSFileProviderExternalVolumeHandling <NSObject>
```

## Topics

### Connecting to external domains
- [func shouldConnectExternalDomain(completionHandler: ((any Error)?) -> Void)](./nsfileproviderexternalvolumehandling/shouldconnectexternaldomain%28completionhandler%29.md)
  Determines whether to connect to a domain from another device.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with external volumes
- [func stateDirectoryURL() throws -> URL](./nsfileprovidermanager/statedirectoryurl%28%29.md)
  Returns a URL for a directory for storing state information for the domain.
- [class func checkDomainsCanBeStoredOnVolume(at: URL) throws -> NSFileProviderManager.EligibilityResult](./nsfileprovidermanager/checkdomainscanbestoredonvolume%28at%29.md)
  Checks whether the specified URL is eligible for storing a domain.
- [NSFileProviderManager.EligibilityResult](./nsfileprovidermanager/eligibilityresult.md)
  Constants that specify whether a URL is eligible for storing a domain.
- [+ checkDomainsCanBeStored:onVolumeAtURL:unsupportedReason:error:](./nsfileprovidermanager/checkdomainscanbestored_onvolumeaturl_unsupportedreason_error_.md)
  Check if a URL is eligible for storing a domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderexternalvolumehandling)*