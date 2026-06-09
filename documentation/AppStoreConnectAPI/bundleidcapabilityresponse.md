# BundleIdCapabilityResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that enable or modify a capability for a bundle ID.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object BundleIdCapabilityResponse
```

## Properties

- `data` (BundleIdCapability) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object BundleIdCapability](bundleidcapability.md)
  An entitlement or service (such as Push Notifications or In-App Purchases) enabled for a registered bundle ID.
- [object BundleIdCapabilityCreateRequest](bundleidcapabilitycreaterequest.md)
  The request body you use to create a Bundle ID Capability.
- [object BundleIdCapabilityUpdateRequest](bundleidcapabilityupdaterequest.md)
  The request body you use to update a Bundle ID Capability.
- [object BundleIdCapabilitiesResponse](bundleidcapabilitiesresponse.md)
  The response body for endpoints that list capabilities enabled for a bundle ID.
- [object BundleIdCapabilitiesWithoutIncludesResponse](bundleidcapabilitieswithoutincludesresponse.md)
  A response containing a list of bundle ID capabilities, without related resources.
- [object CapabilityOption](capabilityoption.md)
  An option within a capability setting.
- [object CapabilitySetting](capabilitysetting.md)
  An object that represents a capability setting for an app.
- [type CapabilityType](capabilitytype.md)
  String that represents an app’s capability type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundleidcapabilityresponse)*