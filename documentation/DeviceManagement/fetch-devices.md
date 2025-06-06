# Get a List of Devices

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of devices that are managed by the server.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This request fetches a list of all devices that are assigned to this MDM server at the time of the request. This service should be used for loading an initial list of devices into the MDM server’s data store. Once the list of devices is loaded, [`Sync the List of Devices`](sync-devices.md) to update the list.

This request provides a limited number of entries per request, using cursors to provide position information across requests.

## Topics

### Request and Response
- [object FetchDeviceRequest](fetchdevicerequest.md)
  The request for a list of devices.
- [object FetchDeviceResponse](fetchdeviceresponse.md)
  The response that contains a list of devices.

## Request Body

The request for a list of devices.

## See Also

- [Activation Lock a Device](activation-lock-devices.md)
  Enable activation lock on a remote device.
- [Get Device Details](device-details.md)
  Get the details on a set of devices.
- [Sync the List of Devices](sync-devices.md)
  Get updates about the list of devices the server manages.
- [Disown Devices](disown-devices.md)
  Notify Apple’s servers that your organization no longer owns the specified devices.
- [Get Beta Enrollment Tokens](get-beta-enrollment-tokens.md)
  Retrieves the beta enrollment tokens available for the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-devices)*