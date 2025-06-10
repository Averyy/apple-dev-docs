# NSExtension Mappings

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of the installed extensions for a user on a device.

**Availability**:
- macOS 10.13+

#### Discussion

This list is a superset of the list that [`ActiveNSExtensionsCommand`](activensextensionscommand.md) returns. It may contain extensions that the system never enables due to various restrictions.

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
- [object NSExtensionMappingsCommand](nsextensionmappingscommand.md)
  The command to get a list of the installed extensions for a user on a device.
- [object NSExtensionMappingsResponse](nsextensionmappingsresponse.md)
  A response from the device after it processes the command to get a list of the installed extensions for a user on a device.

## Request Body

The request object the server returns for the NSExtension Mappings Command.

## See Also

- [Active NSExtensions](active-nsextensions-command.md)
  Get a list of active extensions for a user on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/nsextension-mappings-command)*