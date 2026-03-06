# Profile

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Profiles  resource.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object Profile
```

## Topics

### Objects
- [object Profile.Attributes](profile/attributes-data.dictionary.md)
  Attributes that describe a Profiles resource.
- [object Profile.Relationships](profile/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (Profile.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource
- `relationships` (Profile.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object ProfileCreateRequest](profilecreaterequest.md)
  The request body you use to create a Profile.
- [object ProfileResponse](profileresponse.md)
  A response that contains a single Profiles resource.
- [object ProfilesResponse](profilesresponse.md)
  A response that contains a list of Profiles resources.
- [object ProfilesWithoutIncludesResponse](profileswithoutincludesresponse.md)
- [object ProfileBundleIdLinkageResponse](profilebundleidlinkageresponse.md)
- [object ProfileCertificatesLinkagesResponse](profilecertificateslinkagesresponse.md)
- [object ProfileDevicesLinkagesResponse](profiledeviceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/profile)*