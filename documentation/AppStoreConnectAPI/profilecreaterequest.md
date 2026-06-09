# ProfileCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create a Profile.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object ProfileCreateRequest
```

## Topics

### Objects
- [object ProfileCreateRequest.Data](profilecreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (ProfileCreateRequest.Data) *(required)*: The resource data.

## See Also

- [object Profile](profile.md)
  A provisioning profile that authorizes specific devices to run an app during development or distribution.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/profilecreaterequest)*