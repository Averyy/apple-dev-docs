# CiMacOsVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a macOS Versions resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiMacOsVersion
```

## Topics

### Objects
- [object CiMacOsVersion.Attributes](cimacosversion/attributes-data.dictionary.md)
  The attributes that describe a macOS Versions resource.
- [object CiMacOsVersion.Relationships](cimacosversion/relationships-data.dictionary.md)
  The relationships of the macOS Versions resource you included in the request and those on which you can operate.

## Properties

- `attributes` (CiMacOsVersion.Attributes): The attributes that describe the macOS Versions resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a macOS Versions resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (CiMacOsVersion.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object CiMacOsVersionResponse](cimacosversionresponse.md)
  A response that contains a single macOS Versions resource.
- [object CiMacOsVersionsResponse](cimacosversionsresponse.md)
  A response that contains a list of macOS Versions resources.
- [object CiMacOsVersionXcodeVersionsLinkagesResponse](cimacosversionxcodeversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cimacosversion)*