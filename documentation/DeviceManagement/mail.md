# Mail

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a Mail account.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- visionOS 1.1+

## Declaration

```swift
object Mail
```

#### Discussion

Specify `com.apple.mail.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, visionOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, visionOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, visionOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EmailAccountDescription</key>
            <string>Company Mail Account</string>
            <key>EmailAccountName</key>
            <string>Juan Chavez</string>
            <key>EmailAccountType</key>
            <string>EmailTypeIMAP</string>
            <key>EmailAddress</key>
            <string>juanchavez4@example.com</string>
            <key>IncomingMailServerAuthentication</key>
            <string>EmailAuthPassword</string>
            <key>IncomingMailServerHostName</key>
            <string>imap.example.com</string>
            <key>IncomingMailServerPortNumber</key>
            <integer>993</integer>
            <key>IncomingMailServerUseSSL</key>
            <true/>
            <key>IncomingMailServerUsername</key>
            <string>juanchavez4@example.com</string>
            <key>IncomingPassword</key>
            <string>Password123</string>
            <key>OutgoingMailServerAuthentication</key>
            <string>EmailAuthPassword</string>
            <key>OutgoingMailServerHostName</key>
            <string>smtp.example.com</string>
            <key>OutgoingMailServerPortNumber</key>
            <integer>587</integer>
            <key>OutgoingMailServerUseSSL</key>
            <true/>
            <key>OutgoingMailServerUsername</key>
            <string>juanchavez4@example.com</string>
            <key>OutgoingPassword</key>
            <string>Password123</string>
            <key>OutgoingPasswordSameAsIncomingPassword</key>
            <false/>
            <key>SMIMEEnablePerMessageSwitch</key>
            <false/>
            <key>SMIMEEnabled</key>
            <false/>
            <key>SMIMEEncryptionEnabled</key>
            <false/>
            <key>SMIMESigningEnabled</key>
            <false/>
            <key>allowMailDrop</key>
            <false/>
            <key>disableMailRecentsSyncing</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mymailpayload</string>
            <key>PayloadType</key>
            <string>com.apple.mail.managed</string>
            <key>PayloadUUID</key>
            <string>d6379d8d-9e05-4d99-80bc-0865f1fe0aca</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Mail</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>8e1961d8-898e-4d79-986f-c7a61af4103c</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `allowMailDrop` (boolean): If `true`, the system enables this account to use Mail Drop. Available: iOS 9.2+ | iPadOS 9.2+ | macOS 10.12+ | visionOS 1.1+
- `disableMailRecentsSyncing` (boolean): If `true`, the system excludes this account from Recent Addresses syncing. Available: iOS 6+ | iPadOS 6+ | macOS 10.7+ | visionOS 1.1+
- `EmailAccountDescription` (string): A user-visible description of the email account, shown in the Mail and Settings applications.
- `EmailAccountName` (string): The full user name for the account. The system displays this name in sent messages.
- `EmailAccountType` (string) *(required)*: Defines the protocol to use for the account.
- `EmailAddress` (string): The full email address for the account. If this string isn’t present in the payload, the device prompts the user for this string during interactive profile installation in Settings or System Preferences.
- `IncomingMailServerAuthentication` (string) *(required)*: The authentication scheme for incoming mail.
- `IncomingMailServerHostName` (string) *(required)*: The incoming mail server host name.
- `IncomingMailServerIMAPPathPrefix` (string): The path prefix for the IMAP mail server.
- `IncomingMailServerPortNumber` (integer): The incoming mail server port number. If not set, the system uses the default port for a given protocol.
- `IncomingMailServerUsername` (string): The user name for the email account, usually the same as the email address up to the “@” character. If not set and the account requires authentication for incoming email, the device prompts the user for this string during interactive profile installation in Settings or System Preferences.
- `IncomingMailServerUseSSL` (boolean): If `true`, the system enables SSL for authentication on the incoming mail server.
- `IncomingPassword` (string): The password for the incoming mail server. Only use this in encrypted profiles.
- `OutgoingMailServerAuthentication` (string) *(required)*: The authentication scheme for outgoing mail.
- `OutgoingMailServerHostName` (string) *(required)*: The outgoing mail server host name.
- `OutgoingMailServerPortNumber` (integer): The outgoing mail server port number. If not set, the system uses ports 25, 587, and 465, in that order.
- `OutgoingMailServerUsername` (string): The user name for the email account, usually the same as the email address up to the “@” character. If not set and the account requires authentication for outgoing email, the device prompts the user for this string during interactive profile installation in Settings or System Preferences.
- `OutgoingMailServerUseSSL` (boolean): If `true`, the system enables SSL authentication on the outgoing mail server.
- `OutgoingPassword` (string): The password for the outgoing mail server. Only use this in encrypted profiles.
- `OutgoingPasswordSameAsIncomingPassword` (boolean): If `true`, the system prompts the user only once for the password, which it uses for both outgoing and incoming mail. This setting supports only interactive profile installations. Non-interactive installations, such as MDM on iOS, don’t support this setting.
- `PreventAppSheet` (boolean): If `true`, the system prevents this account from sending mail in any app other than the Apple Mail app. Available: iOS 5+ | iPadOS 5+ | visionOS 1.1+
- `PreventMove` (boolean): If `true`, the system prevents moving messages out of this email account and into another account. It also prevents forwarding or replying from an account other than the recipient of the message. Available: iOS 5+ | iPadOS 5+ | visionOS 1.1+
- `SMIMEEnabled` (boolean): If `true`, the system enables S/MIME encryption. The system ignores this key in iOS 10.0 and later. Available: iOS 5+ | iPadOS 5+ | visionOS 1.1+
- `SMIMEEnableEncryptionPerMessageSwitch` (boolean): If `true`, the system displays the per-message encryption switch in the Mail Compose UI. Available: iOS 12+ | iPadOS 12+ | visionOS 1.1+
- `SMIMEEnablePerMessageSwitch` (boolean): If `true`, the system displays the per-message encryption switch in the Mail Compose UI. Deprecated in iOS 12.0. Use `SMIMEEnableEncryptionPerMessageSwitch` instead. Available: iOS 8+ | iPadOS 8+
Deprecated: iOS 10+ | iPadOS 10+
- `SMIMEEncryptByDefault` (boolean): If `true`, the system enables S/MIME encryption by default. Available: iOS 12+ | iPadOS 12+ | visionOS 1.1+
- `SMIMEEncryptByDefaultUserOverrideable` (boolean): If `true`, the user can turn encryption by default on/off, and encryption is on. Available: iOS 12+ | iPadOS 12+ | visionOS 1.1+
- `SMIMEEncryptionCertificateUUID` (string): The UUID of the identity certificate used to decrypt messages sent to this account. The system attaches the public certificate to outgoing mail to allow the user to receive encrypted mail. When the user sends encrypted mail, the system uses the public certificate to encrypt the copy of the mail in their Sent mailbox. Available: iOS 5+ | iPadOS 5+ | visionOS 1.1+
- `SMIMEEncryptionCertificateUUIDUserOverrideable` (boolean): If `true`, the user can select the S/MIME encryption identity, and encryption is on. Available: iOS 12+ | iPadOS 12+ | visionOS 1.1+
- `SMIMEEncryptionEnabled` (boolean): If `true`, the system enables S/MIME encryption for this account. Available: iOS 10+ | iPadOS 10+ | visionOS 1.1+
- `SMIMESigningCertificateUUID` (string): The payload UUID of the identity certificate used to sign messages sent from this account. Available: iOS 5+ | iPadOS 5+ | visionOS 1.1+
- `SMIMESigningCertificateUUIDUserOverrideable` (boolean): If `true`, the user can select the signing identity. Available: iOS 12+ | iPadOS 12+ | visionOS 1.1+
- `SMIMESigningEnabled` (boolean): If `true`, the system enables S/MIME signing for this account. Available: iOS 10+ | iPadOS 10+ | visionOS 1.1+
- `SMIMESigningUserOverrideable` (boolean): If `true`, the user can turn S/MIME signing on or off in Settings. Available: iOS 12+ | iPadOS 12+ | visionOS 1.1+
- `VPNUUID` (string): The VPNUUID of the per-app VPN the account uses for network communication. Available: iOS 14+ | iPadOS 14+ | visionOS 1.1+

## See Also

- [object ExchangeActiveSync](exchangeactivesync.md)
  The payload that configures Exchange ActiveSync accounts.
- [object ExchangeWebServices](exchangewebservices.md)
  The payload that configures an Exchange Web Services accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mail)*