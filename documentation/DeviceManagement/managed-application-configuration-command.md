# Managed Application Configuration

**Framework**: Device Management  
**Kind**: httpRequest

Get app configurations from managed apps on a device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.15+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

This command allows the server to get the configuration of managed apps.

The response doesn’t include apps that Declarative Device Management is managing.

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
- [object ManagedApplicationConfigurationCommand](managedapplicationconfigurationcommand.md)
  The command to get app configurations from managed apps on a device.
- [object ManagedApplicationConfigurationResponse](managedapplicationconfigurationresponse.md)
  A response from the device after it processes the command to get app configurations from managed apps on a device.

## Request Body

The request object the server returns for the Managed Application Configuration Command.

## See Also

- [Install Application](install-application-command.md)
  Install a third-party app on a device.
- [Install Enterprise Application](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Installed Application List](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Managed Application List](managed-application-list-command.md)
  Get the status of all managed apps on a device.
- [Remove Application](remove-application-command.md)
  Remove an app.
- [Apply Redemption Code](apply-redemption-code-command.md)
  Complete the installation of an app using a redemption code.
- [Validate Applications](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-application-configuration-command)*