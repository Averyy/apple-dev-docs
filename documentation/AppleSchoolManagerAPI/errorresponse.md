# ErrorResponse

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

The error details that an API returns in the response body whenever the API request isn’t successful.

**Availability**:
- Apple School Manager API 1.7+

## Declaration

```
object ErrorResponse
```

### Example response

```json
     {
       "errors": [
         {
           "id": "d41f0ce2-8e12-41b7-bffd-91fd628f6628",
           "status": "404",
           "code": "NOT_FOUND",
           "title": "The specified resource doesn't exist",
           "detail": "There is no resource of type 'orgDevices' with id 'XABC123X0ABC123X0'"
         }
       ]
     }
```

## Topics

### Dictionaries
- [object ErrorResponse.Errors](./errorresponse/errors-data.dictionary.md)
  The details about an error that returns when an API request isn’t successful.

## Properties

- `errors` ([ErrorResponse.Errors]): An array of one or more errors.

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
- [object PagedDocumentLinks](./pageddocumentlinks.md)
  Links related to the response document, including paging links.
- [object PagingInformation](./paginginformation.md)
  Paging information for data responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/errorresponse)*