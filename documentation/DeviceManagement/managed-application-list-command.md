# Managed Application List

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

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

This command returns the status of managed apps from the App Store.

Some statuses are transient and the device removes them after reporting them to the server.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object ManagedApplicationListCommand](managedapplicationlistcommand.md)
  The command to get the status of all managed apps on a device.
- [object ManagedApplicationListResponse](managedapplicationlistresponse.md)
  A response from the device after it processes the command to get the status of all managed apps on a device.

## Request Body

The request object the server returns for the Managed Application List Command.

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
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-application-list-command)*