# FDERecoveryKeyEscrow

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures FileVault recovery key escrow.

**Availability**:
- macOS 10.13+

## Declaration

```swift
object FDERecoveryKeyEscrow
```

#### Discussion

Specify `com.apple.security.FDERecoveryKeyEscrow` as the payload type.

FileVault Full Disk Encryption (FDE) recovery keys are, by default, sent to Apple if the user requests them. Only one payload of this type is allowed per system.

If FileVault is enabled after the system installs this payload, the system encrypts the FileVault PRK with the specified certificate, wrapped with a CMS envelope and stored at `/var/db/FileVaultPRK.dat`. The `SecurityInfo` command makes this encrypted data available to the MDM server.

Alternatively, if a site uses its own administration software, it can extract the PRK from the foregoing location at any time. Because the PRK is encrypted using the certificate provided in the profile, only the author of the profile can extract the data.

Note these cautions:

- The payload needs to exist in a system-scoped profile.
- Installing more than one payload of this type per computer results in an error.
- The previous payload (`com.apple.security.FDERecoveryRedirect`) is no longer supported. You can still install the previous payload but the system ignores it, so servers can send out the same profile to old and new clients.
- If only an old-style redirection payload is installed at the time FileVault is turned on through the Security Preferences pane, the system displays an error and doesn’t enable FileVault.
- The system doesn’t provide a warning or error if FileVault is already enabled and an old-style payload is installed. In this case, it’s assumed that the recovery key has already been escrowed with the server.

Although the system no longer supports the previous FDE Recovery payload in macOS 10.13 and later, it’s still supported in macOS 10.9 through 10.12. Designate that payload by specifying `com.apple.security.FDERecoveryRedirect` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>Password</key>
            <string>Password123</string>
            <key>PayloadContent</key>
            <data>
            MIIDHjCCAgagAwIBAgIEeRGqmzANBgkqhkiG9w0BAQsFADBAMR8w
            HQYDVQQDDBZGaWxlVmF1bHQgUmVjb3ZlcnkgS2V5MR0wGwYDVQQN
            DBRpb3MtdGFyZGlzLmFwcGxlLmNvbTAeFw0xODA2MTkyMTA2Mzla
            Fw0xOTA2MTkyMTA2MzlaMEAxHzAdBgNVBAMMFkZpbGVWYXVsdCBS
            ZWNvdmVyeSBLZXkxHTAbBgNVBA0MFGlvcy10YXJkaXMuYXBwbGUu
            Y29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtOPt
            QOZ38VJMyMHWcWcs5S8D1xXVZ9OjQ7+8s7q+xNeGUZZXlHXehBHA
            iV8o7F9LvkOuJuwiWuw+9xj+ye7G4EnAtDA0p3bqZNoBIc3HIqDE
            BKTCPufqHEZfX6AH05mnYqr6fz8FbICQpx+1x6hO9f8ZSNrBJUxe
            viPCkYTvRFel9VvBS06Jijn3THFBZ9UAJjxTjU8PGQYHNRpa4pVh
            y1yIXjRwSKrmCv6NyF7vz9BQ8X4ExanGBG3P20tl5JhUTZlI+qo2
            B/ZYlQDvR+DMhrdaKtbJphdi4GNK8B87+bG7EmPCpiwLzVtkzSUK
            Y4WNbYCwUhJTjOclQsZFQKvT4QIBAQABoyAwHjALBgNVHQ8EBAMC
            ArQwDwYDVR0TAQH/BAUwAwEBADANBgkqhkiG9w0BAQsFAAOCAQEA
            rPLq0RFfAJO0Hq/Z+NLZp/EI3mBXD8a5Gq5VUepB4AYgxbmtS5Dr
            XJMlzi1ctYGj3+QN+9XbgNv/p3cphHvSBmvFmjL8gJ6AuqNG9/hV
            TYEsoS5i9pGIlWozTziS+EPbdHt76g4xOOPoQ3SDur+qpc3Hfi1A
            imCaRB2Ga/eIITDqQUi1Sfgz0r0Md0jIEpXnW8RSvAQm9tlt35os
            onzTvHiKjXkOxBrXGg84YSK9/MsvwcPUM/XZ9HmZMTVYnPRacZlX
            9m4yKJligP7vmSjpbQ6u5zngsilhLUezX9stOyduAKLxk354yW85
            CQEgrRbwQQzGSWlf8KV0sbubwz4H8w==
            </data>
            <key>PayloadIdentifier</key>
            <string>com.example.mypkcs1payload</string>
            <key>PayloadType</key>
            <string>com.apple.security.pkcs1</string>
            <key>PayloadUUID</key>
            <string>5ddd0439-620a-4939-8bbc-838ae490b12f</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
        <dict>
            <key>Defer</key>
            <true/>
            <key>DeferDontAskAtUserLogout</key>
            <false/>
            <key>DeferForceAtUserLoginMaxBypassAttempts</key>
            <integer>-1</integer>
            <key>Enable</key>
            <string>On</string>
            <key>PayloadCertificateUUID</key>
            <string>5ddd0439-620a-4939-8bbc-838ae490b12f</string>
            <key>ShowRecoveryKey</key>
            <true/>
            <key>UseKeychain</key>
            <true/>
            <key>UseRecoveryKey</key>
            <true/>
            <key>UserEntersMissingInfo</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.myfv2payload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX.FileVault2</string>
            <key>PayloadUUID</key>
            <string>8d5d8dfb-688a-436d-b827-b81e550702b3</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
        <dict>
            <key>EncryptCertPayloadUUID</key>
            <string>5ddd0439-620a-4939-8bbc-838ae490b12f</string>
            <key>Location</key>
            <string>Your Information is now escrowed</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myfderecoverykeyescrowpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.FDERecoveryKeyEscrow</string>
            <key>PayloadUUID</key>
            <string>202ffa93-e1ae-43b5-b9de-e656ac0c2045</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>FDE Recovery Key Escrow</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>bf625ece-5e99-489b-b197-6f1d7c52a601</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object FDEFileVault](fdefilevault.md)
  The payload that configures FileVault.
- [object FDEFileVaultOptions](fdefilevaultoptions.md)
  The payload that configures FileVault options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fderecoverykeyescrow)*