# BundleIdCapability

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Bundle ID Capabilities resource.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```swift
object BundleIdCapability
```

## Topics

### Objects
- [object BundleIdCapability.Attributes](bundleidcapability/attributes-data.dictionary.md)
  Attributes that describe a Bundle ID Capabilities resource.

## Properties

- `attributes` (BundleIdCapability.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object BundleIdCapabilityCreateRequest](bundleidcapabilitycreaterequest.md)
  The request body you use to create a Bundle ID Capability.
- [object BundleIdCapabilityUpdateRequest](bundleidcapabilityupdaterequest.md)
  The request body you use to update a Bundle ID Capability.
- [object BundleIdCapabilityResponse](bundleidcapabilityresponse.md)
  A response that contains a single Bundle ID Capabilities resource.
- [object BundleIdCapabilitiesResponse](bundleidcapabilitiesresponse.md)
  A response that contains a list of Bundle ID Capability resources.
- [object BundleIdCapabilitiesWithoutIncludesResponse](bundleidcapabilitieswithoutincludesresponse.md)
- [object CapabilityOption](capabilityoption.md)
  An option within a capability setting.
- [object CapabilitySetting](capabilitysetting.md)
  An object that  represents a capability setting for an app.
- [type CapabilityType](capabilitytype.md)
  String that represents an app’s capability type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundleidcapability)*