# CiXcodeVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of Xcode Versions resources.

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
  The data structure that represents an Xcode Versions resource.
- [object CiXcodeVersionResponse](cixcodeversionresponse.md)
  A response that contains a single Xcode Versions resource.
- [object CiXcodeVersionMacOsVersionsLinkagesResponse](cixcodeversionmacosversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cixcodeversionsresponse)*