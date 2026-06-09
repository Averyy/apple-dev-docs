# Managing connections

**Framework**: Device Management

Establish or remove a connection between a device and your device management service.

#### Overview

Device management begins when you set up a service and distribute your device management (MDM) enrollment profile to devices to initiate connecting them. Then, you can send commands to managed devices to get detailed information about the device, install apps and books, and more.

After a device installs a device management (MDM) enrollment profile and connects to the service, it can receive commands from the service. When you remove the device management (MDM) enrollment profile from a device, that terminates the device management relationship with the device management service.

#### Create a New Device Management Connection

A connection between your device management service and a device enables you to send commands to the device that it executes and reports back the results. A device management service and a device complete the following steps to establish a connection:

1. A user or adminstrator installs a device management (MDM) enrollment profile on the device. For more information, see [`Deploying device management enrollment profiles`](deploying-device-management-enrollment-profiles.md).
2. The device checks in and authenticates with the device management service. For more information, see [`Managing certificates for device management services and devices`](managing-certificates-for-device-management-services-and-devices.md).
3. The device management service accepts the device, or for Automated Device Enrollment, it can send an error instead, such as [`ErrorCodeSoftwareUpdateRequired`](errorcodesoftwareupdaterequired.md) or [`ErrorUnrecognizedDevice`](errorunrecognizeddevice.md).
4. The device provides its push notification token to the service.

The device management (MDM) enrollment profile contains a payload that provides information necessary for a device to connect to a device management service and authenticate with it. For a description of the information to include in the payload, see [`MDM`](mdm.md).

The device presents its identity certificate to the device management service for authentication, along with its `UDID` and push-notification token. The device management service uses this token to initate a transaction with the device. This token may change, and when it does, the device automatically checks in with the device management service to provide the new token.

> **Note**:  Although device management uses `UDID`s, they’re deprecated in iOS. A `UDID` may contain special characters, such as dashes, and its length isn’t guaranteed.

#### Handle Device Restores

A user can restore their connected device from a backup. If the backup contains a device management (MDM) enrollment profile, the system restores management of the device, and the device schedules delivery of a [`TokenUpdateRequest`](tokenupdaterequest.md) check-in message to the device management service. However, if the user restores the backup to a different device, the system won’t restore device management.

Your device management service can either accept the device by replying with a `200` HTTP status code, or reject the device with a `401` status code. If your service replies with a `401` status code, the device removes the device management (MDM) enrollment profile.

> 💡 **Tip**:  Configure your service to respond with a `401` HTTP status code to any device that it isn’t actively managing.

#### Terminate Management of a Device

Terminate a management relationship with a device by performing one of these actions:

- Remove the device management enrollment profile that contains the MDM payload. A device management service can always remove this profile, even if it doesn’t have the access rights to add or remove configuration profiles.
- Respond to any request from the device with a `401` HTTP status. The device automatically removes the device management enrollment profile that contains the MDM payload.

## Topics

### Enrollment errors
- [object ErrorCodePairingTokenMissing](errorcodepairingtokenmissing.md)
  An error response that indicates a missing pairing token.
- [object ErrorCodePlatformSSORequired](errorcodeplatformssorequired.md)
  An error response that indicates Platform SSO is required.
- [object ErrorCodeSoftwareUpdateRequired](errorcodesoftwareupdaterequired.md)
  An error response that indicates the system requires a software update.
- [object ErrorUnrecognizedDevice](errorunrecognizeddevice.md)
  An error response that indicates a device needs to unenroll.
- [object ErrorWellKnownFailed](errorwellknownfailed.md)
  An error response that indicates a well-known service discovery request failed.

## See Also

- [Managing certificates for device management services and devices](managing-certificates-for-device-management-services-and-devices.md)
  Ensure secure connectivity with your device management service using valid certificates.
- [Providing information about your device management service](providing-information-about-your-device-management-service.md)
  Create a service configuration entry point to your device management service to access frequently used information.
- [Dealing with inactive managed devices and invalid push tokens](dealing-with-inactive-managed-devices-and-invalid-push-tokens.md)
  Handle when devices become unmanageable due to inactivity or invalid push tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-connections)*