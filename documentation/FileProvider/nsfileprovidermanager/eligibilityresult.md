# NSFileProviderManager.EligibilityResult

**Framework**: File Provider  
**Kind**: enum

Constants that specify whether a URL is eligible for storing a domain.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum EligibilityResult
```

## Topics

### Determining eligibility
- [NSFileProviderManager.EligibilityResult.eligible](nsfileprovidermanager/eligibilityresult/eligible.md)
- [NSFileProviderManager.EligibilityResult.ineligible(_:)](nsfileprovidermanager/eligibilityresult/ineligible(_:).md)
- [struct NSFileProviderVolumeUnsupportedReason](nsfileprovidervolumeunsupportedreason.md)
  Constants that describe why an external volume might not be eligible for storing a domain.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func stateDirectoryURL() throws -> URL](nsfileprovidermanager/statedirectoryurl.md)
  Returns a URL for a directory for storing state information for the domain.
- [class func checkDomainsCanBeStoredOnVolume(at: URL) throws -> NSFileProviderManager.EligibilityResult](nsfileprovidermanager/checkdomainscanbestoredonvolume(at:).md)
  Checks whether the specified URL is eligible for storing a domain.
- [protocol NSFileProviderExternalVolumeHandling](nsfileproviderexternalvolumehandling.md)
  A protocol that defines the interface for handling external volumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/eligibilityresult)*