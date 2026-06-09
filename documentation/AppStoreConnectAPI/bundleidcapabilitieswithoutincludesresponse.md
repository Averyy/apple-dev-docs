# BundleIdCapabilitiesWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of bundle ID capabilities, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object BundleIdCapabilitiesWithoutIncludesResponse
```

## Properties

- `data` ([BundleIdCapability]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object BundleIdCapability](bundleidcapability.md)
  An entitlement or service (such as Push Notifications or In-App Purchases) enabled for a registered bundle ID.
- [object BundleIdCapabilityCreateRequest](bundleidcapabilitycreaterequest.md)
  The request body you use to create a Bundle ID Capability.
- [object BundleIdCapabilityUpdateRequest](bundleidcapabilityupdaterequest.md)
  The request body you use to update a Bundle ID Capability.
- [object BundleIdCapabilityResponse](bundleidcapabilityresponse.md)
  The response body for endpoints that enable or modify a capability for a bundle ID.
- [object BundleIdCapabilitiesResponse](bundleidcapabilitiesresponse.md)
  The response body for endpoints that list capabilities enabled for a bundle ID.
- [object CapabilityOption](capabilityoption.md)
  An option within a capability setting.
- [object CapabilitySetting](capabilitysetting.md)
  An object that represents a capability setting for an app.
- [type CapabilityType](capabilitytype.md)
  String that represents an app’s capability type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundleidcapabilitieswithoutincludesresponse)*