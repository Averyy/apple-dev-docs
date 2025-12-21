# Install Enterprise Application

**Framework**: Device Management  
**Kind**: httpRequest

Install an enterprise app on a device.

**Availability**:
- macOS 10.13.6+

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

This command provides a more secure version of the `InstallApplication` command when that uses a `ManifestURL`. The request must contain either `Manifest` or `ManifestURL`. Using `Manifest` ignores the pinning options. When using `ManifestURL`, specify the pinning options to increase security. In macOS, the device returns an `Acknowledged` response after validating the parameters, but before downloading and installing the app. However, it doesn’t notify the MDM server about errors that occur during the installation process.

This command fails if Declarative Device Management is managing the app.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | macOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object InstallEnterpriseApplicationCommand](installenterpriseapplicationcommand.md)
  The command to install an enterprise app on a device.
- [object InstallEnterpriseApplicationResponse](installenterpriseapplicationresponse.md)
  A response from the device after it processes the command to install an enterprise app on a device.

## Request Body

The request object the server returns for the Install Enterprise Application Command.

## See Also

- [Install Application](install-application-command.md)
  Install a third-party app on a device.
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
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/install-enterprise-application-command)*