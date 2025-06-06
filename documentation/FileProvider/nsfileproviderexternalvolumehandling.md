# NSFileProviderExternalVolumeHandling

**Framework**: File Provider  
**Kind**: protocol

A protocol that defines the interface for handling external volumes.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol NSFileProviderExternalVolumeHandling : NSObjectProtocol
```

## Topics

### Connecting to external domains
- [func shouldConnectExternalDomain(completionHandler: ((any Error)?) -> Void)](nsfileproviderexternalvolumehandling/shouldconnectexternaldomain(completionhandler:).md)
  Determines whether to connect to a domain from another device.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func stateDirectoryURL() throws -> URL](nsfileprovidermanager/statedirectoryurl.md)
  Returns a URL for a directory for storing state information for the domain.
- [class func checkDomainsCanBeStoredOnVolume(at: URL) throws -> NSFileProviderManager.EligibilityResult](nsfileprovidermanager/checkdomainscanbestoredonvolume(at:).md)
  Checks whether the specified URL is eligible for storing a domain.
- [NSFileProviderManager.EligibilityResult](nsfileprovidermanager/eligibilityresult.md)
  Constants that specify whether a URL is eligible for storing a domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderexternalvolumehandling)*