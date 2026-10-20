# CapabilityOption

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

An option within a capability setting.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```
object CapabilityOption
```

## Properties

- `description` (string)
- `enabled` (boolean)
- `enabledByDefault` (boolean)
- `key` (string): **Allowed Values**: `XCODE_5`, `XCODE_6`, `COMPLETE_PROTECTION`, `PROTECTED_UNLESS_OPEN`, `PROTECTED_UNTIL_FIRST_USER_AUTH`, `PRIMARY_APP_CONSENT`
- `name` (string)
- `supportsWildcard` (boolean)

## See Also

### Object and Data Types
- [object BundleIdCapability](./bundleidcapability.md)
  An entitlement or service (such as Push Notifications or In-App Purchases) enabled for a registered bundle ID.
- [object BundleIdCapabilityCreateRequest](./bundleidcapabilitycreaterequest.md)
  The request body you use to create a Bundle ID Capability.
- [object BundleIdCapabilityUpdateRequest](./bundleidcapabilityupdaterequest.md)
  The request body you use to update a Bundle ID Capability.
- [object BundleIdCapabilityResponse](./bundleidcapabilityresponse.md)
  The response body for endpoints that enable or modify a capability for a bundle ID.
- [object BundleIdCapabilitiesResponse](./bundleidcapabilitiesresponse.md)
  The response body for endpoints that list capabilities enabled for a bundle ID.
- [object BundleIdCapabilitiesWithoutIncludesResponse](./bundleidcapabilitieswithoutincludesresponse.md)
  A response containing a list of bundle ID capabilities, without related resources.
- [object CapabilitySetting](./capabilitysetting.md)
  An object that represents a capability setting for an app.
- [type CapabilityType](./capabilitytype.md)
  String that represents an app’s capability type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/capabilityoption)*