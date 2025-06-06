# List the Managed Apps

**Framework**: Device Management  
**Kind**: httpRequest

Get the status of all managed apps on a device.

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

This command returns the status of managed apps from the App Store.

Some statuses are transient and the device removes them after reporting them to the server.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS, macOS |
| Required Access Right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Command and Response
- [object ManagedApplicationListCommand](managedapplicationlistcommand.md)
  The command to get the status of managed apps on a device.
- [object ManagedApplicationListResponse](managedapplicationlistresponse.md)
  A response from the device after it processes the command to get the status of all managed apps.

## Request Body

The command to get the status of managed apps on a device.

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
- [Query App Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Get App Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Get App Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-application-list-command)*