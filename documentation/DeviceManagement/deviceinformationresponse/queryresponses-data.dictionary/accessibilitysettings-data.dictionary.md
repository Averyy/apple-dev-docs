# DeviceInformationResponse.QueryResponses.AccessibilitySettings

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The response dictionary that contains the devices accessibility settings.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 10.0+

## Declaration

```
object DeviceInformationResponse.QueryResponses.AccessibilitySettings
```

## Properties

- `BoldTextEnabled` (boolean): If `true`, the device has enabled bold text.
- `GrayscaleEnabled` (boolean): If `true`, the device has enabled grayscale display.

  Available: watchOS 10+
- `IncreaseContrastEnabled` (boolean): If `true`, the device has enabled increase contrast.

  Available: iOS 16+ | iPadOS 16+
- `ReduceMotionEnabled` (boolean): If `true`, the device has enabled reduced motion.
- `ReduceTransparencyEnabled` (boolean): If `true`, the device has enabled reduced transparency.
- `TextSize` (integer): The accessibility text size apps that support dynamic text use. 0 is the smallest value, and 11 is the largest available.

  `-1` indicates that the current size is unknown or hasn’t been explicitly set.

  **Allowed Values**: `-1`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`
- `TouchAccommodationsEnabled` (boolean): If `true`, the device has enabled touch accommodations.
- `VoiceOverEnabled` (boolean): If `true`, the device has enabled voiceover.
- `ZoomEnabled` (boolean): If `true`, the device has enabled zoom.

## See Also

### Objects
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
- [object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings](./softwareupdatesettings-data.dictionary.md)
  The response dictionary that contains information about the Software Update pane in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/accessibilitysettings-data.dictionary)*