# MathSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure the math and calculator apps.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
object MathSettings
```

#### Discussion

Specify `com.apple.configuration.math.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS |
| Allowed in user scope | macOS, Shared iPad |

##### Configuration Example

This configuration prevents the use of scientific and programmer modes in calculator app.

```json
{
    "Type": "com.apple.configuration.math.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Calculator": {
            "ScientificMode": {
                "Enabled": false
            },
            "ProgrammerMode": {
                "Enabled": false
            }
        }
    }
}
```

## Topics

### Objects
- [object MathSettingsCalculatorObject](mathsettingscalculatorobject.md)
  The declaration to configure the calculator app.
- [object MathSettingsSystemBehaviorObject](mathsettingssystembehaviorobject.md)
  The declaration to configure math behavior at the system level.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to test declarative device management.
- [object Package](package.md)
  The declaration to install a package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettings)*