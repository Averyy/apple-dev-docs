# Deploying software updates using declarative management

**Framework**: Device Management

Use declarative configurations to deploy and manage software updates on managed devices.

#### Overview

Instead of initiating software updates on managed devices on-demand, you can use declarative device management to declare the desired operating system version state, and delegate the task to achieve that state to the device itself. This allows for a more resilient managed software update process and increased user transparency.

#### Use the Apple Software Lookup Service

The Apple Software Lookup Service (available at ([`https://gdmf.apple.com/v2/pmv`](https://developer.apple.comhttps://gdmf.apple.com/v2/pmv)) is the official resource to obtain a list of publicly available updates, upgrades, and Background Security Improvements. It allows a device management service to query releases as soon as Apple publishes them, and calculate applicability for each hardware model in a timely and accurate manner.

The JSON response contains three lists of available software releases:

- `PublicAssetSets`: This list contains the latest releases available to the general public if they try to update or upgrade.
- `AssetSets`: This list is a subset of `PublicAssetSets` and contains all the releases available for device management services to push to devices.
- `PublicBackgroundSecurityImprovements`: This list contains Background Security Improvement releases currently available for Apple devices.

Each element in the list contains the `ProductVersion` number and `Build` of the operating system, the `PostingDate` when the release was published, the `ExpirationDate`, and a list of `SupportedDevices` for that release. The device list matches the `ProductName` or `PRODUCT` value from the device, which is returned in a [`DeviceInformationResponse`](deviceinformationresponse.md), the initial [`Authenticate`](authenticate.md) request, or in the [`MachineInfo`](machineinfo.md) when the device tries to enroll.

The expiration date, typically set to 180 days after the posting date, defines the date the signing of the update expires. An expired update can’t be installed on devices anymore. When subsequent updates are made available, previous updates might have their expiration dates updated. If an expiration date isn’t provided, the update has yet to expire. An update has expired only when it has an expiration date in the past.

The assets are grouped by operating system platform using the following keys:

- `iOS` (which includes iPadOS, tvOS, and watchOS)
- `macOS`
- `visionOS`

The following is an example entry from the Apple Software Lookup Service:

```json
{
  "AssetSets": {
   "iOS": [
    {
"ProductVersion": "18.2.1",
"Build": "22C6161",
"PostingDate": "2025-01-06",
"ExpirationDate": "2025-04-17",
"SupportedDevices": ["iPad11,1", "iPad11,2", "iPad11,3", "iPad11,4", "iPad11,6", "iPad11,7", "iPad12,1", 
    "iPad12,2", "iPad13,1", "iPad13,10", "iPad13,11", "iPad13,16", "iPad13,17", "iPad13,18", "iPad13,19", 
    "iPad13,2", "iPad13,4", "iPad13,5", "iPad13,6", "iPad13,7", "iPad13,8", "iPad13,9", "iPad14,1", 
    "iPad14,10", "iPad14,11", "iPad14,2", "iPad14,3", "iPad14,4", "iPad14,5", "iPad14,6", "iPad14,8", 
    "iPad14,9", "iPad16,1", iPad16,2", "iPad16,3", "iPad16,4", "iPad16,5", "iPad16,6", "iPad7,11", 
    "iPad7,12", "iPad8,1", "iPad8,10", "iPad8,11", "iPad8,12", "iPad8,2", "iPad8,3", "iPad8,4", 
    "iPad8,5", "iPad8,6", "iPad8,7", "iPad8,8", "iPad8,9", "iPhone11,2", "iPhone11,4", "iPhone11,6", 
    "iPhone11,8", "iPhone12,1", "iPhone12,3", "iPhone12,5", "iPhone12,8", "iPhone13,1", "iPhone13,2", 
    "iPhone13,3", "iPhone13,4", "iPhone14,2", "iPhone14,3", "iPhone14,4", "iPhone14,5", "iPhone14,6", 
    "iPhone14,7", "iPhone14,8", "iPhone15,2", "iPhone15,3", "iPhone15,4", "iPhone15,5", "iPhone16,1", 
    "iPhone16,2", "iPhone17,1", "iPhone17,2", "iPhone17,3", "iPhone17,4"
   ]
 },
```

Use the product version list to determine which versions are later than the deviceʼs current operating system version, and are applicable to a specific device. Then provide that list of versions to the administrator as potential operating system update candidates.

#### Send a Status Report to the Device Management Service

To receive updates for status items as they change, the device management service needs to subscribe to each status report by sending a [`ManagementStatusSubscriptions`](managementstatussubscriptions.md) declaration to the device. The device then sends a `StatusReport` to the device management service when a [`ManagementStatusSubscriptions`](managementstatussubscriptions.md) declaration becomes active, if the status of a subscribed item changes, and every 24 hours.

For the purposes of monitoring operating system versions and software update status, the device management service may want to subscribe to the following status reports:

| Status report | Description |
| --- | --- |
| [`StatusDeviceOperatingSystemBuildVersion`](statusdeviceoperatingsystembuildversion.md) | The operating system’s build version on the device (for example, 21E219). |
| [`StatusDeviceOperatingSystemVersion`](statusdeviceoperatingsystemversion.md) | The operating system’s version in use on the device (for example, 17.4). |
| [`StatusDeviceOperatingSystemSupplementalBuildVersion`](statusdeviceoperatingsystemsupplementalbuildversion.md) | The operating system’s build and Background Security Improvement versions in use on the device, for example (20A123a or 20F75c). |
| [`StatusDeviceOperatingSystemSupplementalExtraVersion`](statusdeviceoperatingsystemsupplementalextraversion.md) | The operating system’s Background Security Improvement version in use on the device (for example, a). |
| [`StatusSoftwareUpdatePendingVersion`](statussoftwareupdatependingversion.md) | A dictionary that contains the build and operating system versions of the software update that’s pending on the device. |
| [`StatusSoftwareUpdateInstallState`](statussoftwareupdateinstallstate.md) | The software update installation status, which has one of values listed below. |
| [`StatusSoftwareUpdateInstallReason`](statussoftwareupdateinstallreason.md) | A dictionary with details about the reason for a pending software update. |
| [`StatusSoftwareUpdateFailureReason`](statussoftwareupdatefailurereason.md) | Details about a software update failure. The details include the number of times the software update has failed, last failure timestamp, and the failure reason. |
| [`StatusSoftwareUpdateBetaEnrollment`](statussoftwareupdatebetaenrollment.md) | The device’s enrolled beta program name, or an empty string if there is no enrolled beta program. |

The [`StatusSoftwareUpdateInstallState`](statussoftwareupdateinstallstate.md) can have one of the following values:

- `none`: There’s no software update pending, and any previous software update succeeded.
- `waiting`: A software update is waiting to start.
- `downloading`: The device is downloading a software update.
- `prepared`: The device prepared the software update and it’s ready for installation.
- `installing`: The device is installing the software update.
- `failed`: The software update failed.

The [`StatusSoftwareUpdateInstallReason`](statussoftwareupdateinstallreason.md) can have one of the following values:

- `system-settings`: It was initiated from Settings (on iOS, iPadOS, and tvOS) or System Settings (on macOS).
- `install-tonight`: It was initiated by an install tonight action.
- `auto-update`: It was initiated by an automatic update.
- `notification`: It was initiated from a user notification.
- `setup-assistant`: It was initiated during Setup Assistant.
- `command-line`: It was initiated by the softwareupdate command-line tool.
- `mdm`: It was initiated by a device management command.
- `declaration: It was initiated by a declarative device management configuration.

In addition to the other reports, device management services may also want to make [`StatusSoftwareUpdateInstallReason`](statussoftwareupdateinstallreason.md) available to administrator for support purposes, and to provide additional insight into how an update occurs. You can use this dictionary to determine whether a user initiates the update, the update happens automatically, or a software update enforcement declaration initiates it.

#### Request a Specific Minimum Software Version During Enrollment

If a device supports this capability, it returns an `MDM_CAN_REQUEST_SOFTWARE_UPDATE` key, set to `true`, in the [`MachineInfo`](machineinfo.md) data that it sends in the initial HTTP `POST` request to the device management service when the device detects a management configuration in Setup Assistant.

In addition, devices provide the following fields in the [`MachineInfo`](machineinfo.md) data which are relevant for software update management:

- `VERSION`
- `OS_VERSION`
- `SUPPLEMENTAL_BUILD_VERSION`
- `SUPPLEMENTAL_OS_VERSION_EXTRA`
- `SOFTWARE_UPDATE_DEVICE_ID`

Based on the provided information, the device management service can decide whether to enforce the device to update.

- If a device management service chooses *not* to enforce a software update, it simply returns the enrollment profile in response to the HTTP `POST` request, as it does to allow the enrollment to proceed.
- If the device management service chooses to enforce a software update, it needs to return an HTTP response with the 403 status code, and include a JSON or XML object in the response body (the HTTP `Content-Type` response header needs to be set to `application/json` or `application/xml`, respectively).

After receiving this error response, the device attempts to update to the specified version. If the update succeeds, the device restarts and the user needs to go through Setup Assistant again. The next [`MachineInfo`](machineinfo.md) HTTP `POST` request from the device to the device management service shows the updated operating system version, and the service can then proceed with enrollment. If the update fails, an error message displays to the user, and the Remote Management pane appears in Setup Assistant again.

The response schema is defined in the table below.

| Key | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | String | Yes | Needs to be set to `com.apple.softwareupdate.required`. |
| `description` | String | No | The description of the error. Used only for logging purposes. |
| `message` | String | No | The description of the error suitable for displaying to the user. |
| `details` | Dictionary | Yes | Additional data specifying the software update. |

The `details` dictionary schema is defined here.

| Key | Type | Required | Description |
| --- | --- | --- | --- |
| `OSVersion` | String | Yes | The operating system version that the device is required to update to. |
| `BuildVersion` | String | No | The build version that the device is required to update to. |
| `RequireBetaProgram` | Dictionary | No | The device enrolls in the beta program, allowing enforced software updates to beta program operating system versions. The device remains in the beta program after the enforced software update is complete. |

If you specify only `OSVersion`, a device automatically downloads and installs any Background Security Improvements available for this version. If a specific build or supplemental version is needed, a device management service can also optionally specify the `BuildVersion`. For example, to require a device to run iOS 16.5.1(a) before enrolling — although iOS 16.5.1(c) is already available — a device management service needs to set `OSVersion` to iOS 16.5.1 and `BuildVersion` to 20F770750b.

> ❗ **Important**:  Before macOS 15, only releases from the `PublicAssetSets` and `PublicBackgroundSecurityImprovements` lists can be specified. In macOS 15, assets from `AssetSets` can also be used.

#### Device Management Settings for Software Updates

The [`SoftwareUpdateSettings`](softwareupdatesettings.md) declaration consists of dictionaries that can be used to configure various aspects of the software update behavior.

After a device management service distributes different keys across multiple declarations, a device merges the settings of all active software update settings declarations. If multiple declarations configure the same key, the merge behavior depends on the individual key, which is outlined in the tables below.

#### Configure Automatic Software Updates with Device Management

The [`SoftwareUpdateSettings`](softwareupdatesettings.md) declaration offers a dictionary to define the automatic software update behavior on supervised iPhone, iPad, Mac, and Apple TV devices.

#### How a Device Management Service Handles Background Security Improvements

Background Security Improvements always apply to the latest update of an operating system, which becomes the base version of the Background Security Improvement. For example, if an iPhone has operating system version iOS 17.2 installed, then it applies the 17.2 (a) supplemental update, if one is available. In iOS 18, iPadOS 18, and macOS 15, combined updates have been made available, which allow a software update to include any available Background Security Improvements.

Prior to iOS 18, iPadOS 18, and macOS 15, a device management service may need to start two software updates to ensure that a specific supplemental version is present. First, it needs to update the device to the base version of the supplemental update, if the device isn’t already on that base version (for example, iOS 17.1 to iOS 17.2). Then it needs to update the base version to the supplemental version (for example, iOS 17.2 to iOS 17.2 (a)).

In iOS 18, iPadOS 18, and macOS 15, a device management service can specify either:

- The operating system version (which automatically installs available Background Security Improvements)
- The supplemental build version (which causes the device to perform a necessary update to the base version automatically as part of the process)

These two approaches apply to the software update enforcement configuration, and to the enforced minimum version during Automated Device Enrollment.

The [`SoftwareUpdateSettings`](softwareupdatesettings.md) declaration can also be used to configure the Background Security Improvement behavior on supervised iPhone, iPad, and Mac devices.

#### Defer a Software Update with Device Management

Deferring a software update or upgrade from 1 to 90 days is done using the [`SoftwareUpdateSettings`](softwareupdatesettings.md) declaration on supervised iPhone, iPad, and Mac devices.

A configured deferral defines the number of days before an organization offers a release to users after it becomes publicly available. Independent of a configured deferral, a device management service can still enforce a specific software update, upgrade, or Background Security Improvement on managed devices.

> **Note**:  Deferring software updates also defers any Background Security Improvements that are dependent on that version.

#### Enforce Software Updates with Device Management

To enforce a software update by a certain time on devices that enroll using Device Enrollment or Automated Device Enrollment, device management services can apply the [`SoftwareUpdateEnforcementSpecific`](softwareupdateenforcementspecific.md) declaration.

If a configuration gets applied to a device that specifies an operating system or build version that’s the same as, or older than the current device version, the device returns an error in the status report.

If multiple configurations are present with a newer operating system or build version than the current device version, the configuration with the earliest target date and time is processed first, and any others remain in the queue.

When the device updates to a new version, the set of configurations are reprocessed to determine which becomes the next one to be processed. As part of this process the device ignores any existing configurations that specify a version that is older or the same as the current one.

Here are some examples:

**Example 1:**

An iPhone has iOS 26.0 installed and you have two configurations:

- iOS 26.1 with an install date of December 20, 2025.
- iOS 26.2 with an install date of January 20, 2026.

The user is prompted to install iOS 26.1 on December 20, 2025 and again prompted to install iOS 26.2 on January 20, 2026.

**Example 2:**

An iPhone has iOS 26.0 installed and you have two configurations:

- iOS 26.1 with an install date of December 20, 2025.
- iOS 26.1 with an install date of January 20, 2026.

The user is prompted to install iOS 26.1 on December 20, 2025.

**Example 3:**

An iPhone has iOS 26.0 installed and you have two configurations:

- iOS 26.1 with an install date of January 20, 2026.
- iOS 26.2 with an install date of December 20, 2025.

The user is prompted to install iOS 26.2 on December 20, 2025, after which the device reevaluates the configurations and ignores the one for iOS 26.1, as the currently installed version is newer than the requested one.

The operating system automatically installs any available Background Security Improvements if a device management service defines only the `TargetOSVersion`. To target a specific release or Background Security Improvement, a device management service can use the `TargetBuildVersion` key in addition to specifying the build, including the supplemental version identifier.

#### Notifications

The `Notifications` key changes the default notification behavior to show only a notification 1 hour before the enforcement time and the restart countdown.

#### Use the Bootstrap Token for Mac Computers with Apple Silicon

To authorize an enforced software update on a supervised Mac computer with Apple silicon, a device management service can request and escrow a bootstrap token. This allows for a completely seamless software update experience, and avoids the need for user interaction as part of the process. When needed, the device uses a [`GetBootstrapTokenRequest`](getbootstraptokenrequest.md) to retrieve the bootstrap token from the device management service.

In the first step, the device management service determines whether the device supports a bootstrap token using the [`SecurityInfoCommand`](securityinfocommand.md). If the response includes a `BootstrapTokenRequiredForSoftwareUpdate` that’s set to `true`, the device can use a bootstrap token to authorize a software update.

To create a bootstrap token, the device management service needs to add `com.apple.mdm.bootstraptoken` to the `ServerCapabilities` array in the [`MDM`](mdm.md) profile.

After the device receives the bootstrap token, it creates a bootstrap token the next time a secure token-enabled user logs in. It then reaches out to the check-in endpoint of the device management service and escrows the token using a [`Set Bootstrap Token`](set-bootstrap-token.md) request.

## See Also

- [Phases of software update enforcement](phases-of-software-update-enforcement.md)
  Enforcing software updates on Apple devices goes through specific phases.
- [Enrolling a device in a beta program](enrolling-a-device-in-a-beta-program.md)
  Use program tokens to manage beta program enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deploying-software-updates-using-declarative-management)*