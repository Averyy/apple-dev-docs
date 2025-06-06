# ScreenSharingConnection

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a connection to a screen-sharing host.

**Availability**:
- macOS 14.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ScreenSharingConnection
```

#### Discussion

Specify `com.apple.configuration.screensharing.connection` as the declaration type.

##### Configuration Availability

| Allowed in Device Enrollment | macOS |
| --- | --- |
| Allowed in User Enrollment | macOS |
| Allowed in Local Enrollment | macOS |
| Allowed in System Scope | macOS |
| Allowed in User Scope | macOS |

## Topics

### Supporting Objects
- [object ScreenSharingConnectionDisplayConfigurationObject](screensharingconnectiondisplayconfigurationobject.md)
  The display configuration for this connection.
- [object ScreenSharingConnectionGroup](screensharingconnectiongroup.md)
  The declaration to configure a group of screen-sharing connections.
- [object ScreenSharingHostSettings](screensharinghostsettings.md)
  The declaration to configure screen-sharing host settings and restrictions.

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
- [object PasscodeSettings](passcodesettings.md)
  The declaration to configure passcode policy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensharingconnection)*