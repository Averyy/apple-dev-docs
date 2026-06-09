# Dealing with inactive managed devices and invalid push tokens

**Framework**: Device Management

Handle when devices become unmanageable due to inactivity or invalid push tokens.

#### Overview

When a device becomes inactive, your service can take action, such as limiting the deviceʼs access to your organizationʼs resources until the device resumes responding to push notifications.

#### Handle When a Device Becomes Inactive

To receive a notification when a device becomes inactive, set the `CheckOutWhenRemoved` key to `true` in the MDM payload. This causes the device to contact your device management service when it becomes unmanaged.

The following actions cause a device to become inactive:

- Powering off the device.
- Disconnecting from the network.
- Erasing the device.
- Removing the MDM profile.

> **Note**:  Your security report for each managed device specifies whether the MDM profile is nonremovable. The [`ProfileListResponse.ProfileListItem`](profilelistresponse/profilelistitem.md) contains this information.

Because a managed device makes only a single attempt to deliver this message, employ a timeout to detect devices that fail to check out due to network conditions. Your service then sends a push notification periodically to ensure that managed devices are still listening to it.

If the device fails to respond to push notifications after a specified time, you can consider the device inactive. The time to wait before considering that a device is inactive can vary according to your IT policy. A good time period to use ranges from several days to one week.

You don’t need to send push notifications on a daily basis to make sure a device is responding. Appleʼs push notification servers cache your last push notification and deliver it to the device when it reconnects to the network.

## See Also

- [Managing connections](managing-connections.md)
  Establish or remove a connection between a device and your device management service.
- [Managing certificates for device management services and devices](managing-certificates-for-device-management-services-and-devices.md)
  Ensure secure connectivity with your device management service using valid certificates.
- [Providing information about your device management service](providing-information-about-your-device-management-service.md)
  Create a service configuration entry point to your device management service to access frequently used information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dealing-with-inactive-managed-devices-and-invalid-push-tokens)*