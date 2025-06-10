# Remove a Profile

**Framework**: Device Management  
**Kind**: httpRequest

Remove a profile from a list of devices.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

After this call, the devices in the list will have no profiles associated with them. However, if those devices have already obtained the profile, this has no effect until the device is wiped and activated again.

## Topics

### Request and Response
- [object ClearProfileRequest](clearprofilerequest.md)
  The request used to remove a profile from devices.
- [object ClearProfileResponse](clearprofileresponse.md)
- [object ClearProfileResponse.Devices](clearprofileresponse/devices-data.dictionary.md)

## Request Body

The request used to remove a profile from devices.

## See Also

- [Define a Profile](define-profile.md)
  Define a profile that can be distributed to the devices in your organization.
- [Get a Profile](fetch-profile.md)
  Get details about a profile.
- [Assign a Profile](assign-profile.md)
  Assign a profile to a list of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-device-profile)*