# SoftwareUpdateEnforcementSpecific

**Framework**: Device Management  
**Kind**: dictionary

A software update enforcement policy for a specific OS release.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 18.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SoftwareUpdateEnforcementSpecific
```

#### Discussion

Specify `com.apple.configuration.softwareupdate.enforcement.specific` as the declaration type.

If the `TargetVersion` is an OS version that includes both a minor and patch version, then the system installs that specific version, for example, `16.1.1`. If the minor version doesn’t include a patch version, the system installs the latest available patch version. For example, if the `TargetVersion` is `16.1` and a `.1` patch is available, the system installs `16.1.1`.

The system can only install a supplemental software update on a device that already has the base OS version installed. For example, the system can only install a `16.1`(a) update on a device that currently has `16.1` installed, but it can’t install that update on a device that only has `16.0` installed. To update to a supplemental version from an older base version, use two configurations. Use the first configuration to update to the new base version, and the second configuration to update the new base version to its supplemental version.

If the device isn’t running at the target date-time, the system enforces the update one hour after restarting, or when the device meets all required conditions, such as minimum battery level.

##### Configuration Availability

| Allowed in Device Enrollment | iOS, macOS |
| --- | --- |
| Allowed in User Enrollment | - |
| Allowed in Local Enrollment | - |
| Allowed in System Scope | iOS, macOS, Shared iPad |
| Allowed in User Scope | - |

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdateenforcementspecific)*