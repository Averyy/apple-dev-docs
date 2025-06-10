# Profile List

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

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowInspection |

##### Example Request and Response

## Topics

### Commands and responses
- [object ProfileListCommand](profilelistcommand.md)
  The command to get a list of installed profiles on a device.
- [object ProfileListResponse](profilelistresponse.md)
  A response from the device after it processes the command to get a list of installed profiles on a device.

## Request Body

The request object the server returns for the Profile List Command.

## See Also

- [Install Profile](install-profile-command.md)
  Install a configuration profile on a device.
- [Remove Profile](remove-profile-command.md)
  Remove a previously installed profile from the device.
- [Install Provisioning Profile](install-provisioning-profile-command.md)
  Install a provisioning profile on a device.
- [Provisioning Profile List](provisioning-profile-list-command.md)
  Get a list of installed provisioning profiles on a device.
- [Remove Provisioning Profile](remove-provisioning-profile-command.md)
  Remove a previously installed provisioning profile from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profile-list-command)*