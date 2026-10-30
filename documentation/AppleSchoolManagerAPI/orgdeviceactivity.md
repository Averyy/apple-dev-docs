# OrgDeviceActivity

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents an organization device activity resource.

**Availability**:
- Apple School Manager API 1.8+

## Declaration

```
object OrgDeviceActivity
```

## Topics

### Dictionaries
- [object OrgDeviceActivity.Attributes](./orgdeviceactivity/attributes-data.dictionary.md)
  Attributes that describe an organization device activity resource.

## Properties

- `attributes` (OrgDeviceActivity.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `orgDeviceActivities`

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
- [object MdmServer](./mdmserver.md)
  The data structure that represents device management services in organizations.
- [object MdmServerResponse](./mdmserverresponse.md)
  A response that contains a single device management service resource.
- [object MdmServersResponse](./mdmserversresponse.md)
  A response that contains a list of device management service resources.
- [object MdmServerDevicesLinkagesResponse](./mdmserverdeviceslinkagesresponse.md)
  The data and links that describe the relationship between the resources.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/orgdeviceactivity)*