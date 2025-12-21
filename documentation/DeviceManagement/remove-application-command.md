# Remove Application

**Framework**: Device Management  
**Kind**: httpRequest

Remove an app.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

This command allows a server to remove managed apps. It also allows a server to remove unmanaged and system deletable apps on supervised devices in iOS 26 and later, tvOS 26 and later, visionOS 26 and later, and watchOS 26 and later. When the device removes an app, it also removes the data for the app.

This command fails for apps that Declarative Device Management is managing.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object RemoveApplicationCommand](removeapplicationcommand.md)
  The command to remove an app.
- [object RemoveApplicationResponse](removeapplicationresponse.md)
  A response from the device after it processes the command to remove an app.

## Request Body

The request object the server returns for the Remove Application Command.

## See Also

- [Install Application](install-application-command.md)
  Install a third-party app on a device.
- [Install Enterprise Application](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Installed Application List](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Managed Application List](managed-application-list-command.md)
  Get the status of all managed apps on a device.
- [Apply Redemption Code](apply-redemption-code-command.md)
  Complete the installation of an app using a redemption code.
- [Validate Applications](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/remove-application-command)*