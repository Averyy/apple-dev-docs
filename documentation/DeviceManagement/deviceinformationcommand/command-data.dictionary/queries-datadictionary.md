# DeviceInformationCommand.Command.Queries

**Framework**: Device Management  
**Kind**: dictionary

An array of query dictionaries to get information about a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object DeviceInformationCommand.Command.Queries
```

## Properties

- `AccessibilitySettings` (string): The key to get the current state of settable accessibility settings. Available: iOS 16+ | iPadOS 16+ | watchOS 10+
- `ActiveManagedUsers` (string): The key to get an array of directory GUIDs for logged-in managed users. Requires the Device Information access right. Available: macOS 10.11+
- `AppAnalyticsEnabled` (string): The key to determine whether the device is sharing app analytics. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+ | visionOS 1.1+ | watchOS 10+
- `AutoSetupAdminAccounts` (string): The key to get the contents of [`DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem`](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md), which Setup Assistant automatically creates during enrollment. Requires the Device Information access right. Available: macOS 10.11+
- `AvailableDeviceCapacity` (string): The key to get the available capacity. Requires the Device Information access right. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | visionOS 1.1+ | watchOS 10+
- `AwaitingConfiguration` (string): The key to determine whether the device is waiting for a [`Device Configured`](device-configured-command.md) command or [`User Configured`](user-configured-command.md) command to continue through Setup Assistant on the device channel or user channel, respectively. Available: iOS 9+ | iPadOS 9+ | macOS 10.11+ | tvOS 10.2+ | visionOS 2+ | watchOS 10+
- `BatteryLevel` (string): The key to get the battery level. Requires the Device Information access right. Available: iOS 5+ | iPadOS 5+ | macOS 13.3+ | visionOS 1.1+ | watchOS 10+
- `BluetoothMAC` (string): The key to get the Bluetooth media access control (MAC) address. Requires the Network Information access right. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | tvOS 9+ | visionOS 1.1+
- `BuildVersion` (string): The key to get the operating system version. Requires the Device Information access right.
- `CarrierSettingsVersion` (string): Removed: iOS 26+ | iPadOS 26+
- `CellularTechnology` (string): The key to get the cellular technology type. Requires the Device Information access right. Available: iOS 4.2.6+ | iPadOS 4.2.6+
- `CurrentCarrierNetwork` (string): Removed: iOS 26+ | iPadOS 26+
- `CurrentMCC` (string): Removed: iOS 26+ | iPadOS 26+
- `CurrentMNC` (string): Removed: iOS 26+ | iPadOS 26+
- `DataRoamingEnabled` (string): The key to determine whether the system enabled data roaming on the device. Requires the Network Information access right. Available: iOS 5+ | iPadOS 5+
- `DeviceCapacity` (string): The key to get the device’s total capacity. Requires the Device Information access right. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | visionOS 1.1+ | watchOS 10+
- `DeviceID` (string): The key to get the device ID. Requires the Device Information access right. Available: tvOS 9+
- `DeviceName` (string): The key to get the device name. Requires the Device Information access right.
- `DevicePropertiesAttestation` (string): The key to get an attestation of the device’s properties. See the hardware requirements for attestation below. Available: iOS 16+ | iPadOS 16+ | macOS 14+ | tvOS 16+ | visionOS 1.1+ | watchOS 10+
- `DiagnosticSubmissionEnabled` (string): The key to determine whether the system enabled the diagnostic submission setting on the device. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+ | visionOS 1.1+ | watchOS 10+
- `EACSPreflight` (string): The key to determine whether the device can perform an [`EraseDeviceCommand`](erasedevicecommand.md) using Erase All Content and Settings (EACS). Available: macOS 13.3+
- `EASDeviceIdentifier` (string): The key to get the device identifier for Exchange ActiveSync (EAS). Requires the Device Information access right. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+
- `EstimatedResidentUsers` (string): The key to get the estimated number of users that can use this Shared iPad device, according to the available space of the device and each user’s quota. Requires the Device Information access right. Available: iOS 14+ | iPadOS 14+
- `EthernetMAC` (string): The key to get the primary Ethernet MAC address. Requires the Network Information access right. Available: macOS 10.7+
- `HasBattery` (string): The key to determine whether the device has an internal battery. Available: macOS 13.3+
- `HostName` (string): The key to get the hostname. Available: macOS 10.11+
- `ICCID` (string): Removed: iOS 26+ | iPadOS 26+
- `IMEI` (string): Removed: iOS 26+ | iPadOS 26+
- `IsActivationLockEnabled` (string): The key to determine whether the system enabled Activation Lock on the device. Requires the Device Information access right. Available as of iOS 7 and macOS 10.15, and deprecated in iOS 16 and macOS 13. Available: iOS 7+ | iPadOS 7+ | macOS 10.15+ | watchOS 10+
Deprecated: iOS 16+ | iPadOS 16+ | macOS 13+ | watchOS 10+
- `IsActivationLockSupported` (string): The key to determine whether the device supports Activation Lock. Also see `IsActivationLockManageable` in [`SecurityInfoResponse.SecurityInfo.ManagementStatus`](securityinforesponse/securityinfo-data.dictionary/managementstatus-data.dictionary.md). Available: macOS 10.15+
- `IsAppleSilicon` (string): The key to determine whether the device is a Mac with Apple silicon (for example, an Apple M1 chip). Available: macOS 12+
- `IsCloudBackupEnabled` (string): The key to determine whether the system enabled iCloud Backup on the device. Requires the Device Information access right. Available: iOS 7.1+ | iPadOS 7.1+ | visionOS 1.1+
- `IsDeviceLocatorServiceEnabled` (string): The key to determine whether the system enabled a device locator service such as Find My on the device. Requires the Device Information access right. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+ | watchOS 10+
- `IsDoNotDisturbInEffect` (string): The key to determine whether the device is in Do Not Disturb (DND) mode. Requires the Device Information access right. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+ | watchOS 10+
- `IsMDMLostModeEnabled` (string): The key to determine whether the system enabled Managed Lost Mode on the device. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+ | watchOS 10+
- `IsMultiUser` (string): The key to determine whether the device is a Shared iPad. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+
- `IsNetworkTethered` (string): The key to determine whether the device is network-tethered. Requires the Network Information access right. Available: iOS 10.3+ | iPadOS 10.3+
- `IsRoaming` (string): Removed: iOS 26+ | iPadOS 26+
- `IsSupervised` (string): The key to determine whether the device is supervised. Requires the Device Information access right. Available: iOS 6+ | iPadOS 6+ | macOS 10.15+ | tvOS 9+ | visionOS 1.1+ | watchOS 10+
- `iTunesStoreAccountHash` (string): The key to get a hash of the logged-in iTunes Store account. Also see [`GetVppUserRequest`](getvppuserrequest.md). Requires the App Installation access right. Available: iOS 8+ | iPadOS 8+ | macOS 10.10+ | tvOS 9+ | watchOS 10+
- `iTunesStoreAccountIsActive` (string): The key to determine whether the iTunes Store account is active. Requires the App Installation access right. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 9+ | watchOS 10+
- `LastCloudBackupDate` (string): The key to get the date of the most-recent iCloud backup. Available: iOS 8+ | iPadOS 8+ | visionOS 1.1+
- `LocalHostName` (string): The key to get the local hostname from Bonjour. Available: macOS 10.11+
- `ManagedAppleIDDefaultDomains` (string): The key to get the list of domains that the device suggests on the Shared iPad login screen. Available: iOS 16+ | iPadOS 16+
- `MaximumResidentUsers` (string): The key to get the maximum number of users that can use this Shared iPad device. In iOS 13.4 and later, this value is always `32`. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+
- `MDMOptions` (string): The key to get the contents of [`SettingsCommand.Command.Settings.MDMOptions.MDMOptions`](settingscommand/command-data.dictionary/settings-data.dictionary/mdmoptions-data.dictionary/mdmoptions-data.dictionary.md). Available: iOS 7+ | iPadOS 7+ | macOS 11+ | tvOS 9+ | visionOS 1.1+ | watchOS 10+
- `MEID` (string): Removed: iOS 26+ | iPadOS 26+
- `Model` (string): The key to get the model. Requires the Device Information access right. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | tvOS 9+ | watchOS 10+
- `ModelName` (string): The key to get the model name, such as *iPhone*. Requires the Device Information access right.
- `ModelNumber` (string): The key to get the device’s hardware model number, including region info, such as `MK1A3LL/A`. Requires the Device Information access right. Requires a Mac with Apple silicon for macOS. Available: iOS 16.4+ | iPadOS 16.4+ | macOS 13.3+ | tvOS 16.4+ | visionOS 1.1+ | watchOS 10+
- `ModemFirmwareVersion` (string): The key to get the modem firmware version. Requires the Device Information access right. Available: iOS 4+ | iPadOS 4+
- `OnlineAuthenticationGracePeriod` (string): The key to get the grace period for Shared iPad online authentication (in days). Available: iOS 16+ | iPadOS 16+
- `OrganizationInfo` (string): The key to get the contents of [`SettingsCommand.Command.Settings.OrganizationInfo.OrganizationInfo`](settingscommand/command-data.dictionary/settings-data.dictionary/organizationinfo-data.dictionary/organizationinfo-data.dictionary.md). Available: iOS 7+ | iPadOS 7+ | macOS 10.11+ | tvOS 9+ | visionOS 1.1+ | watchOS 10+
- `OSUpdateSettings` (string): Removed: macOS 27+
- `OSVersion` (string): The key to get the operating system version. Requires the Device Information access right.
- `PersonalHotspotEnabled` (string): The key to determine whether the system enabled Personal Hotspot on the device, which isn’t available for all carriers. Requires the Network Information access right. Available: iOS 7+ | iPadOS 7+
- `PhoneNumber` (string): Removed: iOS 26+ | iPadOS 26+
- `PINRequiredForDeviceLock` (string): The key to determine whether the [`DeviceLockCommand`](devicelockcommand.md) requires a PIN. Available: macOS 11+
- `PINRequiredForEraseDevice` (string): The key to determine whether the [`EraseDeviceCommand`](erasedevicecommand.md) requires a PIN. Available: macOS 11+
- `ProductName` (string): The key to get the product name, such as *iPad8,12*. Requires the Device Information access right.
- `ProvisioningUDID` (string): The key to get the device identifier for provisioning profiles. This value differs from the UDID for a Mac with Apple silicon. Available: macOS 11.3+
- `PushToken` (string): The key to get the push token for the current user-channel connection. The MDM server ignores this query for the device channel. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.12+
- `QuotaSize` (string): The key to get the quota size for each user on this Shared iPad device. Requires the Device Information access right. Available: iOS 13.4+ | iPadOS 13.4+
- `ResidentUsers` (string): The key to get the number of users currently on this Shared iPad device. Requires the Device Information access right. Available: iOS 13.4+ | iPadOS 13.4+
- `SerialNumber` (string): The key to get the serial number. Requires the Device Information access right.
- `ServiceSubscriptions` (string): The key to get the contents of [`DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty`](deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty.md). Requires the Network Information access right. Available: iOS 12+ | iPadOS 12+
- `SIMCarrierNetwork` (string): Removed: iOS 5+ | iPadOS 5+
- `SkipLanguageAndLocaleSetupForNewUsers` (string): The key to determine whether the system skips the language and country/region panes for new users on Shared iPad. Available: iOS 16.2+ | iPadOS 16.2+
- `SoftwareUpdateDeviceID` (string): Removed: subscribe to the declarative management `softwareupdate.device-id` status item. 

Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | visionOS 27+
- `SoftwareUpdateSettings` (string): Removed: use the declarative management `com.apple.configuration.softwareupdate.settings` configuration to set values. 

Removed: iOS 27+ | iPadOS 27+
- `SubscriberCarrierNetwork` (string): Removed: iOS 26+ | iPadOS 26+
- `SubscriberMCC` (string): Removed: iOS 26+ | iPadOS 26+
- `SubscriberMNC` (string): Removed: iOS 26+ | iPadOS 26+
- `SupplementalBuildVersion` (string): The key to get the build version for the currently installed Background Security Improvement. If there’s no installed Background Security Improvement, this value is the same as `BuildVersion`. Requires the Device Information access right. Available: iOS 16.1+ | iPadOS 16.1+ | macOS 13+ | tvOS 16.1+ | visionOS 1.1+ | watchOS 10+
- `SupplementalOSVersionExtra` (string): The key to get the OS update Background Security Improvement version letter, if a Background Security Improvement update is installed. Requires the Device Information access right. Available: iOS 16.1+ | iPadOS 16.1+ | macOS 13+ | tvOS 16.1+ | visionOS 1.1+ | watchOS 10+
- `SupportsiOSAppInstalls` (string): The key to determine whether the macOS device supports iOS or iPadOS app installs. Available: macOS 11+
- `SupportsLOMDevice` (string): The key to determine whether the device can receive `PowerON`, `PowerOFF`, and `Reset` commands from a lights-out management (LOM) controller. Available: macOS 11+
- `SystemIntegrityProtectionEnabled` (string): The key to determine whether the system enabled System Integrity Protection on the device. Requires the Device Information access right, and is available in macOS 10.12 and later. Available: macOS 10.12+
- `TemporarySessionOnly` (string): The key to determine whether the device allows only temporary sessions. Available: iOS 14.5+ | iPadOS 14.5+
- `TemporarySessionTimeout` (string): The key to get the timeout interval for the temporary session. Available: iOS 14.5+ | iPadOS 14.5+
- `TimeZone` (string): The key to get the current Internet Assigned Numbers Authority (IANA) time zone database name. Requires the Device Information access right. Available: iOS 14+ | iPadOS 14+ | macOS 26+ | tvOS 14+ | visionOS 2+ | watchOS 10+
- `UDID` (string): The key to get the unique identifier of the device.
- `UserSessionTimeout` (string): The key to get the timeout interval for the user session. Available: iOS 14.5+ | iPadOS 14.5+
- `VoiceRoamingEnabled` (string): Removed: iOS 26+ | iPadOS 26+
- `WiFiMAC` (string): The key to get the Wi-Fi MAC address. Requires the Network Information access right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationcommand/command-data.dictionary/queries-data.dictionary)*