# Implementing Platform SSO for unattended device enrollment

**Framework**: Device Management

Configure and enroll unattended devices by using Platform SSO.

#### Overview

A device management service can silently configure Platform SSO on a macOS device after the administrator registers the device with the Automated Device Enrollment program. After enrollment, user logins leverage Platform SSO, enabling a seamless, zero-touch setup, with devices ready for authentication out of the box.

#### Set Up a Device for Unattended Enrollment

For unattended device setup, the device management service needs to set the `auto_advance_setup` key to `true` in the Automated Device Enrollment [`Profile`](profile.md) it assigns to the device. This ensures that the device proceeds through `Setup Assistant` automatically, without the need for any user interaction.

The device management service also needs to set the `await_device_configured` key to `true` in the Automated Device Enrollment [`Profile`](profile.md). This ensures that the device enters the await configuration state, forcing it to wait for the service to indicate that it can proceed. This gives the service time to configure Platform SSO on the device so that it’s ready when a user logs in.

#### Configure Platform Sso After Enrollment

When the device enrolls with the device management service, it enters the await configuration state again when the enrollment is complete. In that state, the service can send commands to the device without the device advancing through `Setup Assistant`. After the service sends all the commands it needs to configure the device, it sends the [`Device Configured`](device-configured-command.md) command to have the device exit the await configuration state, allowing it to proceed through `Setup Assistant`.

To configure Platform SSO on the device, the device management service needs to install:

- An app that includes the SSO extension for Platform SSO
- A profile that contains an [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile payload with a configuration to use Platform SSO

The device management service needs to wait for the app to install before it sends the [`Device Configured`](device-configured-command.md) command to have the device exit the await configuration state. There are two options for waiting, depending on whether the service installs the app using declarative management or MDM commands:

> **Note**:  Declarative management is the preferred solution. It requires less network traffic to monitor the app status because the device reports the status autonomously. With MDM commands, the device management service needs to continuously poll the device to check the app status.

To ensure that the system skips the local user account creation pane in `Setup Assistant`, the device management service needs to do the following:

- Send an [`Account Configuration`](account-configuration-command.md) command to the device during the await configuration state.
- Set the `SkipPrimarySetupAccountCreation` key to `true` in the command.
- Provide at least one [`AccountConfigurationCommand.Command.AutoSetupAdminAccountItem`](accountconfigurationcommand/command-data.dictionary/autosetupadminaccountitem.md) object in the `AutoSetupAdminAccounts` key in the command.

After the device management service finishes configuring the device with the Platform SSO app, extensible SSO profile, and any other management state it needs, it sends the [`Device Configured`](device-configured-command.md) command to the device. When the device receives the [`Device Configured`](device-configured-command.md) command, it registers for Platform SSO using the app’s SSO extension and the SSO configuration from the profile. This doesn’t require any user interaction.

The device then proceeds through `Setup Assistant`. However, the device doesn’t create a local user account as it usually does during the `Setup Assistant` process. Instead, it completes `Setup Assistant` and is ready to use. The system automatically creates the local user account when the first user logs in, with the login using Platform SSO to sign in.

#### Manage the Device

After `Setup Assistant` completes, the device is managed and has a configuration to use Platform SSO. The SSO app and configuration profile that the device installs during the await configuration state persist on the device and remain managed.

## See Also

- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)
  Streamline device enrollment by using Platform SSO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/implementing-platform-sso-for-unattended-device-enrollment)*