# PagedDocumentLinks

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

Links related to the response document, including paging links.

**Availability**:
- Apple School Manager API 1.8+

## Declaration

```
object PagedDocumentLinks
```

## Properties

- `first` (uri-reference): The link to the first page of documents.
- `next` (uri-reference): The link to the next page of documents.
- `self` (uri-reference) *(required)*: The link that produces the current document.

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
- [object PagingInformation](./paginginformation.md)
  Paging information for data responses.
- [object RelationshipLinks](./relationshiplinks.md)
  Links related to the response document, including self-links.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/pageddocumentlinks)*