# BADownloadDomainAllowList

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The permitted list of domains the extension can use when scheduling the initial set of asset downloads.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Details

- **Name**: `BADownloadDomainAllowList`
- **Type**: array of string 

## Discussion

This key is required to use Background Assets.

## See Also

### Initial download restrictions
- [BADownloadAllowance](./badownloadallowance.md)
  The combined, maximum size of the initial, non-essential asset download files.
- [BAEssentialDownloadAllowance](./baessentialdownloadallowance.md)
  The combined, maximum size of the essential asset download files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/bainitialdownloadrestrictions/badownloaddomainallowlist)*