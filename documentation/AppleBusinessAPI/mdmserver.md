# MdmServer

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents a device management service resource in an organization.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
object MdmServer
```

## Topics

### Related Types
- [type MdmServerStatus](./mdmserverstatus.md)
  Strings that represent the operational status of a device management service.
- [type MdmServerProductFamily](./mdmserverproductfamily.md)
  Strings that represent a product family that can be assigned as a default to a device management service.
- [object MdmServerCertificate](./mdmservercertificate.md)
  The X.509 certificate to associate with a device management service.
### Dictionaries
- [object MdmServer.Attributes](./mdmserver/attributes-data.dictionary.md)
  Attributes that describe a device management service resource.
- [object MdmServer.Relationships](./mdmserver/relationships-data.dictionary.md)
  The relationships you include in the request, and those that you can operate on.

## Properties

- `attributes` (MdmServer.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (MdmServer.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `mdmServers`

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

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/mdmserver)*