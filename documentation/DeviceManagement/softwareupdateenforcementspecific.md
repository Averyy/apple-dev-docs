# SoftwareUpdateEnforcementSpecific

**Framework**: Device Management  
**Kind**: dictionary

A software update enforcement policy for a specific OS release.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object SoftwareUpdateEnforcementSpecific
```

#### Discussion

Specify `com.apple.configuration.softwareupdate.enforcement.specific` as the declaration type.

If the `TargetOSVersion` and optional `TargetBuildVersion` values don’t match an available software update, the device keeps the configuration active, but won’t be able to update. If a software update that matches these keys becomes available later, the device will process the update.

To determine available software updates to show to an admin, a device management service uses the Apple GDMF service via `https://gdmf.apple.com/v2/pmv`. Configurations only enforce a software update if GDMF has the corresponding OS version or build available. So device management services need to regularly check available versions, and adjust the list shown to admins, and also remove any deployed configurations that use OS versions or builds that are no longer available. Device management services should check GDMF no more than once a day.

If the `TargetOSVersion` is an OS version that includes both a minor and patch version, the system installs that specific version, for example, `16.1.1`. If the minor version doesn’t include a patch version, the system installs the latest available patch version. For example, if the `TargetOSVersion` is `16.1` and a `.1` patch is available, the system installs `16.1.1`.

The system can only install a supplemental software update on a device that already has the base OS version installed. For example, the system can only install a `16.1`(a) update on a device that currently has `16.1` installed, but it can’t install that update on a device that has only `16.0` installed. To update to a supplemental version from an older base version, use two configurations. Use the first configuration to update to the new base version, and the second configuration to update the new base version to its supplemental version.

If the device isn’t running at the target date-time, the system enforces the software update 1 hour after restarting, or when the device meets all required conditions, such as minimum battery level.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | NA |

##### Configuration Example

This configuration enforces a software update to a specific OS version and build at a specified time.

```json
{
    "Type": "com.apple.configuration.softwareupdate.enforcement.specific",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "TargetOSVersion": "26.0",
        "TargetBuildVersion": "23A309",
        "TargetLocalDateTime": "2025-09-21T01:00:00"
    }
}
```

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
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdateenforcementspecific)*