# AudioAccessorySettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure audio accessory settings.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
object AudioAccessorySettings
```

#### Discussion

Specify `com.apple.configuration.audio-accessory.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, Shared iPad |
| Allowed in user scope | NA |

## Topics

### Objects
- [object AudioAccessorySettingsTemporaryPairingObject](audioaccessorysettingstemporarypairingobject.md)
  A dictionary that describes audio accessory temporary pairing behavior. The device enables temporary pairing when this key is present and the `Disabled` key isn’t `false`. The device doesn’t synchronize pairing information with iCloud when temporary pairing is active.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure an address book account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a Calendar subscription.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive, legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to test the MDM system.
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.
- [object Package](package.md)
  The declaration to install a package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/audioaccessorysettings)*