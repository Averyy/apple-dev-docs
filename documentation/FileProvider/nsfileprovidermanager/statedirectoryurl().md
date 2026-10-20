# stateDirectoryURL()

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Returns a URL for a directory for storing state information for the domain.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func stateDirectoryURL() throws -> URL
```

```objc
- (NSURL *) stateDirectoryURLWithError:(NSError **) error;
```

## See Also

### Working with external volumes
- [class func checkDomainsCanBeStoredOnVolume(at: URL) throws -> NSFileProviderManager.EligibilityResult](./checkdomainscanbestoredonvolume%28at%29.md)
  Checks whether the specified URL is eligible for storing a domain.
- [NSFileProviderManager.EligibilityResult](./eligibilityresult.md)
  Constants that specify whether a URL is eligible for storing a domain.
- [protocol NSFileProviderExternalVolumeHandling](../nsfileproviderexternalvolumehandling.md)
  A protocol that defines the interface for handling external volumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/statedirectoryurl())*