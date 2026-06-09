# AppManaged

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a managed app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
object AppManaged
```

## Mentions

- [Configuring managed apps and extensions](configuring-managed-apps-and-extensions.md)
- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)
- [Transferring management of apps to declarative management](transferring-management-of-apps-to-declarative-management.md)
- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)
- [Installing packages](installing-packages.md)
- [Migrating managed devices](migrating-managed-devices.md)

#### Discussion

Specify `com.apple.configuration.app.managed` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, Shared iPad, visionOS |
| Allowed in user scope | macOS |
| Apply | Multiple configurations are applied separately |

##### Configuration Examples

**App Store**:

This configuration installs an App Store app with `Required` install behavior and a device license.

```json
{
    "Type": "com.apple.configuration.app.managed",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "AppStoreID": "361285480",
        "InstallBehavior": {
            "Install": "Required",
            "License": {
                "Assignment": "Device"
            }
        }
    }
}
```

**Enterprise**:

This configuration installs an enterprise app with app attributes, cellular downloads disallowed, and an update policy.

```json
{
    "Type": "com.apple.configuration.app.managed",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ManifestURL": "https://example.com/apps/TestApp.plist",
        "InstallBehavior": {
            "Install": "Required",
            "AllowDownloadsOverCellular": "AlwaysOff"
        },
        "UpdateBehavior": {
            "AutomaticAppUpdates": "AlwaysOn"
        },
        "Attributes": {
            "AssociatedDomains": [
                "www.example.com"
            ],
            "AssociatedDomainsEnableDirectDownloads": true,
            "CellularSliceUUID": "Cellular-12345",
            "ContentFilterUUID": "ContentFilter-12345",
            "DNSProxyUUID": "DNSProxy-12345",
            "Hideable": false,
            "Lockable": false,
            "RelayUUID": "Relay-12345",
            "TapToPayScreenLock": true,
            "VPNUUID": "VPN-12345"
        }
    }
}
```

**Packaged**:

This configuration manages an app installed by a package using a composed identifier to identify the app.

```json
{
    "Type": "com.apple.configuration.app.managed",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "AppComposedIdentifier": "com.example.TestApp (ABCDE12345)",
        "InstallBehavior": {
            "Install": "Required"
        }
    }
}
```

**Configuration**:

This configuration installs an enterprise app with declarative app configuration for the app and an extension.

```json
{
    "Type": "com.apple.configuration.app.managed",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ManifestURL": "https://example.com/apps/TestApp.plist",
        "InstallBehavior": {
            "Install": "Required",
            "AllowDownloadsOverCellular": "AlwaysOff"
        },
        "UpdateBehavior": {
            "AutomaticAppUpdates": "AlwaysOn"
        },
        "AppConfig": {
            "DataAssetReference": "52C7D562-1DEC-472A-BFDF-3A8BE630385B",
            "Certificates": [
                {
                    "Identifier": "Certificate1",
                    "AssetReference": "84965BAD-11B2-48CE-9766-CE32387C508E"
                }
            ]
        },
        "ExtensionConfigs": {
            "com.example.TestApp.extension1 (ABCDE12345)": {
                "DataAssetReference": "52C7D562-1DEC-472A-BFDF-3A8BE630385B",
                "Certificates": [
                    {
                        "Identifier": "Certificate1",
                        "AssetReference": "84965BAD-11B2-48CE-9766-CE32387C508E"
                    },
                    {
                        "Identifier": "Certificate2",
                        "AssetReference": "4CEF7D59-CDB5-477A-B51B-6A1E8A63D678"
                    }
                ]
            }
        }
    }
}
```

## Topics

### Objects
- [object AppManagedAppConfigDictionaryObject](appmanagedappconfigdictionaryobject.md)
  A dictionary of app config data and credentials.
- [object AppManagedAttributesObject](appmanagedattributesobject.md)
  A dictionary of values to associate with the app.
- [object AppManagedExtensionConfigsObject](appmanagedextensionconfigsobject.md)
  A dictionary of extension config data and credentials.
- [object AppManagedInstallBehaviorObject](appmanagedinstallbehaviorobject.md)
  A dictionary that describes how and when to install the app.
- [object AppManagedUpdateBehaviorObject](appmanagedupdatebehaviorobject.md)
  A dictionary that specifies how the device updates apps.

## Properties

- `AppComposedIdentifier` (string): A string that specifies the composed identifier of an existing app that needs to be managed. The device uses this to take over management of an app installed by some other process, for example installed manually by the user, or via a package configuration. If the app isn’t present when the device applies the configuration, the device takes over management of it when it does install. Management of the app occurs only if its code signature matches the composed identifier. The following rules apply when the device takes over management: - If the `InstallBehavior.Install` key is set to `Required`, the device takes over management of the app.
- If the `InstallBehavior.Install` key is set to `Optional`, the device takes over management of the app when the user “installs” it using an MDM management app. The format of the composed identifier is either “Bundle-ID” or “Bundle-ID (Team-ID)”. “Bundle-ID” is the bundle identifier string of the provider. “Team-ID” is the team identifier from the provider’s code signature. For example, “com.example.app” for the bundle ID format, or “com.example.app (ABCD1234)” for the team ID format. In macOS, only one of `AppStoreID`, `BundleID`, or `AppComposedIdentifier` needs to be present. Available: macOS 26+
- `AppConfig` (AppManagedAppConfigDictionaryObject): A dictionary of app config data and credentials. Available: iOS 18.4+ | iPadOS 18.4+ | macOS 27+ | visionOS 2.4+
- `AppStoreID` (string): The App Store ID of the managed app that is downloaded from the App Store. Only one of `AppStoreID`, `BundleID`, `ManifestURL`, or `AppComposedIdentifier` needs to be present.
- `Attributes` (AppManagedAttributesObject): A dictionary of values to associate with the app. Available: iOS 17.2+ | iPadOS 17.2+ | visionOS 2.4+
- `BundleID` (string): The bundle ID of the managed app that is downloaded from the App Store. Only one of `AppStoreID`, `BundleID`, `ManifestURL`, or `AppComposedIdentifier` needs to be present.
- `ExtensionConfigs` (AppManagedExtensionConfigsObject): A dictionary of extension config data and credentials. Available: iOS 18.4+ | iPadOS 18.4+ | macOS 27+ | visionOS 2.4+
- `IncludeInBackup` (boolean): If `true`, backups contain the app and its data. Available: iOS 17.2+ | iPadOS 17.2+ | visionOS 2.4+
- `InstallBehavior` (AppManagedInstallBehaviorObject): A dictionary that describes how and when to install the app.
- `iOSApp` (boolean): If `true`, the device installs an iOS or iPadOS app that runs on a Mac with Apple silicon. This is only used when the app is an App Store app. Available: macOS 26+
- `LegacyAppConfigAssetReference` (string): The identifier of an asset declaration containing a reference to the app config data. The device provides the app config data to the app using the MDMv1 behavior. The corresponding asset needs to be of type `com.apple.asset.data`. The referenced data needs to be a property list file, and the asset’s “ContentType” value set to match the data type. Available: iOS 18.4+ | iPadOS 18.4+ | macOS 27+ | visionOS 2.4+
- `ManifestURL` (string): The URL of the manifest for the managed app that the device downloads from a web site. The manifest is a [`ManifestURL`](manifesturl.md) property list. Only one of `AppStoreID`, `BundleID`, `ManifestURL`, or `AppComposedIdentifier` needs to be present. Available: iOS 17.2+ | iPadOS 17.2+ | visionOS 2.4+
- `UpdateBehavior` (AppManagedUpdateBehaviorObject): A dictionary that specifies how the device updates apps. Available: iOS 26+ | iPadOS 26+ | macOS 26+ | visionOS 26+

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
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appmanaged)*