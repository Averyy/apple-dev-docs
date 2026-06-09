# SoftwareUpdateSettingsDeferralsObject

**Framework**: Device Management  
**Kind**: dictionary

This object configures the deferral of software updates. Background Security Improvements aren’t considered in `Major`, `Minor`, or `System` deferral mechanism.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object SoftwareUpdateSettingsDeferralsObject
```

## Properties

- `CombinedPeriodInDays` (integer): Specifies the number of days to defer a major or minor OS software update on the device. When set, software updates only appear after the specified delay, following the release of the software update. Available: iOS 18+ | iPadOS 18+ | tvOS 18.4+ | visionOS 26+
- `MajorPeriodInDays` (integer): Specifies the number of days to defer a major OS software update on the device. When set, software updates only appear after the specified delay, following the release of the software update. Available: macOS 15+
- `MinorPeriodInDays` (integer): Specifies the number of days to defer a minor OS software update on the device. It also defers major updates for iOS. When set, software updates only appear after the specified delay, following the release of the software update. Available: macOS 15+
- `SystemPeriodInDays` (integer): Specifies the number of days to defer system or non-OS updates. When set, updates only appear after the specified delay, following the release of the update. Available: macOS 15+

## See Also

- [object SoftwareUpdateSettingsAutomaticActionsObject](softwareupdatesettingsautomaticactionsobject.md)
  This object configures various automatic Software Update functionality.
- [object SoftwareUpdateSettingsBetaObject](softwareupdatesettingsbetaobject.md)
  This object configures the beta program settings for a device.
- [object SoftwareUpdateSettingsRapidSecurityResponseObject](softwareupdatesettingsrapidsecurityresponseobject.md)
  These configurations set user access to interacting with Background Security Improvement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdatesettingsdeferralsobject)*