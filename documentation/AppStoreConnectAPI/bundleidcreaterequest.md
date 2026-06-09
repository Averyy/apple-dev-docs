# BundleIdCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create a Bundle ID.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object BundleIdCreateRequest
```

## Topics

### Objects
- [object BundleIdCreateRequest.Data](bundleidcreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (BundleIdCreateRequest.Data) *(required)*: The resource data.

## See Also

- [object BundleId](bundleid.md)
  An App ID registered with Apple, associating a specific bundle identifier with capabilities and provisioning profiles.
- [type BundleIdPlatform](bundleidplatform.md)
  Strings that represent the operating system intended for the bundle.
- [object BundleIdUpdateRequest](bundleidupdaterequest.md)
  The request body you use to update a Bundle ID.
- [object BundleIdResponse](bundleidresponse.md)
  The response body for endpoints that create, read, or modify a single bundle ID.
- [object BundleIdWithoutIncludesResponse](bundleidwithoutincludesresponse.md)
  A response containing a single bundle ID, without including capability and profile details.
- [object BundleIdsResponse](bundleidsresponse.md)
  The response body for endpoints that list bundle IDs.
- [object BundleIdAppLinkageResponse](bundleidapplinkageresponse.md)
- [object BundleIdBundleIdCapabilitiesLinkagesResponse](bundleidbundleidcapabilitieslinkagesresponse.md)
- [object BundleIdProfilesLinkagesResponse](bundleidprofileslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundleidcreaterequest)*