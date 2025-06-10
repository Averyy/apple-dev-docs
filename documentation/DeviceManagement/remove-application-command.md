# Remove Application

**Framework**: Device Management  
**Kind**: httpRequest

Remove an installed managed app.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

This command only applies to managed apps and also removes the data for the removed app.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | iOS, visionOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object RemoveApplicationCommand](removeapplicationcommand.md)
  The command to remove an installed managed app.
- [object RemoveApplicationResponse](removeapplicationresponse.md)
  A response from the device after it processes the command to remove an installed managed app.

## Request Body

The request object the server returns for the Remove Application Command.

## See Also

- [Install Application](install-application-command.md)
  Install a third-party app on a device.
- [Install Enterprise Application](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Apply Redemption Code](apply-redemption-code-command.md)
  Complete the installation of an app using a redemption code.
- [Validate Applications](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [Managed Application List](managed-application-list-command.md)
  Get the status of all managed apps on a device.
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/remove-application-command)*