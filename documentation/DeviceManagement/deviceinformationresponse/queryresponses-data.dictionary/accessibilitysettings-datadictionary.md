# DeviceInformationResponse.QueryResponses.AccessibilitySettings

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that contains the devices accessibility settings.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 10.0+

## Declaration

```swift
object DeviceInformationResponse.QueryResponses.AccessibilitySettings
```

## Properties

- `BoldTextEnabled` (boolean): If `true`, the device has enabled bold text.
- `GrayscaleEnabled` (boolean): If `true`, the device has enabled grayscale display. Available: watchOS 10+
- `IncreaseContrastEnabled` (boolean): If `true`, the device has enabled increase contrast. Available: iOS 16+ | iPadOS 16+
- `ReduceMotionEnabled` (boolean): If `true`, the device has enabled reduced motion.
- `ReduceTransparencyEnabled` (boolean): If `true`, the device has enabled reduced transparency.
- `TextSize` (integer): The accessibility text size apps that support dynamic text use. 0 is the smallest value, and 11 is the largest available. `-1` indicates that the current size is unknown or hasn’t been explicitly set.
- `TouchAccommodationsEnabled` (boolean): If `true`, the device has enabled touch accommodations.
- `VoiceOverEnabled` (boolean): If `true`, the device has enabled voiceover.
- `ZoomEnabled` (boolean): If `true`, the device has enabled zoom.

## See Also

- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](deviceinformationresponse/queryresponses-data.dictionary/mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](deviceinformationresponse/queryresponses-data.dictionary/organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/accessibilitysettings-data.dictionary)*