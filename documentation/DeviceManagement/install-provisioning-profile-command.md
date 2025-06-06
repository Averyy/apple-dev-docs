# Install a Provisioning Profile

**Framework**: Device Management  
**Kind**: httpRequest

Install a provisioning profile on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Installing Profiles on Devices](installing-profiles-on-devices.md)

#### Discussion

No error occurs if the provisioning profile is already present.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS |
| Required Access Right | AllowProvisioningInstallationRemoval |

##### Example Request and Response

## Topics

### Command and Response
- [object InstallProvisioningProfileCommand](installprovisioningprofilecommand.md)
  The command to install a provisioning profile on a device.
- [object InstallProvisioningProfileResponse](installprovisioningprofileresponse.md)
  A response from the device after it processes the command to install a provisioning profile.

## Request Body

The command to install a provisioning profile on a device.

## See Also

- [Install a Profile](install-profile-command.md)
  Install a configuration profile on a device.
- [List the Installed Profiles](profile-list-command.md)
  Get a list of installed profiles on a device.
- [Remove a Profile](remove-profile-command.md)
  Remove a previously installed profile from the device.
- [List the Installed Provisioning Profiles](provisioning-profile-list-command.md)
  Get a list of installed provisioning profiles on a device.
- [Remove a Provisioning Profile](remove-provisioning-profile-command.md)
  Remove a previously installed provisioning profile from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/install-provisioning-profile-command)*