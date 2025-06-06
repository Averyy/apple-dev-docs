# Define a Profile

**Framework**: Device Management  
**Kind**: httpRequest

Define a profile that can be distributed to the devices in your organization.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This service defines a profile with Apple’s servers that can then be assigned to specific devices. This command provides information about the MDM server that is assigned to manage one or more devices, information about the host that the managed devices can pair with, and various attributes that control the MDM association behavior of the device.

## Topics

### Request and Response
- [object DefineProfileResponse](defineprofileresponse.md)
  The response to defining a profile.
- [object DefineProfileResponse.Devices](defineprofileresponse/devices-data.dictionary.md)
  A dictionary containing device information.

## Request Body

A profile’s properties and their values.

## See Also

- [Get a Profile](fetch-profile.md)
  Get details about a profile.
- [Assign a Profile](assign-profile.md)
  Assign a profile to a list of devices.
- [Remove a Profile](clear-device-profile.md)
  Remove a profile from a list of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/define-profile)*