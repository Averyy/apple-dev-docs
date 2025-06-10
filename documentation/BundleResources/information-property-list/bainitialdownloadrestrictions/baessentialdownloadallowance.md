# BAEssentialDownloadAllowance

**Framework**: Bundle Resources  
**Kind**: typealias

The combined, maximum size of the essential asset download files.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.4+
- visionOS 2.4+

#### Discussion

If you compress the essential assets, use the compressed file sizes that the system downloads, not the uncompressed file sizes, when providing this value. This key is required to use Background Assets.

## See Also

- [BADownloadAllowance](information-property-list/bainitialdownloadrestrictions/badownloadallowance.md)
  The combined, maximum size of the initial, non-essential asset download files.
- [BADownloadDomainAllowList](information-property-list/bainitialdownloadrestrictions/badownloaddomainallowlist.md)
  The permitted list of domains the extension can use when scheduling the initial set of asset downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/bainitialdownloadrestrictions/baessentialdownloadallowance)*