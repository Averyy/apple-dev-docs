# BundleIdWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single bundle ID, without including capability and profile details.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object BundleIdWithoutIncludesResponse
```

## Properties

- `data` (BundleId) *(required)*
- `links` (DocumentLinks) *(required)*

## See Also

- [object BundleId](bundleid.md)
  An App ID registered with Apple, associating a specific bundle identifier with capabilities and provisioning profiles.
- [type BundleIdPlatform](bundleidplatform.md)
  Strings that represent the operating system intended for the bundle.
- [object BundleIdCreateRequest](bundleidcreaterequest.md)
  The request body you use to create a Bundle ID.
- [object BundleIdUpdateRequest](bundleidupdaterequest.md)
  The request body you use to update a Bundle ID.
- [object BundleIdResponse](bundleidresponse.md)
  The response body for endpoints that create, read, or modify a single bundle ID.
- [object BundleIdsResponse](bundleidsresponse.md)
  The response body for endpoints that list bundle IDs.
- [object BundleIdAppLinkageResponse](bundleidapplinkageresponse.md)
- [object BundleIdBundleIdCapabilitiesLinkagesResponse](bundleidbundleidcapabilitieslinkagesresponse.md)
- [object BundleIdProfilesLinkagesResponse](bundleidprofileslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundleidwithoutincludesresponse)*