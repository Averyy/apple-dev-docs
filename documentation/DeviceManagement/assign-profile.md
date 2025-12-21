# Assign a Profile

**Framework**: Device Management  
**Kind**: httpRequest

Assign a profile to a list of devices.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Migrating managed devices](migrating-managed-devices.md)

#### Discussion

To avoid performance issues, limit requests to 1000 devices at a time.

## Topics

### Request and Response
- [object ProfileServiceRequest](profileservicerequest.md)
  The request for assigning a profile to a set of devices.
- [object AssignProfileResponse](assignprofileresponse.md)
- [object AssignProfileResponse.Devices](assignprofileresponse/devices-data.dictionary.md)

## Request Body

The request for assigning a profile to a set of devices.

## See Also

- [Define a Profile](define-profile.md)
  Define a profile that can be distributed to the devices in your organization.
- [Get a Profile](fetch-profile.md)
  Get details about a profile.
- [Remove a Profile](clear-device-profile.md)
  Remove a profile from a list of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assign-profile)*