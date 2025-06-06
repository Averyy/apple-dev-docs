# CellularSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints on the user’s cellular networking settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct CellularSettings
```

#### Overview

Use `CellularSettings` to constrain the user’s ability to modify cellular settings in the Settings app.

## Topics

### Locking App Access to Cell Data
- [var lockAppCellularData: Bool?](cellularsettings/lockappcellulardata-swift.property.md)
  A Boolean value that indicates whether to prevent the user from changing cellular data settings.
- [static let lockAppCellularData: SettingMetadata<Bool>](cellularsettings/lockappcellulardata-swift.type.property.md)
  The metadata associated with the constraint that locks the cellular data setting.
### Locking the Device’s Cell Plan
- [var lockCellularPlan: Bool?](cellularsettings/lockcellularplan-swift.property.md)
  A Boolean value that indicates whether to prevent the user from changing their cellular plan.
- [static let lockCellularPlan: SettingMetadata<Bool>](cellularsettings/lockcellularplan-swift.type.property.md)
  The metadata associated with the constraint that locks the user’s cellular plan.
### Locking the Device’s eSIM Settings
- [var lockESIM: Bool?](cellularsettings/lockesim-swift.property.md)
  A Boolean value that indicates whether to prevent the user from changing their eSIM settings.
- [static let lockESIM: SettingMetadata<Bool>](cellularsettings/lockesim-swift.type.property.md)
  The metadata associated with the constraint that locks the user’s eSIM settings.

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
- [struct SiriSettings](sirisettings.md)
  Constraints on the device’s Siri settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/cellularsettings)*