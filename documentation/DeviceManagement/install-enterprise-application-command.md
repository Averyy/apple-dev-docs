# Install an Enterprise App

**Framework**: Device Management  
**Kind**: httpRequest

Install an enterprise app on a device.

**Availability**:
- macOS 10.13.6+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command provides a more secure version of `InstallApplication` that specifies a `ManifestURL`. The request must contain either `Manifest` or `ManifestURL`. Using `Manifest` ignores the pinning options. When using `ManifestURL`, specify the pinning options to increase security. In macOS, the device returns an `Acknowledged` response after validating the parameters, but before downloading and installing the app. Howevever, it doesn’t notify the MDM server about errors that occur during the installation process.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | macOS |
| Required Access Right | AllowPasscodeRemovalAndLock |

##### Example Request and Response

## Topics

### Command and Response
- [object InstallEnterpriseApplicationCommand](installenterpriseapplicationcommand.md)
  The command to install an enterprise app on a device.
- [object InstallEnterpriseApplicationResponse](installenterpriseapplicationresponse.md)
  A response from the device after it processes the command to install an enterprise app.

## Request Body

The command to install an enterprise app on a device.

## See Also

- [Install an App](install-application-command.md)
  Install a third-party app on a device.
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
- [Get App Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/install-enterprise-application-command)*