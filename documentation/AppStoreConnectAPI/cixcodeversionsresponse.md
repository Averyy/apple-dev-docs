# CiXcodeVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list Xcode versions available for Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiXcodeVersionsResponse
```

## Properties

- `data` ([CiXcodeVersion]) *(required)*: The resource data.
- `included` ([CiMacOsVersion]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object CiXcodeVersion](cixcodeversion.md)
  An Xcode version available in Xcode Cloud for running workflow builds and tests.
- [object CiXcodeVersionResponse](cixcodeversionresponse.md)
  The response body for endpoints that read a single Xcode version available in Xcode Cloud.
- [object CiXcodeVersionMacOsVersionsLinkagesResponse](cixcodeversionmacosversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cixcodeversionsresponse)*