# Get Device Details

**Framework**: Device Management  
**Kind**: httpRequest

Get the details on a set of devices.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

## Topics

### Request and Response
- [object DeviceListRequest](devicelistrequest.md)
  The request for a list of devices.
- [object DeviceListResponse](devicelistresponse.md)
  The response that contains a list of devices.
- [object DeviceListResponse.Devices](devicelistresponse/devices-data.dictionary.md)
  A dictionary of devices, with their serial numbers.

## Request Body

The request for a list of devices.

## See Also

- [Activation Lock a Device](activation-lock-devices.md)
  Enable activation lock on a remote device.
- [Get a List of Devices](fetch-devices.md)
  Get a list of devices that are managed by the server.
- [Sync the List of Devices](sync-devices.md)
  Get updates about the list of devices the server manages.
- [Disown Devices](disown-devices.md)
  Notify Apple’s servers that your organization no longer owns the specified devices.
- [Get Beta Enrollment Tokens](get-beta-enrollment-tokens.md)
  Retrieves the beta enrollment tokens available for the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-details)*