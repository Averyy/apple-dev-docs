# Managing MDM Connections

**Framework**: Devicemanagement

Establish or remove a connection between a device and an MDM server.

#### Overview

Mobile device management begins when you set up a server and distribute your MDM enrollment profile to devices to initiate connecting them. Then, you can send commands to managed devices to get detailed information about the device, install apps and books, and more.

Once the device installs an MDM enrollment profile and connects to the server, it can receive commands from the server. When you remove the MDM enrollment profile from a device, that terminates the device mangagement relationship with the server.

##### Create a New Device Management Connection

A connection between your MDM server and a device enables you to send commands to the device that it executes and reports back the results. An MDM server and a device complete the following steps to establish a connection:

1. A user or adminstrator installs an MDM enrollment profile on the device. For more information, see [`Deploying MDM Enrollment Profiles`](deploying-mdm-enrollment-profiles.md).
2. The device checks in and authenticates with the MDM server. For more information, see [`Managing Certificates for MDM Servers and Devices`](managing-certificates-for-mdm-servers-and-devices.md).
3. The MDM server accepts the device, or for Automated Device Enrollment, it can send an error instead, such as [`ErrorCodeSoftwareUpdateRequired`](errorcodesoftwareupdaterequired.md).
4. The device provides its push notification token to the server.

The MDM enrollment profile contains a payload that provides information necessary for a device to connect to an MDM server and authenticate with it. See [`MDM`](mdm.md) for a description of the information to include in the payload.

The device presents its identity certificate to the MDM server for authentication, along with its `UDID` and push-notification token. The MDM server uses this token to initate a transaction with the device. This token may change, and when it does, the device automatically checks in with the MDM server to provide the new token.

> **Note**:  Although MDM uses `UDID`s, they’re deprecated in iOS. A `UDID` may contain special characters, such as dashes, and its length isn’t guaranteed.

##### Handle Device Restores

A user can restore their connected device from a backup. If the backup contains an MDM enrollment profile, the system restores management of the device, and the device schedules delivery of a [`TokenUpdateRequest`](tokenupdaterequest.md) check-in message to the server. However, if the user restores the backup to a different device, the system won’t restore MDM service.

Your server can either accept the device by replying with a `200` HTTP status code, or reject the device with a `401` status code. If your server replies with a `401` status code, the device removes the enrollment profile that contains the MDM payload.

> 💡 **Tip**:  Configure your server to respond with a `401` HTTP status code to any device that it isn’t actively managing.

##### Terminate Management of a Device

Terminate a management relationship with a device by performing one of these actions:

- Remove the enrollment profile that contains the MDM payload. An MDM server can always remove this profile, even if it doesn’t have the access rights to add or remove configuration profiles.
- Respond to any request from the device with a `401` HTTP status. The device automatically removes the enrollment profile that contains the MDM payload.

## Topics

### Enrollment Errors
- [object ErrorCodeSoftwareUpdateRequired](errorcodesoftwareupdaterequired.md)
  An error response that indicates the system requires a software update.

## See Also

- [Simplifying MDM Server Administration for iOS Devices](simplifying-mdm-server-administration-for-ios-devices.md)
  Create a service configuration entry point to your MDM server to access to frequently used information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement/managing-mdm-connections)*