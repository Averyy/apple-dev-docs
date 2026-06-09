# Profile

**Framework**: App Store Connect API  
**Kind**: dictionary

A provisioning profile that authorizes specific devices to run an app during development or distribution.

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
  The response body for endpoints that create or read a single provisioning profile.
- [object ProfilesResponse](profilesresponse.md)
  The response body for endpoints that list provisioning profiles.
- [object ProfilesWithoutIncludesResponse](profileswithoutincludesresponse.md)
  A response containing a list of provisioning profiles, without related resources.
- [object ProfileBundleIdLinkageResponse](profilebundleidlinkageresponse.md)
- [object ProfileCertificatesLinkagesResponse](profilecertificateslinkagesresponse.md)
- [object ProfileDevicesLinkagesResponse](profiledeviceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/profile)*