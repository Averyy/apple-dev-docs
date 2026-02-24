# WatchEnrollment

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure an MDMv1 profile for Apple Watch enrollment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
object WatchEnrollment
```

#### Discussion

Specify `com.apple.configuration.watch.enrollment` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS |
| Allowed in user scope | NA |

##### Configuration Example

```json
{
    "Type": "com.apple.configuration.watch.enrollment",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "EnrollmentProfileURL": "https://example.com/enroll/watch",
        "AnchorCertificateAssetReferences": [
            "91D3512C-5E44-4C6F-97A5-59A8F731641D"
        ]
    }
}
```

## Properties

- `AnchorCertificateAssetReferences` ([string]): An array of identifiers of asset declarations that contain anchor certificates to use to evaluate the trust of the enrollment profile server. Set the type of the corresponding assets to `com.apple.asset.credential.certificate`. These certificates are pinned, meaning that the server specified by the `EnrollmentProfileURL` must use a certificate that chains to one of the certs in this array. If it chains to one of the built-in trusted root certificates but not one of the `AnchorCertificateAssetReferences` certs, the connection will fail.
- `EnrollmentProfileURL` (string) *(required)*: The URL of the profile that the Apple Watch downloads and installs if the user opts in to management during the pairing process, which needs to start with `https://`. Successful enrollment requires that the pairing iPhone is supervised and the profile contains an MDM payload. Apple Watch attempts to install each payload that the profile contains.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/watchenrollment)*