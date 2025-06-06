# Handling NotNow Status Responses

**Framework**: Device Management

Handle when a device won’t execute a command and instead returns a NotNow status.

#### Overview

Specific conditions prevent a device from executing a command. For example, a device won’t execute some commands before the first unlock after a device boot. When this occurs, a device can respond to the server with a `NotNow` status to indicate that later retries may succeed.

When the server receives a `NotNow` response from a device, it can either stop sending commands to the device or send another command to it on the same connection.

##### Understand Server and Device Polling

When a server stops sending commands to a device, the device automatically polls the server when conditions change. However, the device doesn’t cache the failed command. If you configure the server to instruct the device to retry the command, it must send the command again when the device polls the server. The server doesn’t need to send another push notification in response to this status, but it can send another one to instruct the device to poll the server immediately.

If the server sends another command to the client on the same connection, and this new command returns anything other than a `NotNow` response, the device won’t automatically poll the server as it would if the first command executed successfully. The server must send a push notification at a later time to instruct the device to reconnect. The device only polls the server in response to a `NotNow` status if that’s the last status sent by the device to the server.

##### Handle Notnow Responses

In macOS, a device may not execute commands, but instead respond with a `NotNow` status during these conditions:

- The device is running on battery power in Power Nap and the server sends any command other than [`DeleteUserCommand`](deleteusercommand.md), [`DeviceLockCommand`](devicelockcommand.md), [`EraseDeviceCommand`](erasedevicecommand.md), [`RestartDeviceCommand`](restartdevicecommand.md), [`ShutDownDeviceCommand`](shutdowndevicecommand.md), [`UserListCommand`](userlistcommand.md), [`ActivationLockBypassCodeCommand`](activationlockbypasscodecommand.md), [`ClearActivationLockBypassCodeCommand`](clearactivationlockbypasscodecommand.md), or [`UnlockUserAccountCommand`](unlockuseraccountcommand.md).
- The server sends an `InstallProfile` or `RemoveProfile` command on the user connection and the user’s keychain is locked.
- The device is blocking the user’s login while it contacts the server and the server sends a request that can take a long time to process; for example, `InstalledApplicationList`.

Avoid receiving a `NotNow` status response on iOS devices by executing any of the following commands:

- [`DeviceInformationCommand`](deviceinformationcommand.md)
- [`ProfileListCommand`](profilelistcommand.md)
- [`DeviceLockCommand`](devicelockcommand.md)
- [`EraseDeviceCommand`](erasedevicecommand.md)
- [`ClearPasscodeCommand`](clearpasscodecommand.md)
- [`ProvisioningProfileListCommand`](provisioningprofilelistcommand.md)
- [`InstalledApplicationListCommand`](installedapplicationlistcommand.md)
- [`RestrictionsCommand`](restrictionscommand.md)

## See Also

- [Sending MDM Commands to a Device](sending-mdm-commands-to-a-device.md)
  Execute commands on a device and receive responses that contain the results of each operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/handling-notnow-status-responses)*