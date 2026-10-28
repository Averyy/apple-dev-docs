# Remove a Profile

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a profile from a list of devices.

**Availability**:
- Device Assignment Services 5.0+

## Discussion

After this call, the devices in the list will have no profiles associated with them. However, if those devices have already obtained the profile, this has no effect until the device is wiped and activated again.

## Topics

### Request and Response
- [object ClearProfileRequest](./clearprofilerequest.md)
  The request used to remove a profile from devices.
- [object ClearProfileResponse](./clearprofileresponse.md)
- [object ClearProfileResponse.Devices](./clearprofileresponse/devices-data.dictionary.md)

## Endpoint

`DELETE https://mdmenrollment.apple.com/profile/devices`

## Request Body

**Content-Type**: `application/json`  
**Type**: `ClearProfileRequest`

The request used to remove a profile from devices.

## Responses

- `200` OK (`ClearProfileResponse`, `application/json`)
- `400` Bad Request:

  - `DEVICE_ID_REQUIRED`: The request did not contain any device IDs.
  - `USER_AGENT_INVALID:`  The `User-Agent` header is invalid.
  - `USER_AGENT_MISSING:`  The `User-Agent` header is missing or has no assigned value.

## See Also

### Profile management
- [Define a Profile](./define-profile.md)
  Define a profile that can be distributed to the devices in your organization.
- [Get a Profile](./fetch-profile.md)
  Get details about a profile.
- [Assign a Profile](./assign-profile.md)
  Assign a profile to a list of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-device-profile)*