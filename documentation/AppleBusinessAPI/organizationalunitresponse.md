# OrganizationalUnitResponse

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

A response that contains a single organizational unit resource.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object OrganizationalUnitResponse
```

## Properties

- `data` (OrganizationalUnit) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

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
- [object MdmDeviceDetail](./mdmdevicedetail.md)
  The data structure that represents the detailed information for a device management service enrolled device resource.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/organizationalunitresponse)*