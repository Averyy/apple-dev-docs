# CertificatePEM

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a PEM-formatted certificate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
object CertificatePEM
```

## Mentions

- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)

#### Discussion

Specify `com.apple.security.pem` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |

##### Example Profile

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadContent</key>
            <data>
            LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURTakNDQWpL
            Z0F3SUJBZ0lCQVRBTkJna3Foa2lHOXcwQkFRc0ZBREJLTVJZd0ZB
            WURWUVFEREExdFkzaDIKWVd4cFpHRjBhVzl1TVFzd0NRWURWUVFH
            RXdKVlV6RWpNQ0VHQ1NxR1NJYjNEUUVKQVJZVWNtOWljMjl1WDJG
            agpRR2xqYkc5MVpDNWpiMjB3SGhjTk1UZ3dNakUwTVRrMU9UUXpX
            aGNOTWpBd01qRTBNVGsxT1RReldqQktNUll3CkZBWURWUVFEREEx
            dFkzaDJZV3hwWkdGMGFXOXVNUXN3Q1FZRFZRUUdFd0pWVXpFak1D
            RUdDU3FHU0liM0RRRUoKQVJZVWNtOWljMjl1WDJGalFHbGpiRzkx
            WkM1amIyMHdnZ0VpTUEwR0NTcUdTSWIzRFFFQkFRVUFBNElCRHdB
            dwpnZ0VLQW9JQkFRQ3luNzR2Szh2NXRHU2NqK1pieHZhWWl5ZFFD
            cUtUNjFEVzlEdlM1bW4xcCtJcEp6M3hJdFI1Cnd6NCtXTmFzbWRt
            ek11L3BuRUkwaXA0SUxYaHpFUVpieHlIZElGQU1LTWNHTzZuekla
            S3NiZ2MveE1WcVJyM0YKWExTOTY4Vlg3djd2SFVxRFpveDhhMHVn
            b1NlM2ZIeEl1Z2FMTldRL0RYeE1mbllJQ0k4azNndXFtQ3Zib3No
            UwpaTnFhYXNLUlNzWWZFYlRZTUNkSVBYMnBDNDNGMzYyNE16R2RV
            RDZSYjJWZDRUamNQZXVINjVkdDhrbXI3NTc0Cjc5MDF2Zlp3ZDds
            UzFITHozcHdQa0s1UlZnOVU0dHJ5Y0xKUmJWSm9mTUhRUWJIMEZ4
            TWUxTUhpRmx4c1pwYjMKQTl1SDRjYzVyWlRocmpIeUlkTTZPZVoy
            UWVWQ1ZMR3ZBZ01CQUFHak96QTVNQThHQTFVZEV3RUIvd1FGTUFN
            QgpBUUF3RGdZRFZSMFBBCCgvQkFRREFnZUFNQllHQTFVZEpRRUIv
            d1FNTUFvR0NDc0dBUVVGQndNQ01BMEdDU3FHClNJYjNEUUVCQ3dV
            QUE0SUJBUUJ6RTdvdnRBRnVEWDNXQVFuMjc0K2NLTUsvT3JEK050
            dGJxZ2x0ZUFLV250ZlAKTk45VXFmSzhZaTBtZDEvQ3V4OEhWYXp5
            N0ZmdjlXZExHZjFJeDJoczAzcFVJalZUWmZHeWlac2Rhazd6NXZl
            YgpmdXFZT3F5L0VDUElxR2ZSYkxFeW9SZ0RUeTM2ODIzWUJ4bVdm
            bWV1SlFmQVdhTHFvbUd1Z0R6RDVPTFWKWHdHCml2MVdFc0dXYWhT
            Vzlxb3llSkhFcE5tamZ1c1BmSTd4UnY3Q1ByeXh1U2hEakFYdXl5
            cmdqVm5HdjUrdENzNnIKODNQd1NjdUhydU41Ymc4THE5bW9pVnpa
            Qy9WdGRFbTN6TzVwUnFjd0NRanZmUjUvVWJsT2Z5N2x5WkNlWUU3
            SApXKzlLUzdCbmVtRnBBSFhvU296b1M3WW1YQnhmT1BqbDB6MEhW
            V2VsCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K
            </data>
            <key>PayloadIdentifier</key>
            <string>com.example.mycertpempayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.pem</string>
            <key>PayloadUUID</key>
            <string>b740fbbc-ad70-4f59-b6f5-40887d284a70</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>CertificatePEM</string>
    <key>PayloadIdentifier</key>
    <string>com.example.profile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>0d198a1e-7d38-48f5-ad67-422382c1c9e7</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object ACMECertificate](acmecertificate.md)
  The payload that configures Automated Certificate Management Environment (ACME) settings.
- [object ActiveDirectoryCertificate](activedirectorycertificate.md)
  The payload that configures Active Directory Certificate settings.
- [object CertificatePKCS1](certificatepkcs1.md)
  The payload that configures a PKCS #1-formatted certificate.
- [object CertificatePKCS12](certificatepkcs12.md)
  The payload that configures a PKCS #12-formatted certificate.
- [object CertificateRoot](certificateroot.md)
  The payload that configures a root certificate.
- [object CertificatePreference](certificatepreference.md)
  The payload that configures a certificate preference.
- [object CertificateRevocation](certificaterevocation.md)
  The payload that configures certificate revocation checking.
- [object CertificateTransparency](certificatetransparency.md)
  The payload that configures certificate transparency enforcement.
- [object SCEP](scep.md)
  The payload that configures Simple Certificate Enrollment Protocol (SCEP) settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatepem)*