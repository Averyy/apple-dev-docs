# Bundle ID Capabilities

**Framework**: App Store Connect API

Manage the app capabilities for a bundle ID.

#### Overview

The `bundleIdCapabilities` resource represents capabilities that you can enable or disable for a bundle ID. To learn about capabilities, see [`Advanced App Capabilities`](https://developer.apple.comhttps://developer.apple.com/support/app-capabilities/).

## Topics

### Enabling and Disabling Capabilities
- [Enable a Capability](post-v1-bundleidcapabilities.md)
  Enable a capability for a bundle ID.
- [Disable a Capability](delete-v1-bundleidcapabilities-_id_.md)
  Disable a capability for a bundle ID.
### Updating Capabiities
- [Modify a Capability Configuration](patch-v1-bundleidcapabilities-_id_.md)
  Update the configuration of a specific capability.
### Object and Data Types
- [object BundleIdCapability](bundleidcapability.md)
  The data structure that represents a Bundle ID Capabilities resource.
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

## See Also

- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
- [Certificates](certificates.md)
  Create, download, and revoke signing certificates for app development and distribution.
- [Devices](devices.md)
  Register devices for development and testing.
- [Profiles](profiles.md)
  Create, delete, and download provisioning profiles that enable app installations for development and distribution.
- [Merchant ID](merchantids.md)
  Manage your merchant ID for Apple Pay.
- [Pass type Ids](pass-type-id.md)
  Create, download, and revoke pass type ids for app development and distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundle-id-capabilities)*