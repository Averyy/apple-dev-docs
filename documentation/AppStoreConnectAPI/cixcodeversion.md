# CiXcodeVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents an Xcode Versions resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiXcodeVersion
```

## Topics

### Objects
- [object CiXcodeVersion.Attributes](cixcodeversion/attributes-data.dictionary.md)
  The attributes that describe an Xcode Versions resource.
- [object CiXcodeVersion.Relationships](cixcodeversion/relationships-data.dictionary.md)
  The relationships of the Xcode Versions resource you included in the request and those on which you can operate.

## Properties

- `attributes` (CiXcodeVersion.Attributes): The attributes that describe the Xcode Versions resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies an Xcode Versions resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (CiXcodeVersion.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object CiXcodeVersionResponse](cixcodeversionresponse.md)
  A response that contains a single Xcode Versions resource.
- [object CiXcodeVersionsResponse](cixcodeversionsresponse.md)
  A response that contains a list of Xcode Versions resources.
- [object CiXcodeVersionMacOsVersionsLinkagesResponse](cixcodeversionmacosversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cixcodeversion)*