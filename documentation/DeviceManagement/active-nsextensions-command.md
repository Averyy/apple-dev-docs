# Active NSExtensions

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of active extensions for a user on a device.

**Availability**:
- macOS 10.13+

#### Discussion

This command returns information about the active extensions for a user. Extensions exist for each user, not for the device.

Extensions restricted from executing by Application Launch Restrictions or the [`NSExtensionManagement`](nsextensionmanagement.md) configuration profile won’t appear in the response.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | NA |
| User channel | macOS |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | QueryInstalledApps |

##### Example Request and Response

## Topics

### Commands and responses
- [object ActiveNSExtensionsCommand](activensextensionscommand.md)
  The command to get a list of active extensions for a user on a device.
- [object ActiveNSExtensionsResponse](activensextensionsresponse.md)
  A response from the device after it processes the command to get a list of active extensions for a user on a device.

## Request Body

The request object the server returns for the Active NSExtensions Command.

## See Also

- [NSExtension Mappings](nsextension-mappings-command.md)
  Get a list of the installed extensions for a user on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/active-nsextensions-command)*