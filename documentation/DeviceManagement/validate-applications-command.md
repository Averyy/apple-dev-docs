# Validate Applications

**Framework**: Device Management  
**Kind**: httpRequest

Force validation of developer and universal provisioning profiles for enterprise apps.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- tvOS 10.2+
- visionOS 1.1+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad, tvOS, visionOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, visionOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object ValidateApplicationsCommand](validateapplicationscommand.md)
  The command to force validation of developer and universal provisioning profiles for enterprise apps.
- [object ValidateApplicationsResponse](validateapplicationsresponse.md)
  A response from the device after it processes the command to force validation of developer and universal provisioning profiles for enterprise apps.

## Request Body

The request object the server returns for the Validate Applications Command.

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
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/validate-applications-command)*