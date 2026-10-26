# MdmServer

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents device management services in organizations.

**Availability**:
- Apple School Manager API 1.7+

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
- [object AppleCareCoverage](./applecarecoverage.md)
  The data structure that represents an AppleCare coverage resource that belongs to an organization device.
- [object AppleCareCoverageResponse](./applecarecoverageresponse.md)
  A response that contains a list of AppleCare coverage resources that belongs to an organization device.
- [object PagedDocumentLinks](./pageddocumentlinks.md)
  Links related to the response document, including paging links.
- [object PagingInformation](./paginginformation.md)
  Paging information for data responses.
- [object RelationshipLinks](./relationshiplinks.md)
  Links related to the response document, including self-links.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/mdmserver)*