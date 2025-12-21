# Remove Provisioning Profile

**Framework**: Device Management  
**Kind**: httpRequest

Remove a previously installed provisioning profile from a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

> **Note**:  Don’t remove a provisioning profile to revoke access to an enterprise app. An app continues to be usable until the device restarts, even with no provisioning profile. Provisioning profiles also synchronize with iTunes and the system reinstalls them when users sync devices. For more information on removing apps, see [`Remove Application`](remove-application-command.md).

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowProvisioningInstallationRemoval |

##### Example Request and Response

## Topics

### Commands and responses
- [object RemoveProvisioningProfileCommand](removeprovisioningprofilecommand.md)
  The command to remove a previously installed provisioning profile from a device.
- [object RemoveProvisioningProfileResponse](removeprovisioningprofileresponse.md)
  A response from the device after it processes the command to remove a previously installed provisioning profile from a device.

## Request Body

The request object the server returns for the Remove Provisioning Profile Command.

## See Also

- [Install Profile](install-profile-command.md)
  Install a configuration profile on a device.
- [Profile List](profile-list-command.md)
  Get a list of installed profiles on a device.
- [Remove Profile](remove-profile-command.md)
  Remove a previously installed profile from the device.
- [Install Provisioning Profile](install-provisioning-profile-command.md)
  Install a provisioning profile on a device.
- [Provisioning Profile List](provisioning-profile-list-command.md)
  Get a list of installed provisioning profiles on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/remove-provisioning-profile-command)*