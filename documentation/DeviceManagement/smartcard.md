# SmartCard

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a smart card.

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
object SmartCard
```

#### Discussion

Specify `com.apple.security.smartcard` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>UserPairing</key>
            <false/>
            <key>allowSmartCard</key>
            <false/>
            <key>checkCertificateTrust</key>
            <false/>
            <key>oneCardPerUser</key>
            <false/>
            <key>tokenRemovalAction</key>
            <integer>1</integer>
            <key>enforceSmartCard</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mysmartcardpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.smartcard</string>
            <key>PayloadUUID</key>
            <string>88f7336c-d9f6-44d1-b486-11e4080e2223</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>SmartCard</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>85091214-a32f-4131-8b03-0045e5d81c42</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `allowSmartCard` (boolean): If `false`, the system disables smart cards for logins, authorizations, and screen saver unlocking. It’s still allowed for other functions, such as signing emails and accessing the web. The device requires a restart for a setting change to take effect.
- `checkCertificateTrust` (integer): Configures the certificate trust check and has one of the following possible values: - `0`: Turns off certificate trust check.
- `1`: Turns on certificate trust check. The device performs a standard validity check but doesn’t include additional revocation checks.
- `2`: Turns on certificate trust check. The device also performs a soft revocation check. Until CRL/OCSP explicitly rejects the certificate, the device considers it valid. This setting means that unavailable or unreachable CRL/OCSP allow this check to succeed.
- `3`: Turns on certificate trust check. The device also performs a hard revocation check. Unless CRL/OCSP explicitly says “This certificate is OK,” the device considers it invalid. This option is the most secure.
- `enforceSmartCard` (boolean): If `true`, a user can only log in or authenticate with a smart card. Available: macOS 10.13.2+
- `oneCardPerUser` (boolean): If `true`, a user can pair with only one smart card, although existing pairings are allowed if already set up.
- `tokenRemovalAction` (integer): If `1`, the device enables the screen saver when the user removes the smart card. Available: macOS 10.13.4+
- `UserPairing` (boolean): If `false`, users don’t get the pairing dialog, although existing pairings still work.

## See Also

- [object Passcode](passcode.md)
  The payload that configures a passcode policy.
- [object SecurityPreferences](securitypreferences.md)
  The payload that configures security preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/smartcard)*