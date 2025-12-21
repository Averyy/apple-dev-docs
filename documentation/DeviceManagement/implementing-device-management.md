# Implementing Device Management

**Framework**: Device Management

Set up an MDM server and send commands to managed devices.

## Topics

### Essentials
- [Managing MDM Connections](managing-mdm-connections.md)
  Establish or remove a connection between a device and an MDM server.
- [Simplifying MDM Server Administration for iOS Devices](simplifying-mdm-server-administration-for-ios-devices.md)
  Create a service configuration entry point to your MDM server to access to frequently used information.
### Certificates and Profiles
- [Managing Certificates for MDM Servers and Devices](managing-certificates-for-mdm-servers-and-devices.md)
  Ensure secure MDM connectivity with valid certificates.
- [Deploying MDM Enrollment Profiles](deploying-mdm-enrollment-profiles.md)
  Choose the technique to deploy MDM enrollment profiles for your organization.
- [Installing Profiles on Devices](installing-profiles-on-devices.md)
  Optimize deployment of profiles and provisioning profiles.
- [Setting Up Push Notifications for Your MDM Customers](setting-up-push-notifications-for-your-mdm-customers.md)
  Create and sign a certificate signing request (CSR) to enable push notifications.
### Identity Management
- [Validating a Managed Device Attestation](validating-a-managed-device-attestation-attestation.md)
  Verify an attestation that a managed device returns by performing the required steps.
### Devices and Users
- [Managing MDM Devices and Users in macOS](managing-mdm-devices-and-users-in-macos.md)
  Manage devices and users as separate entities in macOS.
- [Enabling Network and Mobile User Logins](enabling-network-and-mobile-user-logins.md)
  Manage network users on macOS devices bound to an Open Directory server, and mobile users on shared iPads.
- [Managing Passcodes](managing-passcodes.md)
  Ensure data security by managing device passcodes and compliance with policies.
- [Dealing with Inactive MDM Devices and Invalid Push Tokens](dealing-with-inactive-mdm-devices-and-invalid-push-tokens.md)
  Handle when devices become unmanageable due to inactivity or invalid push tokens.
- [Returning a managed device to service](returning-a-managed-device-to-service.md)
  Use a device management service to return managed devices to service quickly after use.
### Commands
- [Sending MDM Commands to a Device](sending-mdm-commands-to-a-device.md)
  Execute commands on a device and receive responses that contain the results of each operation.
- [Handling NotNow Status Responses](handling-notnow-status-responses.md)
  Handle when a device won’t execute a command and instead returns a NotNow status.

## See Also

- [Commands and Queries](commands-and-queries.md)
  Manage the configuration and behavior of your devices.
- [Check-in](check-in.md)
  Authenticate devices and maintain push tokens with these commands.
- [Account-driven enrollment](account-driven-enrollment.md)
  Authenticate devices using a user identity-focused workflow.
- [Migrating managed devices](migrating-managed-devices.md)
  Migrate managed devices from one device management service to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/implementing-device-management)*