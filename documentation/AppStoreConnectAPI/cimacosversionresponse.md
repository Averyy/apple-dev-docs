# CiMacOsVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single macOS version available in Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiMacOsVersionResponse
```

## Properties

- `data` (CiMacOsVersion) *(required)*: The resource data.
- `included` ([CiXcodeVersion]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object CiMacOsVersion](cimacosversion.md)
  A macOS version available in Xcode Cloud infrastructure for running workflow builds.
- [object CiMacOsVersionsResponse](cimacosversionsresponse.md)
  A response containing a list of macOS versions supported by Xcode Cloud.
- [object CiMacOsVersionXcodeVersionsLinkagesResponse](cimacosversionxcodeversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cimacosversionresponse)*