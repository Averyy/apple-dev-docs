# Remove an App

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
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command only applies to managed apps and also removes the data for the removed app.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS |
| Required Access Right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Command and Response
- [object RemoveApplicationCommand](removeapplicationcommand.md)
  The command to remove an installed managed app from a device.
- [object RemoveApplicationResponse](removeapplicationresponse.md)
  A response from the device after it processes the command to remove a managed app.

## Request Body

The command to remove an installed managed app from a device.

## See Also

- [Install an App](install-application-command.md)
  Install a third-party app on a device.
- [Install an Enterprise App](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Apply a Redemption Code](apply-redemption-code-command.md)
  Complete the installation of an app using a redemption code.
- [Validate Apps](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [List the Managed Apps](managed-application-list-command.md)
  Get the status of all managed apps on a device.
- [Query App Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Get App Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Get App Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/remove-application-command)*