# Install Application

**Framework**: Device Management  
**Kind**: httpRequest

Install a third-party app on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

If the app is a managed app, this command updates it. The request must contain only one of these keys: `iTunesStoreID`, `Identifier`, or `ManifestURL`.

Installation prompts the user to approve or cancel the update. If the device is supervised, the device only prompts when the app to install is in the foreground.

Set the organization name that appears in this prompt in the `OrganizationInfo` dictionary using the `Settings` command.

In macOS, the device returns an `Acknowledged` response after validating the parameters, but before downloading and installing the app. However, it doesn’t notify the MDM server about errors that occur during the installation process.

For macOS VPP app installations, if the app is device licensed, the system must receive the `InstallApplication` command on the device channel. If the app is user licensed, the system must receive the `InstallApplication` command on the user channel.

Prior to iOS 16.0 and tvOS 16.0, this command would return `NotNow` when Setup Assistant was running. Starting in iOS 16.0 and tvOS 16.0, the command may be sent to supervised devices during Setup Assistant. However, you should only attempt to install device-based VPP apps or enterprise apps while in the awaiting configuration state, as it is unlikely the device would have an App Store account configured, and thus commands that depend on one will fail.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response Enterprise App

##### Example Request and Response Vpp App

## Topics

### Commands and responses
- [object InstallApplicationCommand](installapplicationcommand.md)
  The command to install a third-party app on a device.
- [object InstallApplicationResponse](installapplicationresponse.md)
  A response from the device after it processes the command to install a third-party app on a device.

## Request Body

The request object the server returns for the Install Application Command.

## See Also

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
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/install-application-command)*