# Remove a Profile

**Framework**: Devicemanagement  
**Kind**: httpRequest

Remove a previously installed profile from the device.

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

> **Note**:  Don’t remove a provisioning profile to revoke access to an enterprise app. An app continues to be usable until the device restarts, even with no provisioning profile. Provisioning profiles also synchronize with iTunes and the system reinstalls them when users sync devices. For more information on removing apps, see [`Remove an App`](remove-application-command.md).

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS, Shared iPad |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS, macOS |
| Required Access Right | AllowInstallationRemoval |

##### Example Request and Response

## Topics

### Command and Response
- [object RemoveProfileCommand](removeprofilecommand.md)
  The command to remove a profile from a device.
- [object RemoveProfileResponse](removeprofileresponse.md)
  A response from the device after it processes the command to remove a profile.

## Request Body

The command to remove a profile from a device.

## See Also

- [Install a Profile](install-profile-command.md)
  Install a configuration profile on a device.
- [List the Installed Profiles](profile-list-command.md)
  Get a list of installed profiles on a device.
- [Install a Provisioning Profile](install-provisioning-profile-command.md)
  Install a provisioning profile on a device.
- [List the Installed Provisioning Profiles](provisioning-profile-list-command.md)
  Get a list of installed provisioning profiles on a device.
- [Remove a Provisioning Profile](remove-provisioning-profile-command.md)
  Remove a previously installed provisioning profile from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement/remove-profile-command)*