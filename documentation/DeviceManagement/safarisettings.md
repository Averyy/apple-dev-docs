# SafariSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Safari settings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
object SafariSettings
```

#### Discussion

Specify `com.apple.configuration.safari.settings` as the declaration type.

##### Privacy Permission Defaults

Privacy permission defaults allow an organization to suggest a set of privacy permissions for use on a website. When set, Safari displays a consent prompt listing all the configured defaults. If the user accepts, the system applies those defaults for the website. If the user declines, no defaults are set and Safari prompts the user in the normal way when the website requires permission.

The consent prompt only shows permissions that the user hasn’t previously seen, and won’t appear if the user has seen all permissions. The user can choose from one of two options in the prompt:

- `Allow`: this option sets the website privacy permissions for the specified sub-systems (camera or microphone) to “Allow”. Safari doesn’t prompt the user when the website uses the sub-system.
- `Not Now`: this option ignores the website privacy permission defaults for the specified sub-systems (camera or microphone). Safari prompts the user in the normal way when the website uses the sub-system.

The user can change the website privacy permission settings in Safari settings if they choose.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Examples

###### Settings and Restrictions Examples

**Start page**:

This configuration sets the Safari start page to show a specific website.

```json
{
    "Type": "com.apple.configuration.safari.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "NewTabStartPage": {
            "PageType": "Home",
            "HomepageURL": "https://www.example.com"
        }
    }
}
```

**Restrictions**:

This configuration restricts several Safari features.

```json
{
    "Type": "com.apple.configuration.safari.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "AcceptCookies": "Never",
        "AllowDisablingFraudWarning": false,
        "AllowHistoryClearing": false,
        "AllowJavaScript": false,
        "AllowPrivateBrowsing": false,
        "AllowPopups": false,
        "AllowSummary": false
    }
}
```

###### Website Privacy Examples

**One website**:

This configuration sets the camera permission default in Safari for one specific website.

```json
{
    "Type": "com.apple.configuration.safari.settings",
    "Identifier": "B5C63FC4-3D53-4705-AC70-9F03C178A7B4",
    "ServerToken": "40E91AFE-464D-4DA1-842F-3838CEE7597C",
    "Payload": {
        "Privacy": {
            "PermissionDefaults": {
                "example.com": {
                    "OrganizationJustification": "The camera is required to scan your QR code for authentication.",
                    "Camera": "Allow"
                }
            }
        }
    }
}
```

**One website and its children**:

This configuration sets the camera and microphone permission defaults in Safari for a specific website and its child websites.

```json
{
    "Type": "com.apple.configuration.safari.settings",
    "Identifier": "614B7CD6-2E0B-4BFE-812F-E4E6277C9624",
    "ServerToken": "19B9F819-D65F-4805-9D12-CC264C19D191",
    "Payload": {
        "Privacy": {
            "PermissionDefaults": {
                "*example.com": {
                    "OrganizationJustification": "The camera and microphone are required for video conferencing.",
                    "Camera": "Allow",
                    "Microphone": "Allow"
                }
            }
        }
    }
}
```

## Topics

### Objects
- [object SafariSettingsNewTabStartPageObject](safarisettingsnewtabstartpageobject.md)
  Sets the start page for new tabs in Safari.
- [object SafariSettingsPrivacyObject](safarisettingsprivacyobject.md)
  The dictionary of website privacy settings.

## Properties

- `AcceptCookies` (string): The policy Safari uses for managing cookies: - `Never`: Safari always blocks cookies.
- `CurrentWebsite`: Safari allows cookies only from the current website.
- `VisitedWebsites`: Safari allows cookies only from visited websites.
- `Always`: Safari always allows cookies. Available: iOS 26+ | iPadOS 26+
Allowed enrollments: supervised
- `AllowDisablingFraudWarning` (boolean): If `false`, the system forces fraud warnings on in Safari. Available: iOS 26+ | iPadOS 26+
Allowed enrollments: supervised
- `AllowHistoryClearing` (boolean): If `false`, the system disables clearing history in Safari. Allowed enrollments: supervised
- `AllowJavaScript` (boolean): If `false`, the system disables JavaScript in Safari. Available: iOS 26+ | iPadOS 26+
Allowed enrollments: supervised
- `AllowPopups` (boolean): If `false`, the system disables popups in Safari. Available: iOS 26+ | iPadOS 26+
Allowed enrollments: supervised
- `AllowPrivateBrowsing` (boolean): If `false`, the system disables private browsing in Safari. Allowed enrollments: supervised
- `AllowSummary` (boolean): If `false`, the system disables summarization of content in Safari. Allowed enrollments: supervised
- `NewTabStartPage` (SafariSettingsNewTabStartPageObject): Sets the start page for new tabs in Safari.
- `Privacy` (SafariSettingsPrivacyObject): The dictionary of website privacy settings. Available: iOS 27+ | iPadOS 27+ | macOS 27+
Allowed enrollments: supervised

## See Also

- [object AccessibilitySettings](accessibilitysettings.md)
  The declaration to configure accessibility settings.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safarisettings)*