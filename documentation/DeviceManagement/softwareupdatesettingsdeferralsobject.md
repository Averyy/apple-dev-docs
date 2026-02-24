# SoftwareUpdateSettingsDeferralsObject

**Framework**: Device Management  
**Kind**: dictionary

The object that configures update deferrals.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object SoftwareUpdateSettingsDeferralsObject
```

## Properties

- `CombinedPeriodInDays` (integer): Specifies the number of days to defer a major or minor OS software update on the device. When set, software updates only appear after the specified delay, following the release of the software update. Available in iOS 18 and later.
- `MajorPeriodInDays` (integer): Specifies the number of days to defer a major OS software update on the device. When set, software updates only appear after the specified delay, following the release of the software update. Available in macOS 15 and later.
- `MinorPeriodInDays` (integer): Specifies the number of days to defer a minor OS software update on the device. It also defers major updates for iOS. When set, software updates only appear after the specified delay, following the release of the software update. Available in macOS 15 and later.
- `SystemPeriodInDays` (integer): Specifies the number of days to defer system or non-OS updates. When set, updates only appear after the specified delay, following the release of the update. Available in macOS 15 and later.

## See Also

- [object SoftwareUpdateSettingsAutomaticActionsObject](softwareupdatesettingsautomaticactionsobject.md)
  The object that configures various automatic Software Update functionality.
- [object SoftwareUpdateSettingsBetaObject](softwareupdatesettingsbetaobject.md)
  The object that configures overall beta program settings.
- [object SoftwareUpdateSettingsRapidSecurityResponseObject](softwareupdatesettingsrapidsecurityresponseobject.md)
  The object that configures Background Security Improvement settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdatesettingsdeferralsobject)*