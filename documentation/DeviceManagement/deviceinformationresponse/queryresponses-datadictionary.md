# DeviceInformationResponse.QueryResponses

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that contains information about the device.

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
object DeviceInformationResponse.QueryResponses
```

## Topics

### Objects
- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](deviceinformationresponse/queryresponses-data.dictionary/accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](deviceinformationresponse/queryresponses-data.dictionary/mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OSUpdateSettings](deviceinformationresponse/queryresponses-data.dictionary/osupdatesettings-data.dictionary.md)
  The response dictionary that contains operating system update settings.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](deviceinformationresponse/queryresponses-data.dictionary/organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.
- [object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings](deviceinformationresponse/queryresponses-data.dictionary/softwareupdatesettings-data.dictionary.md)
  The response dictionary that contains information about the Software Update pane in Settings.

## Properties

- `AccessibilitySettings` (DeviceInformationResponse.QueryResponses.AccessibilitySettings): The current state of settable accessibility settings. Available: iOS 16+ | iPadOS 16+ | watchOS 10+
- `ActiveManagedUsers` ([string]): An array of the directory GUIDs of the logged-in managed users. If one of these users is currently logged in to the console, the `CurrentConsoleManagedUser` key returns the GUID of that user. Requires the Device Information access right. Available: macOS 10.11+
- `AppAnalyticsEnabled` (boolean): If `true`, the device is sharing app analytics. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+ | visionOS 1.1+ | watchOS 10+
- `AutoSetupAdminAccounts` ([DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem]): The contents of [`DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem`](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md), which Setup Assistant automatically creates during ADE enrollment. Requires the Device Information access right. Available: macOS 10.11+
- `AvailableDeviceCapacity` (number): The available capacity in floating-point base-10 gigabytes (GB) in iOS and macOS 12 or later. The capacity is in base-2 gibibytes (GiB) in macOS 11 and earlier. Requires the Device Information access right. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | visionOS 1.1+ | watchOS 10+
- `AwaitingConfiguration` (boolean): If `true` on the device channel, the device is still waiting for a [`Device Configured`](device-configured-command.md) command to continue through Setup Assistant. If `true` on the user channel (Shared iPad only), the device is still waiting for a [`User Configured`](user-configured-command.md) command to continue through Setup Assistant and finish login. Available: iOS 9+ | iPadOS 9+ | macOS 10.11+ | tvOS 10.2+ | visionOS 2+ | watchOS 10+
- `BatteryLevel` (number): The battery level, between `0.0` and `1.0`, or `-1.0` if MDM can’t determine the battery level. Requires the Device Information access right. Available: iOS 5+ | iPadOS 5+ | macOS 13.3+ | visionOS 1.1+ | watchOS 10+
- `BluetoothMAC` (string): The Bluetooth media access control (MAC) address. Requires the Network Information access right. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | tvOS 9+ | visionOS 1.1+
- `BuildVersion` (string): The operating system version. Requires the Device Information access right.
- `CarrierSettingsVersion` (string): Removed: iOS 26+ | iPadOS 26+
- `CellularTechnology` (integer): The cellular technology type, which is one of the following values: - `0`: None
- `1`: GSM
- `2`: CDMA
- `3`: GSM and CDMA Requires the Device Information access right. Available: iOS 4.2.6+ | iPadOS 4.2.6+
- `CurrentCarrierNetwork` (string): Removed: iOS 26+ | iPadOS 26+
- `CurrentMCC` (string): Removed: iOS 26+ | iPadOS 26+
- `CurrentMNC` (string): Removed: iOS 26+ | iPadOS 26+
- `DataRoamingEnabled` (boolean): If `true`, the device has enabled data roaming. Requires the Network Information access right. Available: iOS 5+ | iPadOS 5+
- `DeviceCapacity` (number): The total capacity in floating-point base-10 gigabytes (GB) on iOS and macOS 12 or later. The capacity is in base-2 gibibytes (GiB) on macOS 11 and earlier. Requires the Device Information access right. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | visionOS 1.1+ | watchOS 10+
- `DeviceID` (string): The device identifier. Requires the Device Information access right. Available: tvOS 9+
- `DeviceName` (string): The device name. Requires the Device Information access right.
- `DevicePropertiesAttestation` ([data]): The key to get an attestation of the device’s properties. See the hardware requirements for attestation below. The value is an array of certificates in DER form that forms a certificate chain. The chain is rooted with the Apple CA `Apple Enterprise Attestation Root CA`. The first array item is the leaf certificate. The leaf certificate contains custom OIDs describing a device. The OS version of the device, and the type of enrollment, determine which OIDs are present in the certificate. If Apple’s attestation servers are unable to verify a device property they generate a blank value, omit the OID entirely, or refuse to issue an attestation certificate. The following OIDs were introduced in iOS 16, iPadOS 16, tvOS 16, watchOS 10, visionOS 1 and macOS 14: - `1.2.840.113635.100.8.9.1` serial number: This is the serial number of the device. It’s omitted if the enrollment is a user enrollment.
- `1.2.840.113635.100.8.9.2` UDID: For a Mac this has the same value as the `ProvisioningUDID` key, and doesn’t match the UDID used elsewhere in the MDM protocol. It’s omitted if the enrollment is a user enrollment.
- `1.2.840.113635.100.8.10.2` sepOS version: This is the version of the operating system running on the Secure Enclave when the attestation is generated. Typically this matches the version of the main operating system.
- `1.2.840.113635.100.8.11.1` Freshness code: This is the freshness code. See the `DeviceAttestationNonce`. This may not match the requested freshness code if the device returned a cached attestation. The following OIDs were introduced in iOS 17.2, iPadOS 17.2, tvOS 17.2, watchOS 10.2, visionOS 1.l0, and macOS 14.2: - `1.2.840.113635.100.8.9.4` Software Update Device ID: This is an identifier of the device model. It’s expected to match the `SoftwareUpdateDeviceID` in the `DeviceInformation`` response. This is the device identifier to use when looking up available OS updates through [`https://gdmf.apple.com/v2/pmv`](https://developer.apple.comhttps://gdmf.apple.com/v2/pmv).
- `1.2.840.113635.100.8.10.1` OS Version: This is the version of iOS, iPadOS or tvOS running on the device when the attestation is generated.
- `1.2.840.113635.100.8.10.3` LLB Version: This is the version of the Low Level Bootloader firmware running on the device when the attestation is generated. For more information about the boot process, see the documentation of the boot process in the Apple Platform Security guide. The following OIDs were introduced in macOS 14.2: - `1.2.840.113635.100.8.13.1` System Integrity Protection (SIP) status: This indicates whether SIP is enabled or disabled when the attestation is generated. `0` indicates enabled, `1` indicates disabled.
- `1.2.840.113635.100.8.13.2` Secure boot status: This describes part of the configuration of the LocalPolicy when the attestation is generated. The values are `Full Security`, `Reduced Security`, or `Permissive Security`. For a description of these values see the Apple Platform Security guide.
- `1.2.840.113635.100.8.13.3` Third party kernel extensions allowed: This indicates whether third party kernel extensions are allowed. A value of `0` indicates third party kernel extensions aren’t allowed. Any other value means that some kinds of third party kernel extensions are allowed. Available: iOS 16+ | iPadOS 16+ | macOS 14+ | tvOS 16+ | visionOS 1.1+ | watchOS 10+
- `DiagnosticSubmissionEnabled` (boolean): If `true`, the device has enabled diagnostic submission. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+ | visionOS 1.1+ | watchOS 10+
- `EACSPreflight` (string): Specifies whether the device can perform an [`EraseDeviceCommand`](erasedevicecommand.md) using Erase All Content and Settings (EACS), which is one of the following values: - `success`: The device supports EACS.
- `not supported`: The device is too old to support EACS.
- `unknown failure`: A problem occurred for which there isn’t a more specific error message.
- `(other string)`: A reason why the device can’t perform EACS, such as “System is not sealed” Available: macOS 13.3+
- `EASDeviceIdentifier` (string): The device identifier for Exchange Active Sync (EAS). Requires the Device Information access right. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+
- `EstimatedResidentUsers` (integer): The estimated number of users that can use this Shared iPad device, according to the space available on the device and each user’s quota. Requires the Device Information access right. Available: iOS 14+ | iPadOS 14+
- `EthernetMAC` (string): The primary Ethernet MAC address. Requires the Network Information access right. Available: macOS 10.7+
- `HasBattery` (boolean): If `true`, the device has an internal battery. Available: macOS 13.3+
- `HostName` (string): The host name. Available: macOS 10.11+
- `ICCID` (string): Removed: iOS 26+ | iPadOS 26+
- `IMEI` (string): Removed: iOS 26+ | iPadOS 26+
- `IsActivationLockEnabled` (boolean): If `true`, the device has enabled Activation Lock. Requires the Device Information access right. Available as of iOS 7 and macOS 10.9, and deprecated in iOS 16 and macOS 13. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | watchOS 10+
Deprecated: iOS 16+ | iPadOS 16+ | macOS 13+ | watchOS 10+
- `IsActivationLockSupported` (boolean): If `true`, the device supports Activation Lock. Also see `IsActivationLockManageable` in [`SecurityInfoResponse.SecurityInfo.ManagementStatus`](securityinforesponse/securityinfo-data.dictionary/managementstatus-data.dictionary.md). Available: macOS 10.9+
- `IsAppleSilicon` (boolean): If `true`, the macOS device uses an Apple silicon chip. Available: macOS 12+
- `IsCloudBackupEnabled` (boolean): If `true`, the device has enabled iCloud backup. Requires the Device Information access right. Available: iOS 7.1+ | iPadOS 7.1+ | visionOS 1.1+
- `IsDeviceLocatorServiceEnabled` (boolean): If `true`, the device has enabled a device locator service, such as Find My. Requires the Device Information access right. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+ | watchOS 10+
- `IsDoNotDisturbInEffect` (boolean): If `true`, the device is in Do Not Disturb (DND) mode. This value is `true` even if DND is only in effect for a locked device. Requires the Device Information access right. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+ | watchOS 10+
- `IsMDMLostModeEnabled` (boolean): If `true`, the device has enabled Managed Lost Mode. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+ | watchOS 10+
- `IsMultiUser` (boolean): If `true`, the device is a Shared iPad. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+
- `IsNetworkTethered` (boolean): If `true`, the device is network-tethered. Requires the Network Information access right. Available: iOS 10.3+ | iPadOS 10.3+
- `IsRoaming` (boolean): Removed: iOS 26+ | iPadOS 26+
- `IsSupervised` (boolean): If `true`, it’s a supervised device. Requires the Device Information access right. Available: iOS 6+ | iPadOS 6+ | macOS 10.15+ | tvOS 9+ | visionOS 1.1+ | watchOS 10+
- `iTunesStoreAccountHash` (string): A hash of the logged-in iTunes Store account. Also see [`GetVppUserRequest`](getvppuserrequest.md). Requires the App Installation access right. Available: iOS 8+ | iPadOS 8+ | macOS 10.10+ | tvOS 9+ | watchOS 10+
- `iTunesStoreAccountIsActive` (boolean): If `true`, the device has an active iTunes Store account. Requires the App Installation access right. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 9+ | watchOS 10+
- `LastCloudBackupDate` (date): The date of the last iCloud backup. Available: iOS 8+ | iPadOS 8+ | visionOS 1.1+
- `LocalHostName` (string): The local host name from Bonjour. Available: macOS 10.11+
- `ManagedAppleIDDefaultDomains` ([string]): The list of domains that the device suggests on the Shared iPad login screen. Available: iOS 16+ | iPadOS 16+
- `MaximumResidentUsers` (integer): The maximum number of users that can use this Shared iPad device. Starting with iOS 13.4, the value that returns is always `32`. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+
- `MDMOptions` (DeviceInformationResponse.QueryResponses.MDMOptions): The contents of [`SettingsCommand.Command.Settings.MDMOptions.MDMOptions`](settingscommand/command-data.dictionary/settings-data.dictionary/mdmoptions-data.dictionary/mdmoptions-data.dictionary.md). Available: iOS 7+ | iPadOS 7+ | macOS 11+ | tvOS 9+ | visionOS 1.1+ | watchOS 10+
- `MEID` (string): Removed: iOS 26+ | iPadOS 26+
- `Model` (string): The model. Requires the Device Information access right. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | tvOS 9+ | watchOS 10+
- `ModelName` (string): The model name, such as *iPhone*. Requires the Device Information access right.
- `ModelNumber` (string): The device’s hardware model number including region info, for example, `MK1A3LL/A`. Requires the Device Information access right. Requires a Mac with Apple silicon on macOS.
- `ModemFirmwareVersion` (string): The modem firmware version. Requires the Device Information access right. Available: iOS 4+ | iPadOS 4+
- `OnlineAuthenticationGracePeriod` (integer): The grace period for Shared iPad online authentication (in days). A value of `0` indicates that the device requires online authentication for every login. Available: iOS 16+ | iPadOS 16+
- `OrganizationInfo` (DeviceInformationResponse.QueryResponses.OrganizationInfo): The contents of [`SettingsCommand.Command.Settings.OrganizationInfo.OrganizationInfo`](settingscommand/command-data.dictionary/settings-data.dictionary/organizationinfo-data.dictionary/organizationinfo-data.dictionary.md). Available: iOS 7+ | iPadOS 7+ | macOS 10.11+ | tvOS 9+ | visionOS 1.1+ | watchOS 10+
- `OSUpdateSettings` (DeviceInformationResponse.QueryResponses.OSUpdateSettings): Removed: use the declarative management `com.apple.configuration.softwareupdate.settings` configuration to set values. 

Removed: macOS 27+
- `OSVersion` (string): The operating system version. Requires the Device Information access right.
- `PersonalHotspotEnabled` (boolean): If `true,` the device has enabled Personal Hotspot, which isn’t available for all carriers. Requires the Network Information access right. Available: iOS 7+ | iPadOS 7+
- `PhoneNumber` (string): Removed: iOS 26+ | iPadOS 26+
- `PINRequiredForDeviceLock` (boolean): If `true`, the [`DeviceLockCommand`](devicelockcommand.md) requires a PIN. Available: macOS 11+
- `PINRequiredForEraseDevice` (boolean): If `true`, the [`EraseDeviceCommand`](erasedevicecommand.md) requires a PIN. Available: macOS 11+
- `ProductName` (string): The product name, such as *iPad8,12*. Requires the Device Information access right.
- `ProvisioningUDID` (string): The device identifier to use in provisioning profiles. This value differs from the UDID on a Mac with Apple silicon. Available: macOS 11.3+
- `PushToken` (data): The push token for the user-channel connection, in the same format as in [`TokenUpdateRequest`](tokenupdaterequest.md). MDM ignores this query for the device channel. Requires the Device Information access right. Available: iOS 9.3+ | iPadOS 9.3+ | macOS 10.12+
- `QuotaSize` (integer): The quota size in megabytes for each user on this Shared iPad device. Requires the Device Information access right. Available: iOS 13.4+ | iPadOS 13.4+
- `ResidentUsers` (integer): The number of users currently on this Shared iPad device. Requires the Device Information access right. Available: iOS 13.4+ | iPadOS 13.4+
- `SerialNumber` (string): The serial number. Requires the Device Information access right.
- `ServiceSubscriptions` ([DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty]): The contents of [`DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty`](deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty.md). Requires the Network Information access right. Available: iOS 12+ | iPadOS 12+
- `SIMCarrierNetwork` (string): Removed: iOS 5+ | iPadOS 5+
- `SIMMCC` (string): Removed: iOS 4.2.6+ | iPadOS 4.2.6+
- `SIMMNC` (string): Removed: iOS 4.2.6+ | iPadOS 4.2.6+
- `SkipLanguageAndLocaleSetupForNewUsers` (boolean): If `true`, skip the language and country/region panes for new users on Shared iPad. Available: iOS 16.2+ | iPadOS 16.2+
- `SoftwareUpdateDeviceID` (string): Removed: subscribe to the declarative management `softwareupdate.device-id` status item. 

Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | visionOS 27+
- `SoftwareUpdateSettings` (DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings): Removed: use the declarative management `com.apple.configuration.softwareupdate.settings` configuration to set values. 

Removed: iOS 27+ | iPadOS 27+
- `SubscriberCarrierNetwork` (string): Removed: iOS 26+ | iPadOS 26+
- `SubscriberMCC` (string): Removed: iOS 26+ | iPadOS 26+
- `SubscriberMNC` (string): Removed: iOS 26+ | iPadOS 26+
- `SupplementalBuildVersion` (string): The supplemental OS build version. Available: iOS 16.1+ | iPadOS 16.1+ | macOS 13+ | tvOS 16.1+ | visionOS 1.1+ | watchOS 10+
- `SupplementalOSVersionExtra` (string): The OS update Background Security Improvement version letter. Available: iOS 16.1+ | iPadOS 16.1+ | macOS 13+ | tvOS 16.1+ | visionOS 1.1+ | watchOS 10+
- `SupportsiOSAppInstalls` (boolean): If `true`, the device supports iOS or iPadOS app installs through MDM. Available: macOS 11+
- `SupportsLOMDevice` (boolean): If `true`, the device can receive `PowerON`, `PowerOFF`, and `Reset` commands from a lights-out management (LOM) controller. Available: macOS 11+
- `SystemIntegrityProtectionEnabled` (boolean): If `true`, the device has enabled System Integrity Protection. Requires the Device Information access right. Available: macOS 10.12+
- `TemporarySessionOnly` (boolean): If `true`, the device allows only temporary sessions. Available: iOS 14.5+ | iPadOS 14.5+
- `TemporarySessionTimeout` (integer): The timeout interval for the temporary session. A value of `0` indicates that there’s no timeout. Available: iOS 14.5+ | iPadOS 14.5+
- `TimeZone` (string): The current Internet Assigned Numbers Authority (IANA) time zone database name. Requires the Device Information access right. Available: iOS 14+ | iPadOS 14+ | tvOS 14+ | visionOS 1.1+ | watchOS 10+
- `UDID` (string): The unique identifier of the device.
- `UserSessionTimeout` (integer): The timeout interval for the user session. A value of `0` indicates that there’s no timeout. Available: iOS 14.5+ | iPadOS 14.5+
- `VoiceRoamingEnabled` (boolean): Removed: iOS 26+ | iPadOS 26+
- `WiFiMAC` (string): The Wi-Fi MAC address. Requires the Network Information access right.

## See Also

- [object DeviceInformationResponse.ErrorChainItem](deviceinformationresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary)*