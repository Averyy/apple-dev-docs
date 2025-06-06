# List the Installed Profiles

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of installed profiles on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS, Shared iPad |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS, macOS |
| Required Access Right | AllowInspection |

##### Example Request and Response

## Topics

### Command and Response
- [object ProfileListCommand](profilelistcommand.md)
  The command to get a list of installed profiles on a device.
- [object ProfileListResponse](profilelistresponse.md)
  A response from the device after it processes the command to get a list of installed profiles.

## Request Body

The command to get a list of installed profiles on a device.

## See Also

- [Install a Profile](install-profile-command.md)
  Install a configuration profile on a device.
- [Remove a Profile](remove-profile-command.md)
  Remove a previously installed profile from the device.
- [Install a Provisioning Profile](install-provisioning-profile-command.md)
  Install a provisioning profile on a device.
- [List the Installed Provisioning Profiles](provisioning-profile-list-command.md)
  Get a list of installed provisioning profiles on a device.
- [Remove a Provisioning Profile](remove-provisioning-profile-command.md)
  Remove a previously installed provisioning profile from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profile-list-command)*