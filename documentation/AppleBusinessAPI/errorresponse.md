# ErrorResponse

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The error details that an API returns in the response body whenever the API request isn’t successful.

**Availability**:
- Apple Business API 2.6+

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

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/errorresponse)*