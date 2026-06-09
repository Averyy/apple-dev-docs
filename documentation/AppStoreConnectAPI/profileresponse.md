# ProfileResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create or read a single provisioning profile.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object ProfileResponse
```

## Properties

- `data` (Profile) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([*])

## See Also

- [Create a profile](post-v1-profiles.md)
  Create a new provisioning profile.
- [object Profile](profile.md)
  A provisioning profile that authorizes specific devices to run an app during development or distribution.
- [object ProfileCreateRequest](profilecreaterequest.md)
  The request body you use to create a Profile.
- [object ProfilesResponse](profilesresponse.md)
  The response body for endpoints that list provisioning profiles.
- [object ProfilesWithoutIncludesResponse](profileswithoutincludesresponse.md)
  A response containing a list of provisioning profiles, without related resources.
- [object ProfileBundleIdLinkageResponse](profilebundleidlinkageresponse.md)
- [object ProfileCertificatesLinkagesResponse](profilecertificateslinkagesresponse.md)
- [object ProfileDevicesLinkagesResponse](profiledeviceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/profileresponse)*