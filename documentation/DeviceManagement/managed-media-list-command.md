# Managed Media List

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of the managed books on a device.

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
- [object ManagedMediaListCommand](managedmedialistcommand.md)
  The command to get a list of the managed books on a device.
- [object ManagedMediaListResponse](managedmedialistresponse.md)
  A response from the device after it processes the command to get a list of the managed books on a device.

## Request Body

The request object the server returns for the Managed Media List Command.

## See Also

- [Install Media](install-media-command.md)
  Install a book on a device.
- [Remove Media](remove-media-command.md)
  Remove a previously installed book from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-media-list-command)*