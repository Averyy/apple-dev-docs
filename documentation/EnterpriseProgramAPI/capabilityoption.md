# CapabilityOption

**Framework**: Enterprise Program API  
**Kind**: dictionary  
**Role**: Object

An option within a capability setting.

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
  The data structure that represents a Bundle ID Capabilities resource.
- [object BundleIdCapabilityCreateRequest](./bundleidcapabilitycreaterequest.md)
  The request body you use to create a Bundle ID Capability.
- [object BundleIdCapabilityUpdateRequest](./bundleidcapabilityupdaterequest.md)
  The request body you use to update a Bundle ID Capability.
- [object BundleIdCapabilityResponse](./bundleidcapabilityresponse.md)
  A response that contains a single Bundle ID Capabilities resource.
- [object BundleIdCapabilitiesResponse](./bundleidcapabilitiesresponse.md)
  A response that contains a list of Bundle ID Capability resources.
- [object BundleIdCapabilitiesWithoutIncludesResponse](./bundleidcapabilitieswithoutincludesresponse.md)
  A response that contains a single Bundle IDs capability resource without includes.
- [object CapabilitySetting](./capabilitysetting.md)
  An object that  represents a capability setting for an app.
- [type CapabilityType](./capabilitytype.md)
  String that represents an app’s capability type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/capabilityoption)*