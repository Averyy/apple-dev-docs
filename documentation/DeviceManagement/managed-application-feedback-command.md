# Get App Feedback

**Framework**: Device Management  
**Kind**: httpRequest

Get app feedback from a managed app on the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad, tvOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS |
| Required Access Right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Command and Response
- [object ManagedApplicationFeedbackCommand](managedapplicationfeedbackcommand.md)
  The command to get managed app feedback on a device.
- [object ManagedApplicationFeedbackResponse](managedapplicationfeedbackresponse.md)
  A response from the device after it processes the command to get app feedback from a managed app.

## Request Body

The command to get managed app feedback on a device.

## See Also

- [Install an App](install-application-command.md)
  Install a third-party app on a device.
- [Install an Enterprise App](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Apply a Redemption Code](apply-redemption-code-command.md)
  Complete the installation of an app using a redemption code.
- [Remove an App](remove-application-command.md)
  Remove an installed managed app.
- [Validate Apps](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [List the Managed Apps](managed-application-list-command.md)
  Get the status of all managed apps on a device.
- [Query App Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Get App Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-application-feedback-command)*