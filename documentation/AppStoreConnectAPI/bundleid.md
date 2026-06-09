# BundleId

**Framework**: App Store Connect API  
**Kind**: dictionary

An App ID registered with Apple, associating a specific bundle identifier with capabilities and provisioning profiles.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object BundleId
```

## Topics

### Objects
- [object BundleId.Attributes](bundleid/attributes-data.dictionary.md)
  Attributes that describe a Bundle IDs resource.
- [object BundleId.Relationships](bundleid/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BundleId.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (BundleId.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [type BundleIdPlatform](bundleidplatform.md)
  Strings that represent the operating system intended for the bundle.
- [object BundleIdCreateRequest](bundleidcreaterequest.md)
  The request body you use to create a Bundle ID.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundleid)*