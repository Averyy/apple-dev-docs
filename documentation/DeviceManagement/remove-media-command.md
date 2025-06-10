# Remove Media

**Framework**: Device Management  
**Kind**: httpRequest

Remove a previously installed book from a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | iOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object RemoveMediaCommand](removemediacommand.md)
  The command to remove a previously installed book from a device.
- [object RemoveMediaResponse](removemediaresponse.md)
  A response from the device after it processes the command to remove a previously installed book from a device.

## Request Body

The request object the server returns for the Remove Media Command.

## See Also

- [Install Media](install-media-command.md)
  Install a book on a device.
- [Managed Media List](managed-media-list-command.md)
  Get a list of the managed books on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/remove-media-command)*