# SoftwareUpdateEnforcementSpecific

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a software update enforcement policy for a specific OS release.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 26.0+

## Declaration

```swift
object SoftwareUpdateEnforcementSpecific
```

## Mentions

- [Deploy software updates using declarative management](deploy-software-updates-using-declarative-management.md)
- [Phases of software update enforcement](phases-of-software-update-enforcement.md)

#### Discussion

Specify `com.apple.configuration.softwareupdate.enforcement.specific` as the declaration type.

If the `TargetOSVersion` and optional `TargetBuildVersion` values don’t match an available software update, the device keeps the configuration active, but won’t be able to update. If a software update that matches these keys becomes available later, the device will process the update.

To determine available software updates to show to an admin, a device management service uses the Apple GDMF service via `https://gdmf.apple.com/v2/pmv`. Configurations only enforce a software update if GDMF has the corresponding OS version or build available. So device management services need to regularly check available versions, and adjust the list shown to admins, and also remove any deployed configurations that use OS versions or builds that are no longer available. Device management services should check GDMF no more than once a day.

The system installs the specific version set in the `TargetOSVersion`, and it won’t install a patch version if only a minor version is set.

The system can only install a supplemental software update on a device that already has the base OS version installed. For example, the system can only install a `16.1`(a) update on a device that currently has `16.1` installed, but it can’t install that update on a device that has only `16.0` installed. To update to a supplemental version from an older base version, use two configurations. Use the first configuration to update to the new base version, and the second configuration to update the new base version to its supplemental version.

If the device isn’t running at the target date-time, the system enforces the software update 1 hour after restarting, or when the device meets all required conditions, such as minimum battery level.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are applied separately |

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

## Properties

- `DetailsURL` (string): The URL of a web page that shows details that the organization provides about the enforced software update.
- `TargetBuildVersion` (string): The target build version to update the device to by the appropriate time, for example, `20A242`. Use the build version for testing during seeding periods. The build version can include a supplemental version identifier, for example, `20A242a`.
- `TargetLocalDateTime` (string) *(required)*: The local date time value that specifies when to force install the software update. Use the format `yyyy-mm-ddThh:mm:ss`, which is derived from RFC 3339 but doesn’t include a time zone offset or fractional seconds. If the user doesn’t trigger the software update before this time, the device force installs it.
- `TargetOSVersion` (string) *(required)*: The target OS version to update the device to by the appropriate time. This is the OS version number, for example, `16.1`.

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
- [object AppSettings](appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object ContentCaching](contentcaching.md)
  The declaration to configure the Content Caching service.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/softwareupdateenforcementspecific)*