# LegacyInteractiveProfile

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure an interactive legacy profile.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+

## Declaration

```swift
object LegacyInteractiveProfile
```

#### Discussion

Specify `com.apple.configuration.legacy.interactive` as the declaration type.

This declaration specifies an MDMv1 profile to present to the user, who may choose to download and install the profile.

The profile may contain any payload type other than the following:

- `com.apple.mdm`
- `com.apple.declarations`

If a user enrollment triggers this configuration: in macOS the system silently ignores any MDMv1 payloads in macOS where the User Enrollment Mode setting is `forbidden`; in iOS, tvOS, watchOS and visionOS, the system rejects the entire profile if any MDMv1 payload has its User Enrollment Mode setting set to `forbidden`.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, tvOS, visionOS |
| Allowed in device enrollment | iOS, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, tvOS, visionOS |
| Allowed in user scope | macOS |
| Apply | Multiple configurations are applied separately |

##### Configuration Examples

**URL**:

Downloads the profile from a URL on the MDM server.

```json
{
    "Type": "com.apple.configuration.legacy.interactive",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ProfileURL": "https://www.example.com/profiles/passcode.mobileconfig",
        "VisibleName": "Passcode Policy"
    }
}
```

**Asset**:

Downloads the profile using an asset.

```json
{
    "Type": "com.apple.configuration.legacy.interactive",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ProfileAssetReference": "F8D5BF80-F38A-476A-BEE0-0B10BDED2161",
        "VisibleName": "Passcode Policy"
    }
}
```

## Properties

- `ProfileAssetReference` (string): The identifier of an asset declaration containing a reference to the profile data. The corresponding asset needs to be of type `com.apple.asset.data`. The referenced data needs to be a property list file, and the asset’s “ContentType” value set to match the data type. One of `ProfileURL` or `ProfileAssetReference` needs to be present. Available: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+ | visionOS 27+
- `ProfileURL` (string): The URL of the profile to download and install, which needs to start with `https://`. The request uses MDM semantics, which includes the device-identity certificate, and any user authentication. This is equivalent to an MDM request made to the `CheckInURL` or `ServerURL`. One of `ProfileURL` or `ProfileAssetReference` needs to be present.
- `VisibleName` (string) *(required)*: The visible name of the configuration. This name needs to indicate the nature of the profile.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/legacyinteractiveprofile)*