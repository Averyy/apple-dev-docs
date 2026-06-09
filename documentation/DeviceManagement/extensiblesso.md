# ExtensibleSSO

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Extensible Single Sign-On.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object ExtensibleSSO
```

#### Discussion

Specify `com.apple.configuration.extensible-sso` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |
| Apply | Multiple configurations are applied separately |

##### Configuration Examples

**Credential**:

This configuration sets up a Credential-type SSO extension that handles authentication for hosts in the example.com domain.

```json
{
    "Type": "com.apple.configuration.extensible-sso",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ExtensionIdentifier": "com.example.sso.extension",
        "TeamIdentifier": "ABCDE12345",
        "Type": "Credential",
        "Realm": "EXAMPLE.COM",
        "Hosts": [
            ".example.com"
        ],
        "ExtensionData": {
            "useSiteAutoDiscovery": true
        }
    }
}
```

**Redirect**:

This configuration sets up a Redirect-type SSO extension that intercepts authentication requests to specific login URLs.

```json
{
    "Type": "com.apple.configuration.extensible-sso",
    "Identifier": "2A3B4C5D-6E7F-8A9B-0C1D-2E3F4A5B6C7D",
    "ServerToken": "F1E2D3C4-B5A6-7890-ABCD-EF1234567890",
    "Payload": {
        "ExtensionIdentifier": "com.example.sso.extension",
        "TeamIdentifier": "ABCDE12345",
        "Type": "Redirect",
        "URLs": [
            "https://login.example.com/auth",
            "https://sso.example.com/"
        ],
        "ScreenLockedBehavior": "Cancel"
    }
}
```

## Topics

### Objects
- [object ExtensibleSSOExtensionDataObject](extensiblessoextensiondataobject.md)
  A dictionary of arbitrary data passed through to the app extension.
- [object ExtensibleSSOPlatformSSOObject](extensiblessoplatformssoobject.md)
  The dictionary to configure Platform SSO.

## Properties

- `DeniedBundleIdentifiers` ([string]): An array of bundle identifiers of apps that don’t use SSO provided by this extension.
- `ExtensionComposedIdentifier` (string) *(required)*: The identifier of the provider to use for this configuration. Useful for apps that contain more than one DNS proxy extension. In iOS and visionOS, the identifier is a bundle ID, for example, “com.example.app.sso-extension”. In macOS, the identifier is a composed identifier. The format of the composed identifier is “Bundle-ID (Team-ID)”. “Bundle-ID” is the bundle identifier string of the app extension. “Team-ID” is the team identifier from the app extension’s code signature. For example, “com.example.app.sso-extension (ABCD1234)”.
- `ExtensionData` (ExtensibleSSOExtensionDataObject): A dictionary of arbitrary data passed through to the app extension.
- `Hosts` ([string]): An array of host or domain names that apps can authenticate through the app extension. Required for `Credential` payloads. Ignored for `Redirect` payloads. The system: - Matches host or domain names case-insensitively
- Requires that all the host and domain names of all installed Extensible SSO payloads are unique > **Note**:  Host names that begin with a “.” are wildcard suffixes that match all subdomains; otherwise the host name needs be an exact match.
- `PlatformSSO` (ExtensibleSSOPlatformSSOObject): The dictionary to configure Platform SSO. Available: macOS 27+
- `Realm` (string): The realm name for `Credential` payloads. Use proper capitalization for this value. Ignored for `Redirect` payloads.
- `ScreenLockedBehavior` (string): If set to `Cancel`, the system cancels authentication requests when the screen is locked. If set to `DoNotHandle`, the request continues without SSO instead. This doesn’t apply to requests where `userInterfaceEnabled` is `false`, or for background [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) requests.
- `Type` (string) *(required)*: The type of SSO.
- `URLs` ([string]): An array of URL prefixes of identity providers where the app extension performs SSO. Required for `Redirect` payloads. Ignored for `Credential` payloads. The URLs need to begin with `http://` or `https://`. The system: - Matches scheme and host name case-insensitively
- Doesn’t allow query parameters and URL fragments
- Requires that the URLs of all installed Extensible SSO payloads are unique

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
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesso)*