# SafariBookmarks

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure managed bookmarks in Safari.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
object SafariBookmarks
```

#### Discussion

Specify `com.apple.configuration.safari.bookmarks` as the declaration type.

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

##### Configuration Example

This configuration applies a set of managed bookmarks: two bookmarks and one bookmarks folder, which contains two more bookmarks.

```json
{
    "Type": "com.apple.configuration.safari.bookmarks",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ManagedBookmarks": [
            {
                "GroupIdentifier": "Group1",
                "Title": "Company Bookmarks",
                "Bookmarks": [
                    {
                        "Title": "Public Site",
                        "URL": "https://www.example.com"
                    },
                    {
                        "Title": "Store",
                        "URL": "https://store.example.com"
                    },
                    {
                        "Title": "Internal Developers",
                        "Folder": [
                            {
                                "Title": "Developers",
                                "URL": "https://developer.example.com"
                            },
                            {
                                "Title": "Repositories",
                                "URL": "https://repo.example.com"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

## Topics

### Objects
- [object SafariBookmarksBookmarkGroupObject](safaribookmarksbookmarkgroupobject.md)
  A group of managed bookmarks.

## Properties

- `ManagedBookmarks` ([SafariBookmarksBookmarkGroupObject]): A dictionary that specifies a set of managed bookmarks.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safaribookmarks)*