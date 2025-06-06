# stateDirectoryURL()

**Framework**: File Provider  
**Kind**: method

Returns a URL for a directory for storing state information for the domain.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func stateDirectoryURL() throws -> URL
```

## See Also

- [class func checkDomainsCanBeStoredOnVolume(at: URL) throws -> NSFileProviderManager.EligibilityResult](nsfileprovidermanager/checkdomainscanbestoredonvolume(at:).md)
  Checks whether the specified URL is eligible for storing a domain.
- [NSFileProviderManager.EligibilityResult](nsfileprovidermanager/eligibilityresult.md)
  Constants that specify whether a URL is eligible for storing a domain.
- [protocol NSFileProviderExternalVolumeHandling](nsfileproviderexternalvolumehandling.md)
  A protocol that defines the interface for handling external volumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/statedirectoryurl())*