# Package

**Framework**: Device Management  
**Kind**: dictionary

The declaration to install a package.

**Availability**:
- macOS 26.0+

## Declaration

```swift
object Package
```

## Mentions

- [Installing packages](installing-packages.md)

#### Discussion

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

##### Configuration Example

This configuration installs a required package.

```json
{
    "Type": "com.apple.configuration.package",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ManifestURL": "https://example.com/files/packages/TestPackage.plist",
        "InstallBehavior": {
            "Install": "Required"
        }
    }
}
```

## Topics

### Objects
- [object PackageInstallBehaviorObject](packageinstallbehaviorobject.md)
  Specifies the install behavior of the package.

## Properties

- `InstallBehavior` (PackageInstallBehaviorObject): A dictionary that describes how and when to install the package.
- `ManifestURL` (string) *(required)*: The URL of the manifest document for the package that the device downloads. The manifest is returned as a [`ManifestURL`](manifesturl.md) property list. The `url` property of the manifest must point to the package (.pkg) file to install.

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
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/package)*