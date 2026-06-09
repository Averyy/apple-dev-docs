# Package

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a package.

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
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are applied separately |

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
  A dictionary that describes how and when to install the package.
- [object PackageUninstallBehaviorObject](packageuninstallbehaviorobject.md)
  A dictionary that describes how to uninstall the package.

## Properties

- `InstallBehavior` (PackageInstallBehaviorObject): A dictionary that describes how and when to install the package.
- `ManifestURL` (string) *(required)*: The URL of the manifest document for the package that the device downloads. The manifest is returned as a [`ManifestURL`](manifesturl.md) property list. The `url` property of the manifest must point to the package (.pkg) file to install.
- `UninstallBehavior` (PackageUninstallBehaviorObject): A dictionary that describes how to uninstall the package. Available: macOS 27+

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/package)*