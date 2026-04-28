# ExchangeActiveSync

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Exchange ActiveSync accounts.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ExchangeActiveSync
```

#### Discussion

Specify `com.apple.eas.account` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, visionOS |
| User channel | Shared iPad |
| Allow manual install | iOS, visionOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, visionOS |
| Allow multiple payloads | iOS, Shared iPad, visionOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EmailAddress</key>
            <string>juanchavez4@companyemail.com</string>
            <key>EnableCalendars</key>
            <true/>
            <key>EnableCalendarsUserOverridable</key>
            <true/>
            <key>EnableContacts</key>
            <true/>
            <key>EnableContactsUserOverridable</key>
            <true/>
            <key>EnableMail</key>
            <true/>
            <key>EnableMailUserOverridable</key>
            <true/>
            <key>EnableNotes</key>
            <true/>
            <key>EnableNotesUserOverridable</key>
            <true/>
            <key>EnableReminders</key>
            <true/>
            <key>EnableRemindersUserOverridable</key>
            <true/>
            <key>Host</key>
            <string>host.companyemail.com</string>
            <key>MailNumberOfPastDaysToSync</key>
            <integer>7</integer>
            <key>OAuth</key>
            <false/>
            <key>OverridePreviousPassword</key>
            <false/>
            <key>SMIMEEnabled</key>
            <false/>
            <key>SMIMEEncryptionEnabled</key>
            <false/>
            <key>SMIMESigningEnabled</key>
            <false/>
            <key>SSL</key>
            <true/>
            <key>UserName</key>
            <string>juanchavez4@companyemail.com</string>
            <key>disableMailRecentsSyncing</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.myeaspayload</string>
            <key>PayloadType</key>
            <string>com.apple.eas.account</string>
            <key>PayloadUUID</key>
            <string>de789252-dcf2-42e7-91c8-0ab9f50aafc5</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Exchange Active Sync</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b8fd6fd7-a55e-4eb1-96af-d9c4d8562e38'</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object ExchangeActiveSync.CommunicationServiceRules](exchangeactivesync/communicationservicerules-data.dictionary.md)
  The communication service rules.

## Properties

- `allowMailDrop` (boolean): If `true`, the system enables this account to use Mail Drop.
- `Certificate` (data): The `.p12` identity certificate in NSData blob format, for accounts that allow authentication via certificate.
- `CertificateName` (string): The name or description of the certificate.
- `CertificatePassword` (string): The password necessary for the `.p12` identity certificate. Used with mandatory encryption of profiles.
- `CommunicationServiceRules` (ExchangeActiveSync.CommunicationServiceRules): The communication service handler rules for this account.
- `disableMailRecentsSyncing` (boolean): If `true`, the system excludes this account from Recent Addresses syncing.
- `EmailAddress` (string): The full email address for the account. If not present in the payload, the device prompts for this string during profile installation.
- `EnableCalendars` (boolean): If `false`, the system disables the Calendars service for this account. The user can reenable Calendars service in Settings unless `EnableCalendarsUserOverridable` is `false`. > **Note**:  At least of the following fields needs to be `true`: `EnableMail`, `EnableContacts`, `EnableCalendars`, `EnableReminders`, and `EnableNotes`.
- `EnableCalendarsUserOverridable` (boolean): If `false`, the system prevents the user from changing the state of the Calendars service for this account in Settings.
- `EnableContacts` (boolean): If `false`, the system disables the Contacts service for this account. The user can reenable Contacts service in Settings unless `EnableContactsUserOverridable` is `false`. > **Note**:  At least of the following fields needs to be `true`: `EnableMail`, `EnableContacts`, `EnableCalendars`, `EnableReminders`, and `EnableNotes`.
- `EnableContactsUserOverridable` (boolean): If `false`, the system prevents the user from changing the state of the Contacts service for this account in Settings.
- `EnableMail` (boolean): If `false`, the system disables the Mail service for this account. The user can reenable Mail service in Settings unless `EnableMailUserOverridable` is `false`. > **Note**:  At least of the following fields needs to be `true`: `EnableMail`, `EnableContacts`, `EnableCalendars`, `EnableReminders`, and `EnableNotes`.
- `EnableMailUserOverridable` (boolean): If `false`, the system prevents the user from changing the state of the Mail service for this account in Settings.
- `EnableNotes` (boolean): If `false`, the system disables the Notes service for this account. The user can reenable Notes service in Settings unless `EnableNotesUserOverridable` is `false`. > **Note**:  At least of the following fields needs to be `true`: `EnableMail`, `EnableContacts`, `EnableCalendars`, `EnableReminders`, and `EnableNotes`.
- `EnableNotesUserOverridable` (boolean): If `false`, prevents the user from changing the state of the Notes service for this account in Settings.
- `EnableReminders` (boolean): If `false`, the system disables the Reminders service for this account. The user can reenable Reminders service in Settings unless `EnableRemindersUserOverridable` is `false`. > **Note**:  At least of the following fields needs to be `true`: `EnableMail`, `EnableContacts`, `EnableCalendars`, `EnableReminders`, and `EnableNotes`.
- `EnableRemindersUserOverridable` (boolean): If `false`, the system prevents the user from changing the state of the Reminders service for this account in Settings.
- `HeaderMagic` (string): The value of the `X-Apple-Config-Magic` header in each EAS HTTP request.
- `Host` (string): The Exchange server host name or IP address.
- `MailNumberOfPastDaysToSync` (integer): The number of days in the past to sync mail on the device. For no limit, use the value `0`.
- `OAuth` (boolean): If `true`, enables OAuth for authentication. If enabled, don’t specify a password. Available only in iOS 12.0 and above.
- `OAuthSignInURL` (string): The URL that this account should use for signing in through OAuth. Ignored unless `OAuth` is `true`. If you specify this URL, auto-discovery isn’t used for this account, so you need to also specify a host.
- `OAuthTokenRequestURL` (string): The URL that this account should use for token requests through OAuth. Ignored unless `OAuth` is `true`.
- `OverridePreviousPassword` (boolean): If `true`, the system overrides the previous user/EAS password with the new EAS password in the payload. Available in iOS 14 and later.
- `Password` (string): The password of the account. Use only with encrypted profiles.
- `PayloadCertificateUUID` (string): The UUID of the certificate payload within the same profile to use for the identity credential. If this field is present, the Certificate field isn’t used.
- `PreventAppSheet` (boolean): If `true`, prevents this account from sending mail in any app other than the Apple Mail app.
- `PreventMove` (boolean): If `true`, the system prevents moving messages from out of this email account into another account. This setting also prevents forwarding or replying from an account other than the recipient of the message.
- `SMIMEEnabled` (boolean): If `true`, the system enables S/MIME encryption. In iOS 10.0 and later, this key is ignored. Use `SMIMESigningEnabled` instead.
- `SMIMEEnableEncryptionPerMessageSwitch` (boolean): If `true`, the system displays the per-message encryption switch in the Mail Compose UI. Available in iOS 12.0 and later.
- `SMIMEEnablePerMessageSwitch` (boolean): If `true`, the system displays the per-message encryption switch in the Mail Compose UI. Available in iOS 8.0 and later. As of iOS 12.0, this key is deprecated. Use `SMIMEEnableEncryptionPerMessageSwitch` instead.
- `SMIMEEncryptByDefault` (boolean): If `true`, the system enables S/MIME encryption by default. If `SMIMEEnableEncryptionPerMessageSwitch` is `false`, the user can’t change this default. Available in iOS 12.0 and later.
- `SMIMEEncryptByDefaultUserOverrideable` (boolean): If `true`, the system enables encryption by default and the user can’t change it. Available in iOS 12.0 and later.
- `SMIMEEncryptionCertificateUUID` (string): The payload UUID of the identity certificate used to decrypt messages sent to this account. The system attaches the public certificate to outgoing mail to allow the user to receive encrypted mail. When the user sends encrypted mail, the system uses the public certificate to encrypt the copy of the mail in the user’s Sent mailbox.
- `SMIMEEncryptionCertificateUUIDUserOverrideable` (boolean): If `true`, the user can select the S/MIME encryption identity, and encryption is on.Available in iOS 12.0 and later.
- `SMIMEEncryptionEnabled` (boolean): If `true`, the system enables S/MIME encryption for this account. Available in iOS 10.0 and later. As of iOS 12.0, this key is deprecated. Use `SMIMEEncryptByDefault` instead.
- `SMIMESigningCertificateUUID` (string): The UUID of the identity certificate used to sign messages sent from this account.
- `SMIMESigningCertificateUUIDUserOverrideable` (boolean): If `true`, the user can select the signing identity. Available in iOS 12.0 and later.
- `SMIMESigningEnabled` (boolean): If `true`, the system enables S/MIME signing for this account. Available in iOS 10.0 and later.
- `SMIMESigningUserOverrideable` (boolean): If `true`, the user can turn S/MIME signing on or off in Settings. Available in iOS 12.0 and later.
- `SSL` (boolean): If `true`, the system enables SSL for authentication.
- `UserName` (string): This user name for this Exchange account. Required for noninteractive installations like MDM in iOS.
- `VPNUUID` (string): The VPNUUID of the per-app VPN the account uses for network communication. Available in iOS 14 and later.

## See Also

- [object ExchangeWebServices](exchangewebservices.md)
  The payload that configures an Exchange Web Services accounts.
- [object Mail](mail.md)
  The payload that configures a Mail account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/exchangeactivesync)*