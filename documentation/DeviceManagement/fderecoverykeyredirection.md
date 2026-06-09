# FDERecoveryKeyRedirection

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures FileVault recovery key redirection.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object FDERecoveryKeyRedirection
```

#### Discussion

Specify `com.apple.security.FDERecoveryRedirect` as the payload type.

Although the previous FDE Recovery payload is no longer supported in macOS 10.13 and later, it’s still supported in macOS 10.9 through 10.12. When installed, this payload causes any FDE recovery keys to be redirected to the specified URL instead of being sent to Apple. This requires sites to implement their own HTTPS server to receive the recovery keys through a POST request.

Note these cautions:

- The payload must exist in a system-scoped profile.
- Installing more than one payload of this type per machine results in an error.

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

## Properties

- `EncryptCertPayloadUUID` (string) *(required)*: The UUID of a payload within the same profile that contains a certificate used to encrypt the recovery key when it’s sent to the redirected URL. The referenced payload must be of type `com.apple.security.pkcs1`. Deprecated: macOS 10.13+
- `RedirectURL` (string) *(required)*: The URL to which FDE recovery keys should be sent instead of to Apple. The URL must begin with https://. Deprecated: macOS 10.13+

## See Also

- [object APN](apn.md)
  The payload that configures access point names.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload that configures media management.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fderecoverykeyredirection)*