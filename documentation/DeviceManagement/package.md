# Package

**Framework**: Device Management  
**Kind**: dictionary

The declaration to install a package.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
object Package
```

#### Discussion

Specify `com.apple.configuration.package` as the declaration type.

Specify `com.apple.configuration.package` as the declaration type.

This declaration installs a package on a device. Packages can contain apps, fonts, documents, and other items. Apps that a package installs aren’t automatically managed; you can manage them using the [`AppManaged`](appmanaged.md) declaration.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | macOS |
| Allowed in user scope | NA |

## Topics

### Objects
- [object PackageInstallBehaviorObject](packageinstallbehaviorobject.md)
  Specifies the install behavior of the package.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/package)*