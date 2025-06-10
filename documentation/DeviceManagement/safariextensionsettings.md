# SafariExtensionSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Safari Extensions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 26.0+ (Beta)

## Declaration

```swift
object SafariExtensionSettings
```

#### Discussion

Specify `com.apple.configuration.safari.extensions.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |

## Topics

### Objects
- [object SafariExtensionSettingsManagedExtensionsObject](safariextensionsettingsmanagedextensionsobject.md)
  The dictionary that defines the managed extension.

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
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safariextensionsettings)*