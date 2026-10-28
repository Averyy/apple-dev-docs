# Define a Profile

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Define a profile that can be distributed to the devices in your organization.

**Availability**:
- Device Assignment Services 5.0+

## Discussion

This service defines a profile with Apple’s servers that can then be assigned to specific devices. This command provides information about the MDM server that is assigned to manage one or more devices, information about the host that the managed devices can pair with, and various attributes that control the MDM association behavior of the device.

## Topics

### Request and Response
- [object DefineProfileResponse](./defineprofileresponse.md)
- [object DefineProfileResponse.Devices](./defineprofileresponse/devices-data.dictionary.md)

## Endpoint

`POST https://mdmenrollment.apple.com/profile`

## Request Body

**Content-Type**: `application/json`  
**Type**: `Profile`

A profile’s properties and their values.

## Responses

- `200` OK (`DefineProfileResponse`, `application/json`)
- `400` Bad Request:

  - `CONFIG_NAME_INVALID`: The `profile_name` field in the uploaded profile is either empty or has exceeded the maximum allowed length (125 UTF-8 characters).
  - `CONFIG_NAME_REQUIRED`: The configuration name is missing in the uploaded profile.
  - `CONFIG_URL_INVALID`: The URL field in the uploaded profile is either empty or has exceeded the maximum allowed length (2000 URL encoded characters). The syntax of the URL is defined by RFC 2396: Uniform Resource Identifiers (URI):  Generic Syntax, amended by RFC 2732: Format for Literal IPv6 Addresses in URLs.
  - `CONFIG_URL_REQUIRED`: The MDM server URL is missing in the uploaded profile.
  - `DEPARTMENT_INVALID`: The `department` field in the uploaded profile is either empty or has exceeded the maximum allowed length (125 UTF-8 characters).
  - `FLAGS_INVALID`: The flags have been set incorrectly; `is_mdm_removable` can be set to `false` only if flag `is_supervised` is set to `true`.
  - `LOCALE_INVALID`: The locale fields combination is invalid or unsupported.
  - `MAGIC_INVALID`: The magic field in the uploaded profile is either empty or has exceeded the maximum allowed length (256 UTF-8 characters).
  - `SUPPORT_EMAIL_INVALID`: The `support_email_address` field in the uploaded profile is either empty or has exceeded the maximum allowed length (250 UTF-8 characters).
  - `SUPPORT_PHONE_INVALID`: The `support_phone_number` field in the uploaded profile is either empty or has exceeded the maximum allowed length (50 UTF-8 characters).
  - `USER_AGENT_INVALID:`  The `User-Agent` header is invalid.
  - `USER_AGENT_MISSING:`  The `User-Agent` header is missing or has no assigned value.

## See Also

### Profile management
- [Get a Profile](./fetch-profile.md)
  Get details about a profile.
- [Assign a Profile](./assign-profile.md)
  Assign a profile to a list of devices.
- [Remove a Profile](./clear-device-profile.md)
  Remove a profile from a list of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/define-profile)*