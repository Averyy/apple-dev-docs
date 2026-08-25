# LegacyProfile

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a legacy profile.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object LegacyProfile
```

#### Discussion

Specify `com.apple.configuration.legacy` as the declaration type.

This declaration specifies an MDMv1 profile for the device to download and install.

The profile may contain any payload type other than the following:

- `com.apple.mdm`
- `com.apple.declarations`

If a user enrollment triggers this configuration: in macOS the system silently ignores any MDMv1 payloads in macOS where the User Enrollment Mode setting is `forbidden`; in iOS, tvOS, watchOS and visionOS, the system rejects the entire profile if any MDMv1 payload has its User Enrollment Mode setting set to `forbidden`.

##### Transition Profiles From Mdm

A declarative device management (DDM) legacy profile can take control of profiles installed via MDM. This avoids the need to first remove the MDM profile, before installing the DDM equivalent. DDM cannot take over control of non-MDM-installed profiles.

The rules for transitioning profiles are:

1. An existing MDM-installed profile is present (installed by MDM using the [`Install Profile`](install-profile-command.md)).
2. DDM is enabled on the device.
3. The server sends a legacy profile configuration to the device and ensures it is “activated”. 1. The DDM profile that the configuration applies needs to conform to the following requirements: 1. The DDM profile’s `PayloadIdentifier` and `PayloadUUID` need to match that of the MDM profile.
2. The DDM profile needs to have the same number of payloads as the MDM profile.
3. The DDM profile payloads needs to have the same `PayloadType`, `PayloadIdentifier`, and `PayloadUUID`, in the same order as the profile payloads in the MDM profile.
2. If the DDM profile doesn’t conform to the above requirements, the configuration isn’t applied and its `valid` status is set to `invalid`.
3. The [`Profile List`](profile-list-command.md) can be used to determine the “structure” of existing MDM profiles to satisfy the above requirements.

When DDM takes control of the MDM profile, the following occurs:

1. The system doesn’t reinstall the profile. Instead, the MDM profile’s existing system state remains unchanged. Thus system state won’t include any differences between the MDM and DDM profiles (other than the structural items outlined above that must match).
2. Any attempt to install, update, or remove the profile using MDM commands fails (using the usual identifier and UUID matching rules). This holds true while the DDM profile is active.
3. Updates to the DDM configuration result in the system reapplying the profile which updates the system state with any new or changed settings.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| Allowed in user scope | macOS, Shared iPad |
| Apply | Multiple configurations are applied separately |

##### Configuration Examples

**URL**:

Downloads the profile from a URL on the MDM server.

```json
{
    "Type": "com.apple.configuration.legacy",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ProfileURL": "https://www.example.com/profiles/passcode.mobileconfig"
    }
}
```

**Asset**:

Downloads the profile using an asset.

```json
{
    "Type": "com.apple.configuration.legacy",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ProfileAssetReference": "F8D5BF80-F38A-476A-BEE0-0B10BDED2161"
    }
}
```

## Properties

- `ProfileAssetReference` (string): The identifier of an asset declaration containing a reference to the profile data. The corresponding asset needs to be of type `com.apple.asset.data`. The referenced data needs to be a property list file, and the asset’s “ContentType” value set to match the data type. One of `ProfileURL` or `ProfileAssetReference` needs to be present. Available: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+ | visionOS 27+ | watchOS 27+
- `ProfileURL` (string): The URL of the profile to download and install, which needs to start with `https://`. The request uses MDM semantics, which includes the device-identity certificate, and any user authentication. This is equivalent to an MDM request made to the `CheckInURL` or `ServerURL`. One of `ProfileURL` or `ProfileAssetReference` needs to be present.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/legacyprofile)*