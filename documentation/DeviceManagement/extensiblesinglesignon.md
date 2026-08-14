# ExtensibleSingleSignOn

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures an app extension that performs single sign-on (SSO).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.1+

## Declaration

```swift
object ExtensibleSingleSignOn
```

## Mentions

- [Implementing Platform SSO during Automated Device Enrollment](implementing-platform-sso-during-automated-device-enrollment.md)
- [Configuring Platform Single Sign-on](configuring-platform-single-sign-on.md)
- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

Specify `com.apple.extensiblesso` as the payload type.

The system supports user channel installation in macOS 11 and later.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, visionOS |
| User channel | macOS, Shared iPad |
| Allow manual install | N/A |
| Requires supervision | N/A |
| Requires user-approved MDM | macOS |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, visionOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>ExtensionData</key>
            <dict>
                <key>useSiteAutoDiscovery</key>
                <true/>
            </dict>
            <key>ExtensionIdentifier</key>
            <string>com.example.com</string>
            <key>TeamIdentifier</key>
            <string>RandomTeamID</string>
            <key>Hosts</key>
            <array>
                <string>.com.example.com</string>
            </array>
            <key>Realm</key>
            <string>COM.URL.COM</string>
            <key>Type</key>
            <string>Credential</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myessopayload</string>
            <key>PayloadType</key>
            <string>com.apple.extensiblesso</string>
            <key>PayloadUUID</key>
            <string>dbed949d-39a2-440d-a84b-e0c825cdcb2e</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Extensible SSO</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>da3bbbec-a753-4aa7-aeae-a74b7a65c0b5</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object ExtensibleSingleSignOn.ExtensionData](extensiblesinglesignon/extensiondata-data.dictionary.md)
  The additional data to pass to the app extension.
- [object ExtensibleSingleSignOn.PlatformSSO](extensiblesinglesignon/platformsso-data.dictionary.md)
  The dictionary to configure Platform SSO. Requires setting `Type` to `Redirect`.

## Properties

- `AuthenticationMethod` (string): The Platform SSO authentication method the extension uses. Requires that the SSO Extension also supports the method. Don’t use this. Use the `AuthenticationMethod` key in the `PlatformSSO` dictionary instead. Available: macOS 13+
Deprecated: macOS 14+
- `DeniedBundleIdentifiers` ([string]): An array of bundle identifiers of apps that don’t use SSO provided by this extension. Available: iOS 15+ | iPadOS 15+ | macOS 12+ | visionOS 1.1+
- `ExtensionData` (ExtensibleSingleSignOn.ExtensionData): A dictionary of arbitrary data passed through to the app extension.
- `ExtensionIdentifier` (string) *(required)*: The bundle identifier of the app extension that performs SSO for the specified URLs.
- `Hosts` ([string]): An array of host or domain names that apps can authenticate through the app extension. Required for `Credential` payloads. Ignored for `Redirect` payloads. The system: - Matches host or domain names case-insensitively
- Requires that all the host and domain names of all installed Extensible SSO payloads are unique > **Note**:  Host names that begin with a “.” are wildcard suffixes that match all subdomains; otherwise the host name needs be an exact match.
- `PlatformSSO` (ExtensibleSingleSignOn.PlatformSSO): The dictionary to configure Platform SSO. Requires setting `Type` to `Redirect`. Available: macOS 14+
- `Realm` (string): The realm name for `Credential` payloads. Use proper capitalization for this value. Ignored for `Redirect` payloads.
- `RegistrationToken` (string): The token this device uses for registration with Platform SSO. Use it for silent registration with the Identity Provider. Requires that `AuthenticationMethod` in `PlatformSSO` isn’t empty. Available: macOS 13+
- `ScreenLockedBehavior` (string): If set to `Cancel`, the system cancels authentication requests when the screen is locked. If set to `DoNotHandle`, the request continues without SSO instead. This doesn’t apply to requests where `userInterfaceEnabled` is `false`, or for background [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) requests. Available: iOS 15+ | iPadOS 15+ | macOS 12+ | visionOS 1.1+
- `TeamIdentifier` (string): The team identifier of the app extension. The device requires this key on macOS and ignores it elsewhere. Available: macOS 10.15+
- `Type` (string) *(required)*: The type of SSO.
- `URLs` ([string]): An array of URL prefixes of identity providers where the app extension performs SSO. Required for `Redirect` payloads. Ignored for `Credential` payloads. The URLs need to begin with `http://` or `https://`. The system: - Matches scheme and host name case-insensitively
- Doesn’t allow query parameters and URL fragments
- Requires that the URLs of all installed Extensible SSO payloads are unique

## See Also

- [object DirectoryService](directoryservice.md)
  The payload that configures an Active Directory (AD) domain.
- [object ExtensibleSingleSignOnKerberos](extensiblesinglesignonkerberos.md)
  The payload that configures an app extension that performs single sign-on with the Kerberos extension.
- [object Identification](identification.md)
  The payload that configures the names of the account user.
- [object IdentityPreference](identitypreference.md)
  The payload that configures the user’s identity on the device.
- [object SingleSignOn](singlesignon.md)
  The payload that configures single sign-on (SSO).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon)*