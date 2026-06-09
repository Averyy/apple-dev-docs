# ProfilesWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of provisioning profiles, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object ProfilesWithoutIncludesResponse
```

## Properties

- `data` ([Profile]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object Profile](profile.md)
  A provisioning profile that authorizes specific devices to run an app during development or distribution.
- [object ProfileCreateRequest](profilecreaterequest.md)
  The request body you use to create a Profile.
- [object ProfileResponse](profileresponse.md)
  The response body for endpoints that create or read a single provisioning profile.
- [object ProfilesResponse](profilesresponse.md)
  The response body for endpoints that list provisioning profiles.
- [object ProfileBundleIdLinkageResponse](profilebundleidlinkageresponse.md)
- [object ProfileCertificatesLinkagesResponse](profilecertificateslinkagesresponse.md)
- [object ProfileDevicesLinkagesResponse](profiledeviceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/profileswithoutincludesresponse)*