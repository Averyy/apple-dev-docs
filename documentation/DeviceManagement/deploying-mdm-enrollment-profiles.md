# Deploying MDM Enrollment Profiles

**Framework**: Device Management

Choose the technique to deploy MDM enrollment profiles for your organization.

#### Overview

There are several ways to deploy an MDM enrollment profile. Choose the best approach according to the size of your organization and its IT policies, and whether a device management system already exists. Third-party vendors can also install the MDM configuration profile in a variety of ways that integrate with their management systems.

##### Install the Mdm Enrollment Profile

Only include payloads in your enrollment profile that are necessary to complete enrollment. At a minimum, include the following:

- Any root and intermediate certificates necessary to establish SSL trust
- A client identity certificate for use by the MDM payload; either a Simple Certificate Enrollment Protocol (SCEP) payload, recommended, or a PKCS #12 container
- The MDM payload

After the device installs the enrollment profile, the server can push additional managed profiles to it.

In macOS, installing an MDM profile on a device in a single-user environment creates the following conditions:

- The device becomes a managed device through the device profile.
- The user who installs the profile becomes a managed user through the user profile.
- Other local users who log in to the device don’t become managed users, other than by device profiles.

Devices become managed devices when network users bound to Open Directory servers log in to them and the MDM server recognizes those devices.

See [`Install Profile`](install-profile-command.md) for additional information.

##### Assign Media to Users Before Enrollment

Register Volume Purchase Program (VPP) users and assign apps and books to those users before sending invitations to them. This speeds up each assignment because the system doesn’t need to put the items in the user’s purchases at the time of assignment. Also, because acceptance of an invitation is likely to occur before MDM issues an `InstallApplication` command, propagation of all licenses to the user’s iTunes Store purchase history on the user’s clients has ample time to complete. This step is necessary for the `InstallApplication` command to succeed.

Invite a user to each VPP organization only once. By checking the user’s `itsIdHash`, an MDM server can detect when a single Apple Account accepts multiple invitations. Attempts to assign licenses for the same item to multiple VPP users with the same `itsidHash` result in an Already Assigned error (code 9616).

##### Use Over the Air Enrollment

Over-the-air (OTA) enrollment allows your server to validate a userʼs login and the deviceʼs built-in certificate, and query for more information about the device, before delivering an enrollment profile. That profile also becomes eligible for updates, even after expiration of the profile’s signing certificate. This includes the MDM enrollment profile itself.

To replace an installed profile, install a new profile with the same top-level `PayloadIdentifier` as the installed profile. This restarts the check-in process. Include an SCEP payload to create a new client identity. The system restores the old configuration if the update fails.

##### Use the Device Enrollment Program

The Device Enrollment Program (DEP) enables your MDM server to automatically deploy enrollment profiles over the air to devices that you own. If you use this method at the time of purchase, devices that you enroll in this program prompt the user to begin the MDM enrollment process upon activation. This avoids the need to preconfigure each device.

Devices that you enroll using DEP become supervised devices during activation. This allows an MDM server to send additional configuration commands and to apply additional restrictions, such as installing an always-on VPN configuration. Users can’t remove MDM profiles that you deliver using DEP.

MDM vendors can take advantage of web services that DEP provides to integrate its features with their services. For more information, see [`Simplifying MDM Server Administration for iOS Devices`](simplifying-mdm-server-administration-for-ios-devices.md).

## See Also

- [Managing Certificates for MDM Servers and Devices](managing-certificates-for-mdm-servers-and-devices.md)
  Ensure secure MDM connectivity with valid certificates.
- [Installing Profiles on Devices](installing-profiles-on-devices.md)
  Optimize deployment of profiles and provisioning profiles.
- [Setting Up Push Notifications for Your MDM Customers](setting-up-push-notifications-for-your-mdm-customers.md)
  Create and sign a certificate signing request (CSR) to enable push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deploying-mdm-enrollment-profiles)*