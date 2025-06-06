# AccountLDAP

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AccountLDAP
```

#### Discussion

Specify `com.apple.configuration.account.ldap` as the declaration type.

##### Configuration Availability

| Allowed in Device Enrollment | iOS, macOS |
| --- | --- |
| Allowed in User Enrollment | iOS, macOS |
| Allowed in Local Enrollment | iOS, macOS |
| Allowed in System Scope | iOS |
| Allowed in User Scope | macOS, Shared iPad |

## Topics

### Supporting Objects
- [object AccountLDAPSearchSettingsItemObject](accountldapsearchsettingsitemobject.md)
  The settings for configuring the search behavior with an LDAP server.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure an address book account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
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
- [object PasscodeSettings](passcodesettings.md)
  The declaration to configure passcode policy settings.
- [object SafariExtensionSettings](safariextensionsettings.md)
  The declaration to configure Safari Extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountldap)*