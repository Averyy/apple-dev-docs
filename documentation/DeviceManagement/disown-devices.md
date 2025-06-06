# Disown Devices

**Framework**: Device Management  
**Kind**: httpRequest

Notify Apple’s servers that your organization no longer owns the specified devices.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Topics

### Response
- [object DeviceStatusResponse](devicestatusresponse.md)
  The request to get the status of a set of devices.
- [object DeviceStatusResponse.Devices](devicestatusresponse/devices-data.dictionary.md)
  A dictionary of devices with their status.

## Request Body

The request for a list of devices.

## See Also

- [Activation Lock a Device](activation-lock-devices.md)
  Enable activation lock on a remote device.
- [Get Device Details](device-details.md)
  Get the details on a set of devices.
- [Get a List of Devices](fetch-devices.md)
  Get a list of devices that are managed by the server.
- [Sync the List of Devices](sync-devices.md)
  Get updates about the list of devices the server manages.
- [Get Beta Enrollment Tokens](get-beta-enrollment-tokens.md)
  Retrieves the beta enrollment tokens available for the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disown-devices)*