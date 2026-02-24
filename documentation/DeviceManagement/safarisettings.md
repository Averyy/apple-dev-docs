# SafariSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Safari settings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
object SafariSettings
```

#### Discussion

Specify `com.apple.configuration.safari.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |

##### Configuration Examples

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

## Topics

### Objects
- [object SafariSettingsNewTabStartPageObject](safarisettingsnewtabstartpageobject.md)
  Sets the start page for new tabs in Safari.

## Properties

- `AcceptCookies` (string): The policy Safari uses for managing cookies: - `Never`: Safari always blocks cookies.
- `CurrentWebsite`: Safari allows cookies only from the current website.
- `VisitedWebsites`: Safari allows cookies only from visited websites.
- `Always`: Safari always allows cookies.
- `AllowDisablingFraudWarning` (boolean): If `false`, the system forces fraud warnings on in Safari.
- `AllowHistoryClearing` (boolean): If `false`, the system disables clearing history in Safari.
- `AllowJavaScript` (boolean): If `false`, the system disables JavaScript in Safari.
- `AllowPopups` (boolean): If `false`, the system disables popups in Safari.
- `AllowPrivateBrowsing` (boolean): If `false`, the system disables private browsing in Safari.
- `AllowSummary` (boolean): If `false`, the system disables summarization of content in Safari.
- `NewTabStartPage` (SafariSettingsNewTabStartPageObject): Sets the start page for new tabs in Safari.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safarisettings)*