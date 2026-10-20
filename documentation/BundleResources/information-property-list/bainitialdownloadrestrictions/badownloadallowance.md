# BADownloadAllowance

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The combined, maximum size of the initial, non-essential asset download files.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Details

- **Name**: `BADownloadAllowance`
- **Type**: integer

#### Discussion

If you compress the initial assets, use the compressed file sizes that the system downloads, not the uncompressed file sizes, when providing this value. This key is required to use Background Assets.

## See Also

### Initial download restrictions
- [BADownloadDomainAllowList](./badownloaddomainallowlist.md)
  The permitted list of domains the extension can use when scheduling the initial set of asset downloads.
- [BAEssentialDownloadAllowance](./baessentialdownloadallowance.md)
  The combined, maximum size of the essential asset download files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/bainitialdownloadrestrictions/badownloadallowance)*