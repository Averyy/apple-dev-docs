# BundleIdCapabilitiesResponse

**Framework**: Enterprise Program API  
**Kind**: dictionary  
**Role**: Object

A response that contains a list of Bundle ID Capability resources.

## Declaration

```
object BundleIdCapabilitiesResponse
```

## Properties

- `data` ([BundleIdCapability]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

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
- [object BundleIdCapabilitiesWithoutIncludesResponse](./bundleidcapabilitieswithoutincludesresponse.md)
  A response that contains a single Bundle IDs capability resource without includes.
- [object CapabilityOption](./capabilityoption.md)
  An option within a capability setting.
- [object CapabilitySetting](./capabilitysetting.md)
  An object that  represents a capability setting for an app.
- [type CapabilityType](./capabilitytype.md)
  String that represents an app’s capability type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/bundleidcapabilitiesresponse)*