# Managed Application Feedback

**Framework**: Device Management  
**Kind**: httpRequest

Get app feedback from a managed app on the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad, tvOS, visionOS |
| User channel | macOS |
| Requires supervision | macOS |
| Allowed in user enrollment | iOS, visionOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object ManagedApplicationFeedbackCommand](managedapplicationfeedbackcommand.md)
  The command to get app feedback from a managed app on the device.
- [object ManagedApplicationFeedbackResponse](managedapplicationfeedbackresponse.md)
  A response from the device after it processes the command to get app feedback from a managed app on the device.

## Request Body

The request object the server returns for the Managed Application Feedback Command.

## See Also

- [Install Application](install-application-command.md)
  Install a third-party app on a device.
- [Install Enterprise Application](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Apply Redemption Code](apply-redemption-code-command.md)
  Complete the installation of an app using a redemption code.
- [Remove Application](remove-application-command.md)
  Remove an installed managed app.
- [Validate Applications](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [Managed Application List](managed-application-list-command.md)
  Get the status of all managed apps on a device.
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-application-feedback-command)*