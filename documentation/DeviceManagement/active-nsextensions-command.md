# List Active NSExtensions

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of active extensions for a user on a device.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command returns information about the active extensions for a user. Extensions exist for each user, not for the device.

Extensions restricted from executing by Application Launch Restrictions or the [`NSExtensionManagement`](nsextensionmanagement.md) configuration profile won’t appear in the response.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | - |
| User Channel | macOS |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | QueryInstalledApps |

##### Example Request and Response

## Topics

### Command and Response
- [object ActiveNSExtensionsCommand](activensextensionscommand.md)
  The command to get a list of active extensions for a user on a device.
- [object ActiveNSExtensionsResponse](activensextensionsresponse.md)
  A response from the device after it processes the command to get a list of active extensions for a user.

## Request Body

The command to get a list of active extensions for a user on a device.

## See Also

- [List the NSExtensions](nsextension-mappings-command.md)
  Get a list of the installed extensions for a user on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/active-nsextensions-command)*