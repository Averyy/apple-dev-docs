# Assign a Profile

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Assign a profile to a list of devices.

**Availability**:
- Device Assignment Services 5.0+

## Mentions

- [Migrating managed devices](./migrating-managed-devices.md)

#### Discussion

To avoid performance issues, limit requests to 1000 devices at a time.

##### Throttling

With X-Server-Protocol-Version 9 and later, the server may throttle profile assignment on a per-device basis. When the server throttles a device, its value in the `devices` dictionary is `THROTTLED` instead of `SUCCESS`.

With X-Server-Protocol-Version 10 and later, the response also includes `retry_after_seconds` when at least one device is throttled. Clients should wait for at least the indicated number of seconds before retrying assignment for the throttled devices.

## Topics

### Request and Response
- [object ProfileServiceRequest](./profileservicerequest.md)
  The request for assigning a profile to a set of devices.
- [object AssignProfileResponse](./assignprofileresponse.md)
- [object AssignProfileResponse.Devices](./assignprofileresponse/devices-data.dictionary.md)

## Endpoint

`POST https://mdmenrollment.apple.com/profile/devices`

## Request Body

**Content-Type**: `application/json`  
**Type**: `ProfileServiceRequest`

The request for assigning a profile to a set of devices.

## Responses

- `200` OK (`AssignProfileResponse`, `application/json`)
- `400` Bad Request:

  - `DEVICE_ID_REQUIRED`: The request did not contain any device IDs.
  - `PROFILE_UUID_REQUIRED`: The request did not contain a profile ID.
  - `USER_AGENT_INVALID:`  The `User-Agent` header is invalid.
  - `USER_AGENT_MISSING:`  The `User-Agent` header is missing or has no assigned value.
- `404` Not Found: The profile with the specified UUID could not be found.

## See Also

### Profile management
- [Define a Profile](./define-profile.md)
  Define a profile that can be distributed to the devices in your organization.
- [Get a Profile](./fetch-profile.md)
  Get details about a profile.
- [Remove a Profile](./clear-device-profile.md)
  Remove a profile from a list of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assign-profile)*