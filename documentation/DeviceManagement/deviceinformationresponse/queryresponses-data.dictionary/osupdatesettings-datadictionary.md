# DeviceInformationResponse.QueryResponses.OSUpdateSettings

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that contains operating system update settings.

**Availability**:
- macOS 10.11+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DeviceInformationResponse.QueryResponses.OSUpdateSettings
```

## Properties

- `AutoCheckEnabled` (boolean): The preference to automatically check for app updates. This value is available in macOS 10.11 and later.
- `AutomaticAppInstallationEnabled` (boolean): The preference to automatically install app updates. This value is available in macOS 10.11 and later.
- `AutomaticOSInstallationEnabled` (boolean): The preference to automatically install operating system updates. This value is available in macOS 10.11 and later.
- `AutomaticSecurityUpdatesEnabled` (boolean): The preference to automatically install system data files and security updates. This value is available in macOS 10.11 and later.
- `BackgroundDownloadEnabled` (boolean): The preference to download app updates in the background. This value is available in macOS 10.11 and later.
- `CatalogURL` (string): The URL to the software update catalog the client is using. This value is available in macOS 10.11 and later.
- `IsDefaultCatalog` (boolean): If `true`, `CatalogURL` is the default catalog. This value is available in macOS 10.11 and later.
- `PerformPeriodicCheck` (boolean): If `true`, start a new scan. This value is available in macOS 10.11 and later.
- `PreviousScanDate` (date): The date of the last software update scan. This value is available in macOS 10.11 and later.

## See Also

- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](deviceinformationresponse/queryresponses-data.dictionary/accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](deviceinformationresponse/queryresponses-data.dictionary/mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](deviceinformationresponse/queryresponses-data.dictionary/organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.
- [object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings](deviceinformationresponse/queryresponses-data.dictionary/softwareupdatesettings-data.dictionary.md)
  The response dictionary that contains information about the Software Update pane in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/osupdatesettings-data.dictionary)*