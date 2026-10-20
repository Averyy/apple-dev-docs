# DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The response dictionary that contains information about the Software Update pane in Settings.

**Availability**:
- iOS 14.5+ - Deprecated in 26.0
- iPadOS 14.5+ - Deprecated in 26.0
- Mac Catalyst 14.5+ - Deprecated in 26.0

## Declaration

```
object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings
```

## Properties

- `RecommendationCadence` (integer) *(deprecated)*: ~~Which software updates to present to the user.~~

  ~~- `0`: Allows all updates (the default value).~~ ~~- `1`: Allows only older updates.~~ ~~- `2`: Allows only newer updates.~~

  ~~No effect if the device qualifies for only a single update.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+~~
  Removed: iOS 27+ | iPadOS 27+

## See Also

### Objects
- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](./accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](./autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](./mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OSUpdateSettings](./osupdatesettings-data.dictionary.md)
  The response dictionary that contains operating system update settings.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](./organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](./servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/softwareupdatesettings-data.dictionary)*