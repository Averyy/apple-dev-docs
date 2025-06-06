# Apply a Redemption Code

**Framework**: Device Management  
**Kind**: httpRequest

Complete the installation of an app using a redemption code.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Sending a redemption code to an app that doesn’t need it produces an error.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Command and Response
- [object ApplyRedemptionCodeCommand](applyredemptioncodecommand.md)
  The command to send a redemption code to complete installation of an app on a device.
- [object ApplyRedemptionCodeResponse](applyredemptioncoderesponse.md)
  A response from the device after it processes the command to complete the installation of an app using a redemption code.

## Request Body

The command to send a redemption code to complete installation of an app on a device.

## See Also

- [Install an App](install-application-command.md)
  Install a third-party app on a device.
- [Install an Enterprise App](install-enterprise-application-command.md)
  Install an enterprise app on a device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apply-redemption-code-command)*