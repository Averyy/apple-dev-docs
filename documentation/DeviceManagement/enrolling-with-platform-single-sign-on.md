# Enrolling with Platform Single Sign-on

**Framework**: Device Management

Authenticate users during device enrollment using Platform Single Sign-on.

#### Overview

Platform Single Sign-on (Platform SSO) allows a device management service to configure SSO extensions that integrate with the macOS login window, enabling seamless access to apps and websites immediately after logging in without reentering credentials. Local account passwords can optionally stay in sync with the identity provider (IdP), and users can still unlock their Mac using Touch ID or Apple Watch.

A device management service can also use Platform SSO to improve the enrollment flow in two ways during macOS device setup after the administrator registers the device with the Automated Device Enrollment program.

In the first case, a device management service uses Platform SSO to allow a user to sign in before enrollment occurs. That allows the service to validate the user credentials before enrollment, and then allows the device to automatically set up a local user account that it configures to use the SSO credentials. This provides users with a seamless enrollment and sign-in process that results in a Platform SSO-enabled managed device. For more information, see [`Implementing Platform SSO during device enrollment`](implementing-platform-sso-during-device-enrollment.md).

In the second case, a device management service uses Platform SSO to perform an unattended enrollment. When a user logs in to the device, the device uses the configured Platform SSO to sign them in. For more information, see [`Implementing Platform SSO for unattended device enrollment`](implementing-platform-sso-for-unattended-device-enrollment.md).

Only macOS 26 devices that are registered with the Automated Device Enrollment program support these two Platform SSO flows.

## Topics

### Detailed flow instructions
- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)
  Streamline device enrollment by using Platform SSO.
- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)
  Configure and enroll unattended devices by using Platform SSO.

## See Also

- [Onboarding users with account sign-in](onboarding-users-with-account-sign-in.md)
  Implement user-initiated, identity-focused authentication flows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enrolling-with-platform-single-sign-on)*