# Commands and Queries

**Framework**: Device Management

Manage the configuration and behavior of your devices.

#### Overview

The Mobile Device Management (MDM) protocol provides a way to tell a device to remotely execute certain management commands or queries. First, a device registers with the MDM server. Then, the server sends push notifications to the device when there are commands to process on the device.

When the device receives the notification, it polls the server for the command, processes the command, and reports the command results to the server. The device then checks for other commands to process.

> ❗ **Important**:  Mobile Device Management is for enterprise use only. To use it in your app, the Account Holder of your app’s development team must request the Mobile Device Management capability. See [`Request a Mobile Device Management Capability`](https://developer.apple.comhttps://developer.apple.com/contact/request/mdm-capability).

 Mobile Device Management is for enterprise use only. To use it in your app, the Account Holder of your app’s development team must request the Mobile Device Management capability. See [`Request a Mobile Device Management Capability`](https://developer.apple.comhttps://developer.apple.com/contact/request/mdm-capability).

## Topics

### Profile Management
- [Install a Profile](install-profile-command.md)
  Install a configuration profile on a device.
- [List the Installed Profiles](profile-list-command.md)
  Get a list of installed profiles on a device.
- [Remove a Profile](remove-profile-command.md)
  Remove a previously installed profile from the device.
- [Install a Provisioning Profile](install-provisioning-profile-command.md)
  Install a provisioning profile on a device.
- [List the Installed Provisioning Profiles](provisioning-profile-list-command.md)
  Get a list of installed provisioning profiles on a device.
- [Remove a Provisioning Profile](remove-provisioning-profile-command.md)
  Remove a previously installed provisioning profile from a device.
### Device Details
- [List the Installed Apps](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Get Device Information](device-information-command.md)
  Get detailed information about a device.
- [Release Device from Await Configuration](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured Command](user-configured-command.md)
  Informs the device that it can continue past Setup Assistant and finish login.
- [List the Installed Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.
### Device State
- [Erase a Device](erase-device-command.md)
  Remotely and immediately erase a device.
- [Lock a Device](device-lock-command.md)
  Remotely and immediately lock a device.
- [Restart a Device](restart-device-command.md)
  Remotely and immediately restart a device.
- [Shut Down a Device](shut-down-device-command.md)
  Remotely and immediately shut down a device.
### Managed Apps
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
- [Get App Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.
### Managed Media
- [Install Media](install-media-command.md)
  Install a book on a device.
- [List the Managed Media](managed-media-list-command.md)
  Get a list of the managed books on a device.
- [Remove Media](remove-media-command.md)
  Remove a previously installed book from a device.
### Accounts
- [Account Configuration](account-configuration-command.md)
  Create and configure a local administrator account on a device.
- [Invite to the Program](invite-to-program-command.md)
  Invite a user to join the Volume Purchase Program (VPP).
### Passwords
- [Clear the Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear the Restrictions Password](clear-restrictions-password-command.md)
  Clear the restrictions password and the restrictions on a device.
- [Unlock a User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set the Local Administrator Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set the Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify the Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.
### Updates
- [Schedule an OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device.
- [List the Available OS Updates](available-os-updates-command.md)
  Get a list of available operating-system updates for a device.
- [Schedule an OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.
- [Get the OS Update Status](os-update-status-command.md)
  Get the status of operating-system updates on a device.
### Lost Device
- [Enable Lost Mode](enable-lost-mode-command.md)
  Enable Lost Mode on a device, which provides a message and phone number on the Lock screen.
- [Get the Location of a Device](device-location-command.md)
  Request the location of a device when in Lost Mode.
- [Play the Lost Mode Sound](play-lost-mode-sound-command.md)
  Play the Lost Mode sound on a device that’s in Lost Mode.
- [Disable Lost Mode](disable-lost-mode-command.md)
  Take the device out of Lost Mode.
### Recovery Lock
- [Set Recovery Lock Command](set-recovery-lock-command.md)
  Set or clear the Recovery Lock password.
- [Verify Recovery Lock Command](verify-recovery-lock-command.md)
  Verify the device’s Recovery Lock password.
### Content Caching
- [Content Caching Information Command](content-caching-information-command.md)
  Get the status of the content caches on a device.
### AirPlay Mirroring
- [Start AirPlay Mirroring](request-mirroring-command.md)
  Prompt the user to share their screen using AirPlay Mirroring.
- [Stop AirPlay Mirroring](stop-mirroring-command.md)
  Stop mirroring the display on another device.
### eSim Management
- [Update the eSIM Cellular Plan](refresh-cellular-plans-command.md)
  Query a carrier URL for active eSIM cellular-plan profiles on a device.
### Managed Settings
- [Disable Remote Desktop](disable-remote-desktop-command.md)
  Disable Remote Desktop on a device.
- [Enable Remote Desktop](enable-remote-desktop-command.md)
  Enable Remote Desktop on a device.
- [Configure Settings](settings-command.md)
  Configure settings on a device.
### Lights-Out Management
- [LOM Device Request Command](lom-device-request-command.md)
  Send requests to a device using lights-out management (LOM).
- [LOM Setup Request Command](lom-setup-request-command.md)
  Get information from a device to set up lights-out management (LOM).
### Security
- [Security Information](security-info-command.md)
  Get security-related information about a device.
- [List the Certificates](certificate-list-command.md)
  Get a list of installed certificates on a device.
- [Get the Bypass Code for Activation Lock](activation-lock-bypass-code-command.md)
  Get the code to bypass Activation Lock on a device.
- [Clear the Bypass Code for Activation Lock](clear-activation-lock-bypass-code-command.md)
  Clear the Activation Lock bypass code on a device.
- [Rotate the FileVault Key](rotate-filevault-key-command.md)
  Change the FileVault primary password on a device.
### Extensions
- [List Active NSExtensions](active-nsextensions-command.md)
  Get a list of active extensions for a user on a device.
- [List the NSExtensions](nsextension-mappings-command.md)
  Get a list of the installed extensions for a user on a device.
### User Management
- [List the User Accounts](user-list-command.md)
  Get a list of users with active accounts on a device.
- [Log Out the User](log-out-user-command.md)
  Force the current user to log out of a device.
- [Delete a User](delete-user-command.md)
  Delete a user’s account from a device.
### Declarative Management
- [Enable Declarative Management](declarative-management-command.md)
  Enable your server to support declarative management or trigger a declarative management synchronization operation on the device.
### Deprecated
- [Request the Unlock Token](request-unlock-token-command.md)
  Request an unlock token from a device.

## See Also

- [Implementing Device Management](implementing-device-management.md)
  Set up an MDM server and send commands to managed devices.
- [Check-in](check-in.md)
  Authenticate devices and maintain push tokens with these commands.
- [User Enrollment](user-enrollment.md)
  Authenticate devices using an user identity focused workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/commands-and-queries)*