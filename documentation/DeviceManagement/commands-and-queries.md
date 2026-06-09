# Commands and queries

**Framework**: Device Management

Remotely execute management commands and queries on managed devices.

#### Overview

The Mobile Device Management (MDM) protocol provides a way to tell a device to remotely execute certain management commands or queries. When a device registers with the device management service, the service sends push notifications to the device when there are commands to process on the device.

When the device receives the notification, it polls the device management service for the command, processes the command, and reports the command results to the service. The device then checks for other commands to process.

> ❗ **Important**:  Device management is for enterprise use only. To use it in your app, the Account Holder of your app’s development team must request the Mobile Device Management capability. For more information, see [`Request a Mobile Device Management Capability`](https://developer.apple.comhttps://developer.apple.com/contact/request/mdm-capability).

## Topics

### Declarative management
- [Declarative Management](declarative-management-command.md)
  Enable your server to support declarative management or trigger a declarative management synchronization operation on the device.
### Profile management
- [Install Profile](install-profile-command.md)
  Install a configuration profile on a device.
- [Profile List](profile-list-command.md)
  Get a list of installed profiles on a device.
- [Remove Profile](remove-profile-command.md)
  Remove a previously installed profile from the device.
- [Install Provisioning Profile](install-provisioning-profile-command.md)
  Install a provisioning profile on a device.
- [Provisioning Profile List](provisioning-profile-list-command.md)
  Get a list of installed provisioning profiles on a device.
- [Remove Provisioning Profile](remove-provisioning-profile-command.md)
  Remove a previously installed provisioning profile from a device.
### Device details
- [Device Information](device-information-command.md)
  Get detailed information about a device.
- [Device Configured](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured](user-configured-command.md)
  Inform the device that it can continue past Setup Assistant and finish login.
- [Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.
### Device state
- [Erase Device](erase-device-command.md)
  Remotely and immediately erase a device.
- [Device Lock](device-lock-command.md)
  Remotely and immediately lock a device.
- [Restart Device](restart-device-command.md)
  Remotely and immediately restart a device.
- [Shut Down Device](shut-down-device-command.md)
  Remotely and immediately shut down a device.
### Managed apps
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
- [Validate Applications](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.
### Managed media
- [Install Media](install-media-command.md)
  Install a book on a device.
- [Managed Media List](managed-media-list-command.md)
  Get a list of the managed books on a device.
- [Remove Media](remove-media-command.md)
  Remove a previously installed book from a device.
### Accounts
- [Account Configuration](account-configuration-command.md)
  Create and configure a local administrator account on a device.
- [Invite To Program](invite-to-program-command.md)
  Invite a user to join the Volume Purchase Program (VPP).
### Passwords
- [Clear Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear Restrictions Password](clear-restrictions-password-command.md)
  Clear the Screen Time password and the restrictions on a device.
- [Unlock User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set Auto Admin Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.
### Lost device
- [Enable Lost Mode](enable-lost-mode-command.md)
  Enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.
- [Device Location](device-location-command.md)
  Request the location of a device when in Lost Mode.
- [Play Lost Mode Sound](play-lost-mode-sound-command.md)
  Play the Lost Mode sound on a device that’s in Lost Mode.
- [Disable Lost Mode](disable-lost-mode-command.md)
  Take the device out of Lost Mode.
### Recovery Lock
- [Set Recovery Lock](set-recovery-lock-command.md)
  Set or clear the Recovery Lock password.
- [Verify Recovery Lock](verify-recovery-lock-command.md)
  Verify the device’s Recovery Lock password.
### Content caching
- [Content Caching Information](content-caching-information-command.md)
  Get the status of the content caches on a device.
### AirPlay mirroring
- [Request Mirroring](request-mirroring-command.md)
  Prompt the user to share their screen using AirPlay Mirroring.
- [Stop Mirroring](stop-mirroring-command.md)
  Stop mirroring the display to another device.
### eSIM management
- [Refresh Cellular Plans](refresh-cellular-plans-command.md)
  Query a carrier URL for active eSIM cellular-plan profiles on a device.
### Managed settings
- [Disable Remote Desktop](disable-remote-desktop-command.md)
  Disable Remote Desktop on a device.
- [Enable Remote Desktop](enable-remote-desktop-command.md)
  Enable Remote Desktop on a device.
- [Settings](settings-command.md)
  Configure settings on a device.
### Lights-out management
- [LOM Device Request](lom-device-request-command.md)
  Send requests to a device using lights-out management (LOM).
- [LOM Setup Request](lom-setup-request-command.md)
  Get information from a device to set up lights-out management (LOM).
### Security
- [Security Info](security-info-command.md)
  Get security-related information about a device.
- [Certificate List](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Activation Lock Bypass Code](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Clear Activation Lock Bypass Code](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.
- [Rotate FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.
### Extensions
- [Active NSExtensions](active-nsextensions-command.md)
  Get a list of active extensions for a user on a device.
- [NSExtension Mappings](nsextension-mappings-command.md)
  Get a list of the installed extensions for a user on a device.
### Enhanced logging
- [Trigger Enhanced Log Collection](trigger-enhanced-log-collection-command.md)
  Trigger enhanced log collection on the device.
- [Cancel Enhanced Log Collection](cancel-enhanced-log-collection-command.md)
  Cancel enhanced log collection on the device.
### User management
- [User List](user-list-command.md)
  Get a list of users with active accounts on a device.
- [Log Out User](log-out-user-command.md)
  Force the current user to log out of a device.
- [Delete User](delete-user-command.md)
  Delete a user’s account from a device.

## See Also

- [Check-in](check-in.md)
  Authenticate devices and maintain push tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/commands-and-queries)*