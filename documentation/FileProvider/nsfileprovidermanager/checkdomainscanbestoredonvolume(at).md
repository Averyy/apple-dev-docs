# checkDomainsCanBeStoredOnVolume(at:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Type Method

Checks whether the specified URL is eligible for storing a domain.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class func checkDomainsCanBeStoredOnVolume(at url: URL) throws -> NSFileProviderManager.EligibilityResult
```

## See Also

### Working with external volumes
- [func stateDirectoryURL() throws -> URL](./statedirectoryurl%28%29.md)
  Returns a URL for a directory for storing state information for the domain.
- [NSFileProviderManager.EligibilityResult](./eligibilityresult.md)
  Constants that specify whether a URL is eligible for storing a domain.
- [protocol NSFileProviderExternalVolumeHandling](../nsfileproviderexternalvolumehandling.md)
  A protocol that defines the interface for handling external volumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/checkdomainscanbestoredonvolume(at:))*