# Deploying device management enrollment profiles

**Framework**: Device Management

Choose the technique to deploy device management (MDM) enrollment profiles for your organization.

#### Overview

There are several ways to deploy a device management (MDM) enrollment profile. Choose the best approach according to the size of your organization and its IT policies, and whether a device management service already exists. Third-party vendors can also install the MDM configuration profile in a variety of ways that integrate with their device management service.

#### Install the Device Management Mdm Enrollment Profile

Only include payloads in your device management (MDM) enrollment profile that are necessary to complete the enrollment. At a minimum, include the following:

- Any root and intermediate certificates necessary to establish SSL trust.
- A client identity certificate for use by the MDM payload; either an Automated Certificate Management Environment (ACME) payload which is recommended, a Simple Certificate Enrollment Protocol (SCEP) payload, or a PKCS #12 container.
- The MDM payload.

After the device installs the device management (MDM) enrollment profile, the device management service can push additional managed profiles to it.

In macOS, installing an MDM profile on a device in a single-user environment creates the following conditions:

- The device becomes a managed device through the device profile.
- The user who installs the profile becomes a managed user through the user profile.
- Other local users who log in to the device don’t become managed users, other than by device profiles.

Devices become managed devices when network users bound to Open Directory servers log in to them and the device management service recognizes those devices.

For additional information, see [`Install Profile`](install-profile-command.md).

#### Assign Media to Users Before Enrollment

Register Volume Purchase Program (VPP) users and assign apps and books to those users before sending invitations to them. This speeds up each assignment because the system doesn’t need to put the items in the user’s purchases at the time of assignment. Also, because acceptance of an invitation is likely to occur before the device management service issues an `InstallApplication` command, propagation of all licenses to the user’s App Store purchase history on the user’s clients has ample time to complete. This step is necessary for the `InstallApplication` command to succeed.

Invite a user to each VPP organization only once. By checking the user’s `itsIdHash`, a device management service can detect when a single Apple Account accepts multiple invitations. Attempts to assign licenses for the same item to multiple VPP users with the same `itsidHash` result in an *Already Assigned* error (code 9616).

#### Use Over the Air Enrollment

Over-the-air (OTA) enrollment allows your device management service to validate a userʼs login and the deviceʼs built-in certificate, and query for more information about the device, before delivering a device management (MDM) enrollment profile. That profile also becomes eligible for updates, even after expiration of the profile’s signing certificate. This includes the device management (MDM) enrollment profile itself.

To replace an installed profile, install a new profile with the same top-level `PayloadIdentifier` as the installed profile. This restarts the check-in process. Include an ACME or SCEP payload to create a new client identity. The system restores the old configuration if the update fails.

#### Use the Automated Device Enrollment Program

The Automated Device Enrollment program enables your device management service to automatically deploy device management (MDM) enrollment profiles over the air to devices that you own. If you use this method at the time of purchase, devices that you enroll in this program prompt the user to begin the enrollment process upon activation. This avoids the need to preconfigure each device.

Devices that you enroll using ADE become supervised devices during activation. This allows a device management service to send additional configuration commands and to apply additional restrictions, such as installing an always-on VPN configuration. Users can be prevented from removing MDM profiles that you deliver using ADE.

Device management vendors can take advantage of web services that ADE provides to integrate its features with their services. For more information, see [`Providing information about your device management service`](providing-information-about-your-device-management-service.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deploying-device-management-enrollment-profiles)*