# CiXcodeVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a single Xcode Versions resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiXcodeVersionResponse
```

## Properties

- `data` (CiXcodeVersion) *(required)*: The resource data.
- `included` ([CiMacOsVersion]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object CiXcodeVersion](cixcodeversion.md)
  The data structure that represents an Xcode Versions resource.
- [object CiXcodeVersionsResponse](cixcodeversionsresponse.md)
  A response that contains a list of Xcode Versions resources.
- [object CiXcodeVersionMacOsVersionsLinkagesResponse](cixcodeversionmacosversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cixcodeversionresponse)*