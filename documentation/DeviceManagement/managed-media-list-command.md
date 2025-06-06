# List the Managed Media

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of the managed books on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

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
- [object ManagedMediaListCommand](managedmedialistcommand.md)
  The command to get a list of the managed books on a device.
- [object ManagedMediaListResponse](managedmedialistresponse.md)
  A response from the device after it processes the command to get a list of managed books.

## Request Body

The command to get a list of the managed books on a device.

## See Also

- [Install Media](install-media-command.md)
  Install a book on a device.
- [Remove Media](remove-media-command.md)
  Remove a previously installed book from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-media-list-command)*