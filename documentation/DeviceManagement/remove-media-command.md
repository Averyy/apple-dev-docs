# Remove Media

**Framework**: Device Management  
**Kind**: httpRequest

Remove a previously installed book from a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS |
| Required Access Right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Command and Response
- [object RemoveMediaCommand](removemediacommand.md)
  The command to remove an installed book from a device.
- [object RemoveMediaResponse](removemediaresponse.md)
  A response from the device after it processes the command to remove a book from a device.

## Request Body

The command to remove an installed book from a device.

## See Also

- [Install Media](install-media-command.md)
  Install a book on a device.
- [List the Managed Media](managed-media-list-command.md)
  Get a list of the managed books on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/remove-media-command)*