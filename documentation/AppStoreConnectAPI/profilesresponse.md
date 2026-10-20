# ProfilesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that list provisioning profiles.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```
object ProfilesResponse
```

## Properties

- `data` ([Profile]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([*]): **Allowed Types**: `BundleId`, `Certificate`, `Device`

## See Also

### Related Documentation
- [List and download profiles](./get-v1-profiles.md)
  Find and list provisioning profiles and download their data.
### Objects
- [object Profile](./profile.md)
  A provisioning profile that authorizes specific devices to run an app during development or distribution.
- [object ProfileCreateRequest](./profilecreaterequest.md)
  The request body you use to create a Profile.
- [object ProfileResponse](./profileresponse.md)
  The response body for endpoints that create or read a single provisioning profile.
- [object ProfilesWithoutIncludesResponse](./profileswithoutincludesresponse.md)
  A response containing a list of provisioning profiles, without related resources.
- [object ProfileBundleIdLinkageResponse](./profilebundleidlinkageresponse.md)
- [object ProfileCertificatesLinkagesResponse](./profilecertificateslinkagesresponse.md)
- [object ProfileDevicesLinkagesResponse](./profiledeviceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/profilesresponse)*