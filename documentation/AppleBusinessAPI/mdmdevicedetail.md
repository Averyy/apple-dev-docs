# MdmDeviceDetail

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents the detailed information for a device management service enrolled device resource.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object MdmDeviceDetail
```

## Topics

### Dictionaries
- [object MdmDeviceDetail.Attributes](./mdmdevicedetail/attributes-data.dictionary.md)
  The attributes for a device management service enrolled device detail resource.

## Properties

- `attributes` (MdmDeviceDetail.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `mdmDeviceDetails`

## See Also

### Objects and Data Types
- [object OrgDevice](./orgdevice.md)
  The data structure that represents an organization device resource.
- [object OrgDeviceResponse](./orgdeviceresponse.md)
  A response that contains a single organization device resource.
- [object OrgDevicesResponse](./orgdevicesresponse.md)
  A response that contains a list of organization device resources.
- [object OrgDeviceAssignedServerLinkageResponse](./orgdeviceassignedserverlinkageresponse.md)
  The data and links that describe the relationship between the resources.
- [object MdmDevice](./mdmdevice.md)
  The data structure that represents a device management service enrolled device resource.
- [object MdmDeviceResponse](./mdmdeviceresponse.md)
  A response that contains a list of Apple devices enrolled in a device management service.
- [object MdmDevicesResponse](./mdmdevicesresponse.md)
  A response that contains a list of Apple devices enrolled in a device management service.
- [object MdmDeviceDetailResponse](./mdmdevicedetailresponse.md)
  A response that contains the detailed information for an Apple device enrolled in a device management service.
- [object MdmServer](./mdmserver.md)
  The data structure that represents a device management service resource in an organization.
- [object MdmServerResponse](./mdmserverresponse.md)
  A response that contains a single device management service resource.
- [object MdmServersResponse](./mdmserversresponse.md)
  A response that contains a list of device management service resources.
- [object MdmServerDevicesLinkagesResponse](./mdmserverdeviceslinkagesresponse.md)
  The data and links that describe the relationship between the resources.
- [object OrgDeviceActivity](./orgdeviceactivity.md)
  The data structure that represents an organization device activity resource.
- [object OrgDeviceActivityCreateRequest](./orgdeviceactivitycreaterequest.md)
  The request body you use to update the device management service for a device.
- [object OrgDeviceActivityResponse](./orgdeviceactivityresponse.md)
  A response that contains a single organization device activity resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/mdmdevicedetail)*