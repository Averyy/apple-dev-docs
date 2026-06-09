# AppSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure app settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object AppSettings
```

#### Discussion

Specify `com.apple.configuration.app.settings` as the declaration type.

##### Binary Identifier Rules

The following combinations of binary identifiers are supported for each key:

- `AllowedBinaries`: - Either `CDHash` or `TeamID` needs to be present.
- `SigningID`, `PathPrefix`, or `SigningState` may be present.
- `DeniedBinaries` - Either `CDHash` or `TeamID` or `SigningID` needs to be present.
- `PathPrefix` or `SigningState` may be present.

##### Privacy Permission Defaults

Privacy permission defaults allow an organization to suggest a set of privacy permissions for use with an app. When set, the app displays a consent prompt listing all the configured defaults. If the user accepts, the device applies those defaults for the app. If the user declines, no defaults are set and the device prompts the user in the normal way when the app requires permission.

The consent prompt only shows permissions that the user hasn’t previously seen, and won’t appear if the user has seen all permissions. The user can choose from one of two options in the prompt:

- `Allow`: this option sets the app privacy permissions for the specified sub-systems (camera, microphone, and so on) to “Allow”. The device doesn’t prompt the user when the app uses the sub-system.
- `Not Now`: this option ignores the app privacy permission defaults for the specified sub-systems (camera, microphone, and so on). The device prompts the user in the normal way when the app uses the sub-system.

The user can change the app permission privacy settings in Settings.app if they choose.

Only AppKit-based apps on macOS support this feature.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, tvOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Examples

**Allow various permission defaults for several apps in iOS**:

This configuration sets various privacy permission defaults for several apps.

```json
{
    "Type": "com.apple.configuration.app.settings",
    "Identifier": "AF389B6F-5784-4DB6-BEFF-EA6D689BD4B0",
    "ServerToken": "A5CA3371-559E-44B4-B9ED-A0A7DFEC193A",
    "Payload": {
        "Privacy": {
            "PermissionDefaults": {
                "com.example.scanner": {
                    "OrganizationJustification": "This app is used for scanning work documents.",
                    "Camera": "Allow"
                },
                "com.example.on-site": {
                    "OrganizationJustification": "This app is used for video conferences while on-site with customers.",
                    "Camera": "Allow",
                    "Microphone": "Allow",
                    "Location": "WhileUsing",
                    "LocationAccuracy": "Precise"
                }
            }
        }
    }
}
```

**Allow various permission defaults for several apps in macOS**:

This configuration sets various privacy permission defaults for several apps.

```json
{
    "Type": "com.apple.configuration.app.settings",
    "Identifier": "245E4CBC-021B-4DB0-9B30-25F581119A2A",
    "ServerToken": "D6472788-7568-4268-99CE-AD8AE114B28C",
    "Payload": {
        "Privacy": {
            "PermissionDefaults": {
                "com.example.scanner (ABCD1234)": {
                    "OrganizationJustification": "This app is used for scanning work documents.",
                    "Camera": "Allow"
                },
                "com.example.on-site {anchor apple generic}": {
                    "OrganizationJustification": "This app is used for video conferences while on-site with customers.",
                    "Camera": "Allow",
                    "Microphone": "Allow",
                    "Location": "WhileUsing",
                    "LocationAccuracy": "Precise"
                }
            }
        }
    }
}
```

## Topics

### Objects
- [object AppSettingsAllowedObject](appsettingsallowedobject.md)
  The dictionary of allowed app settings.
- [object AppSettingsPrivacyObject](appsettingsprivacyobject.md)
  The dictionary of app settings.

## Properties

- `Allowed` (AppSettingsAllowedObject): The dictionary of allowed app settings.
- `Privacy` (AppSettingsPrivacyObject): The dictionary of app settings. Available: iOS 27+ | iPadOS 27+ | macOS 27+
Allowed scopes: iOS: system | macOS: user

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appsettings)*