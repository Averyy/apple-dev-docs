# DeviceInformationResponse.QueryResponses.OSUpdateSettings

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The response dictionary that contains operating system update settings.

**Availability**:
- macOS 10.11+ - Deprecated in 26.0

## Declaration

```
object DeviceInformationResponse.QueryResponses.OSUpdateSettings
```

## Properties

- `AutoCheckEnabled` (boolean) *(deprecated)*: ~~The preference to automatically check for app updates.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `AutomaticAppInstallationEnabled` (boolean) *(deprecated)*: ~~The preference to automatically install app updates.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `AutomaticOSInstallationEnabled` (boolean) *(deprecated)*: ~~The preference to automatically install operating system updates.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `AutomaticSecurityUpdatesEnabled` (boolean) *(deprecated)*: ~~The preference to automatically install system data files and security updates.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `BackgroundDownloadEnabled` (boolean) *(deprecated)*: ~~The preference to download app updates in the background.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `CatalogURL` (string) *(deprecated)*: ~~The URL to the software update catalog the client is using.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `IsDefaultCatalog` (boolean) *(deprecated)*: ~~If `true`, `CatalogURL` is the default catalog.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `PerformPeriodicCheck` (boolean) *(deprecated)*: ~~If `true`, start a new scan.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `PreviousScanDate` (date) *(deprecated)*: ~~The date of the last software update scan.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+
- `PreviousScanResult` (string) *(deprecated)*: ~~The result code of last software update scan; `0` = success.~~

  ~~Deprecated: macOS 11+~~
  Removed: macOS 15+

## See Also

### Objects
- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](./accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](./autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](./mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](./organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](./servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.
- [object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings](./softwareupdatesettings-data.dictionary.md)
  The response dictionary that contains information about the Software Update pane in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/osupdatesettings-data.dictionary)*