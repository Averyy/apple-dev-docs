# SiriSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints on the device’s Siri settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct SiriSettings
```

## Topics

### Restricting Siri Usage
- [var denySiri: Bool?](sirisettings/denysiri-swift.property.md)
  A Boolean value that indicates whether to prevent access to Siri.
- [static let denySiri: SettingMetadata<Bool>](sirisettings/denysiri-swift.type.property.md)
  The metadata for the constraint that configures access to Siri.

## Relationships

### Conforms To
- [ManagedSettingsGroup](managedsettingsgroup.md)

## See Also

- [var account: AccountSettings](managedsettingsstore/account.md)
  Settings that affect accounts.
- [struct AccountSettings](accountsettings.md)
  An object that configures whether a user can modify their device’s account settings.
- [var cellular: CellularSettings](managedsettingsstore/cellular.md)
  Settings that affect cellular networking.
- [struct CellularSettings](cellularsettings.md)
  Constraints on the user’s cellular networking settings.
- [var dateAndTime: DateAndTimeSettings](managedsettingsstore/dateandtime.md)
  Settings that affect the date and time.
- [struct DateAndTimeSettings](dateandtimesettings.md)
  Constraints on the device’s date and time settings.
- [var passcode: PasscodeSettings](managedsettingsstore/passcode.md)
  Settings that affect the device passcode.
- [struct PasscodeSettings](passcodesettings.md)
  Constraints on a user’s ability to change their device’s passcode.
- [var shield: ShieldSettings](managedsettingsstore/shield.md)
  Settings that affect what activities the system covers with a shielding view on this device.
- [struct ShieldSettings](shieldsettings.md)
  Constraints that indicate what apps and websites to cover with a shielding view.
- [var siri: SiriSettings](managedsettingsstore/siri.md)
  Settings that affect Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/sirisettings)*