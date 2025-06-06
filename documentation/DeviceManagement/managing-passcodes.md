# Managing Passcodes

**Framework**: Device Management

Ensure data security by managing device passcodes and compliance with policies.

#### Overview

When members of your organization have proprietary information on their devices, it’s important to ensure the devices are secure. Require your users to have strong passcodes on their managed devices to secure your data. MDM makes it possible to manage and enforce these requirements.

##### Manage Changes to Passcode Policies

You can use an MDM server to push a profile that contains a passcode policy or a change to an existing policy without user interaction. For instance, you can require a user to change their passcode to comply with a more stringent policy. When you do this, a 60-minute countdown begins. During this grace period, the user receives a prompt to change their passcode when they return to the Home screen, however, they can dismiss the prompt and continue working. After the 60-minute period elapses, the user must change the passcode to launch any application on the device, including built-in applications.

Use the [`SecurityInfoCommand`](securityinfocommand.md) to determine whether a user complies with the passcode restrictions.

> ❗ **Important**:  Wait until the user complies with the passcode policy before sending any proprietary data or configurations to the device.

 Wait until the user complies with the passcode policy before sending any proprietary data or configurations to the device.

##### Manage the Clearpasscode Command

Passcodes add a layer of security to your organization’s devices. Occasionally, it may be necessary to clear a device’s passcode by sending it a [`ClearPasscodeCommand`](clearpasscodecommand.md), such as when:

- A user forgets their passcode.
- You need to perform a device refresh across the team.
- Team members leave your organization.

Clearing the passcode on a managed device compromises its security because it enables access to the device without a passcode, and it disables the Data Protection feature.

If your MDM payload specifies the Device Lock feature, the device includes an `UnlockToken` data value in the `TokenUpdate` message that it sends your server after installing the profile. This data contains a cryptographic package that can enable unlocking the device. Treat this data as the equivalent of a primary passcode for the device. Ensure that your IT policy specifies how to securely store this data, who has access to it, and the requirements to execute the [`ClearPasscodeCommand`](clearpasscodecommand.md). To create a `ClearPasscodeCommand` request, obtain the `UnlockToken` for that device by sending it a [`TokenUpdateRequest`](tokenupdaterequest.md).

> ⚠️ **Warning**:  Never send the `ClearPasscodeCommand` to a lost device, and always ensure physical possession of the device by a member of your organization before sending this command.

 Never send the `ClearPasscodeCommand` to a lost device, and always ensure physical possession of the device by a member of your organization before sending this command.

## See Also

- [Managing MDM Devices and Users in macOS](managing-mdm-devices-and-users-in-macos.md)
  Manage devices and users as separate entities in macOS.
- [Enabling Network and Mobile User Logins](enabling-network-and-mobile-user-logins.md)
  Manage network users on macOS devices bound to an Open Directory server, and mobile users on shared iPads.
- [Dealing with Inactive MDM Devices and Invalid Push Tokens](dealing-with-inactive-mdm-devices-and-invalid-push-tokens.md)
  Handle when devices become unmanageable due to inactivity or invalid push tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-passcodes)*