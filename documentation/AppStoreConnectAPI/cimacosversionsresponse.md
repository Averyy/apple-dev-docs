# CiMacOsVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of macOS Versions resources.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiMacOsVersionsResponse
```

## Properties

- `data` ([CiMacOsVersion]) *(required)*: The resource data.
- `included` ([CiXcodeVersion]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object CiMacOsVersion](cimacosversion.md)
  The data structure that represents a macOS Versions resource.
- [object CiMacOsVersionResponse](cimacosversionresponse.md)
  A response that contains a single macOS Versions resource.
- [object CiMacOsVersionXcodeVersionsLinkagesResponse](cimacosversionxcodeversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cimacosversionsresponse)*