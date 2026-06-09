# BundleIdResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a single bundle ID.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object BundleIdResponse
```

## Properties

- `data` (BundleId) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([*]): The requested relationship data.

## See Also

- [object BundleId](bundleid.md)
  An App ID registered with Apple, associating a specific bundle identifier with capabilities and provisioning profiles.
- [type BundleIdPlatform](bundleidplatform.md)
  Strings that represent the operating system intended for the bundle.
- [object BundleIdCreateRequest](bundleidcreaterequest.md)
  The request body you use to create a Bundle ID.
- [object BundleIdUpdateRequest](bundleidupdaterequest.md)
  The request body you use to update a Bundle ID.
- [object BundleIdWithoutIncludesResponse](bundleidwithoutincludesresponse.md)
  A response containing a single bundle ID, without including capability and profile details.
- [object BundleIdsResponse](bundleidsresponse.md)
  The response body for endpoints that list bundle IDs.
- [object BundleIdAppLinkageResponse](bundleidapplinkageresponse.md)
- [object BundleIdBundleIdCapabilitiesLinkagesResponse](bundleidbundleidcapabilitieslinkagesresponse.md)
- [object BundleIdProfilesLinkagesResponse](bundleidprofileslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundleidresponse)*