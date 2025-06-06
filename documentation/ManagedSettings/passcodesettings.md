# PasscodeSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints on a user’s ability to change their device’s passcode.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct PasscodeSettings
```

## Topics

### Blocking Passcode Changes
- [var lockPasscode: Bool?](passcodesettings/lockpasscode-swift.property.md)
  A Boolean value that indicates whether to prevent changing the device passcode.
- [static let lockPasscode: SettingMetadata<Bool>](passcodesettings/lockpasscode-swift.type.property.md)
  The metadata for the setting that prevents the user from changing their passcode.

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
- [var shield: ShieldSettings](managedsettingsstore/shield.md)
  Settings that affect what activities the system covers with a shielding view on this device.
- [struct ShieldSettings](shieldsettings.md)
  Constraints that indicate what apps and websites to cover with a shielding view.
- [var siri: SiriSettings](managedsettingsstore/siri.md)
  Settings that affect Siri.
- [struct SiriSettings](sirisettings.md)
  Constraints on the device’s Siri settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/passcodesettings)*