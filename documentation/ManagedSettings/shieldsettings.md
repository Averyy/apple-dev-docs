# ShieldSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints that indicate what apps and websites to cover with a shielding view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct ShieldSettings
```

## Topics

### Blocking Apps and Websites
- [var applications: Set<ApplicationToken>?](shieldsettings/applications-swift.property.md)
  Applications for the system to cover with a shielding view.
- [static let applications: SettingMetadata<Set<ApplicationToken>>](shieldsettings/applications-swift.type.property.md)
  The metadata for the configuration that specifies apps for the system to cover with a shielding view.
- [var webDomains: Set<WebDomainToken>?](shieldsettings/webdomains-swift.property.md)
  Websites for the system to cover with a shielding view.
- [static let webDomains: SettingMetadata<Set<WebDomainToken>>](shieldsettings/webdomains-swift.type.property.md)
  The metadata for the configuration that specifies websites for the system to shield.
### Blocking Categories of Apps and Websites
- [ShieldSettings.ActivityCategoryPolicy](shieldsettings/activitycategorypolicy.md)
  Policies available for shielding activities based on their category.
- [var applicationCategories: ShieldSettings.ActivityCategoryPolicy<Application>?](shieldsettings/applicationcategories-swift.property.md)
  Categories of apps for the system to cover with a shielding view.
- [static let applicationCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<Application>>](shieldsettings/applicationcategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of apps for the system to cover with a shielding view.
- [var webDomainCategories: ShieldSettings.ActivityCategoryPolicy<WebDomain>?](shieldsettings/webdomaincategories-swift.property.md)
  Categories of websites for the system to cover with a shielding view.
- [static let webDomainCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<WebDomain>>](shieldsettings/webdomaincategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of websites for the system to shield.

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
- [var siri: SiriSettings](managedsettingsstore/siri.md)
  Settings that affect Siri.
- [struct SiriSettings](sirisettings.md)
  Constraints on the device’s Siri settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings)*