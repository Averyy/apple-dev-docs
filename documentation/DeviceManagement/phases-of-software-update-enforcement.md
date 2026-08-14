# Phases of software update enforcement

**Framework**: Device Management

Enforcing software updates on Apple devices goes through specific phases.

#### Overview

Enforcing software updates using device management involves five main components:

- The device management service
- The device
- The user
- The Apple Software Lookup Service
- The Apple Software Update Catalog

#### Phase 1

The device management service regularly monitors the Apple Software Lookup Service for new releases. If it detects one, it uses the `SupportedDevices` key of the catalog and compares it to its list of managed devices to determine which devices the release is applicable to.

The device management service should also subscribe to the `softwareupdate.*` and `device.operating-system.*` status reports to automatically retrieve updates when any of those values change.

![The device management service regularly monitors the Apple Software Lookup Service for new releases](/images/com.apple.devicemanagement/phases-of-software-update-enforcement01@2x.png)

#### Phase 2

The device management service creates a [`SoftwareUpdateEnforcementSpecific`](softwareupdateenforcementspecific.md) declaration with the detected version and defines the `TargetLocalDateTime` and, optionally, the `DetailsURL` according to the organizational requirements. The device management service then sends a push notification to the device to start the synchronization of declarations. For more information, see [`Integrating declarative management`](integrating-declarative-management.md).

![The device management service creates the enforcement configuration and syncs it to the device](/images/com.apple.devicemanagement/phases-of-software-update-enforcement02@2x.png)

#### Phase 3

After the declaration becomes active on a device, the operating system reaches out to the Apple Software Update Catalog to retrieve the download URL and begins to download the update if it meets the requirements. The device then presents a notification to the user, and returns the following to the device management service:

1. A [`StatusSoftwareUpdateInstallState`](statussoftwareupdateinstallstate.md) value of `waiting`, which indicates the process to request the update has started.
2. A [`StatusSoftwareUpdateInstallState`](statussoftwareupdateinstallstate.md) value of `downloading`, which indicates the update is being downloaded by the device.

If a content caching service is available to the device, it attempts to download the software update from the content cache.

After the device successfully downloads the update, it prepares it for installation. After this process completes, the operating system sends a [`StatusSoftwareUpdateInstallState`](statussoftwareupdateinstallstate.md) value of `prepared` to the device management service.

![The device retrieves the download URL and begins the download and preparation of the software update](/images/com.apple.devicemanagement/phases-of-software-update-enforcement03@2x.png)

#### Phase 4

The device enters the notification period. Depending on when the installation is to occur, this notification may display different text and options.

![The device enters the notification period to regularly inform the user](/images/com.apple.devicemanagement/phases-of-software-update-enforcement04@2x.png)

#### Phase 5

If the user doesn’t install the update before the enforcement deadline, the device begins the installation and sends a [`StatusSoftwareUpdateInstallState`](statussoftwareupdateinstallstate.md) value of `installing` to the device management service. Before starting the installation, a Mac with Apple silicon contacts the device management service to retrieve the bootstrap token (if one is available).

If the update succeeds, the device restarts. If the update fails, a [`StatusSoftwareUpdateInstallState`](statussoftwareupdateinstallstate.md) value of `failed is sent. In either case, the device sends back a [`StatusSoftwareUpdateFailureReason`](statussoftwareupdatefailurereason.md) status report. If the update was successful, the count key has a value of 0.

![The device enforces installtion of the software update and sends status reports to the device management service](/images/com.apple.devicemanagement/phases-of-software-update-enforcement05@2x.png)

#### Phase 6

The device then sends the following information to the device management service. Depending on the update, some objects may not have return values.

- `StatusDeviceOperatingSystemVersion`: A status report of the device’s operating system version.
- `StatusDeviceOperatingSystemBuildVersion`: A status report of the device’s software build identifier.
- `StatusDeviceOperatingSystemSupplementalBuildVersion`: A status report of the device’s operating system version and Background Security Improvement build identifier.
- StatusDeviceOperatingSystemSupplementalExtraVersion`: A status report of the device’s operating system’s Background Security Improvement identifier.

![The device sends updated information to the device management service](/images/com.apple.devicemanagement/phases-of-software-update-enforcement06@2x.png)

#### Phase 7

The device management service unassigns the declaration from the device and sends a push notification to it to initiate the synchronization. After synchronizing, the device removes the declaration.

![Unassign the configuration and send a push notification to initiate synchronization](/images/com.apple.devicemanagement/phases-of-software-update-enforcement07@2x.png)

## See Also

- [Deploying software updates using declarative management](deploying-software-updates-using-declarative-management.md)
  Use declarative configurations to deploy and manage software updates on managed devices.
- [Enrolling a device in a beta program](enrolling-a-device-in-a-beta-program.md)
  Use program tokens to manage beta program enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/phases-of-software-update-enforcement)*