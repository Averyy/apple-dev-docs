# Get a Profile

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a profile.

**Availability**:
- Device Assignment Services 5.0+

## Endpoint

`GET https://mdmenrollment.apple.com/profile`

## Parameters

### Query Parameters

- `profile_uuid` (string) *(required)*: The unique identifier for a profile.

## Responses

- `200` OK (`Profile`, `application/json`)
- `400` Bad Request:

  - `PROFILE_UUID_REQUIRED`: The request did not contain a profile UUID.
  - `NOT_FOUND`: The requested profile UUID doesn’t match a known profile.
  - `USER_AGENT_INVALID:`  The `User-Agent` header is invalid.
  - `USER_AGENT_MISSING:`  The `User-Agent` header is missing or has no assigned value.

## See Also

### Profile management
- [Define a Profile](./define-profile.md)
  Define a profile that can be distributed to the devices in your organization.
- [Assign a Profile](./assign-profile.md)
  Assign a profile to a list of devices.
- [Remove a Profile](./clear-device-profile.md)
  Remove a profile from a list of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-profile)*