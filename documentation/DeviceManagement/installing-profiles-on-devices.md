# Installing Profiles on Devices

**Framework**: Device Management

Optimize deployment of profiles and provisioning profiles.

#### Overview

Follow these provisioning profiles best practices to enable new capabilities or allow users to run enterprise apps.

##### Pair Restrictions with Capabilities in Managed Profiles

Configure each managed profile, so it’s clear to the user what new capability they’ll receive on the device when they comply with an associated retstrictions or requirement.

For example, your IT policy may require a device to have a 6-character passcode in order to access your corporate VPN service. You can configure a managed profile to enable the VPN capability for a user once they comply with the passcode restriction. There are two ways to accomplish this:

- Deliver a single managed profile with both a passcode restriction payload and a VPN payload. This approach allows a grace period before a user must set a compliant passcode.
- Deliver a profile with a passcode restriction, poll the device until it indicates compliance, and then deliver the VPN payload.

##### Install Provisioning Profiles

Third-party enterprise apps require installation of a provisioning profile to enable running them. Use MDM to efficiently deliver up-to-date versions of provisioning profiles instead of manually distributing them through your corporate web portal or bundled with the app, and replacing them when they expire. Using MDM also prevents users from having to perform these tasks on their own. For more information on installation, see [`Install a Provisioning Profile`](install-provisioning-profile-command.md).

## See Also

- [Managing Certificates for MDM Servers and Devices](managing-certificates-for-mdm-servers-and-devices.md)
  Ensure secure MDM connectivity with valid certificates.
- [Deploying MDM Enrollment Profiles](deploying-mdm-enrollment-profiles.md)
  Choose the technique to deploy MDM enrollment profiles for your organization.
- [Setting Up Push Notifications for Your MDM Customers](setting-up-push-notifications-for-your-mdm-customers.md)
  Create and sign a certificate signing request (CSR) to enable push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installing-profiles-on-devices)*