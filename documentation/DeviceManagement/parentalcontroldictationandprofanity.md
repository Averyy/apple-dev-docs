# ParentalControlDictationAndProfanity

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures parental control for dictation and profanity.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object ParentalControlDictationAndProfanity
```

#### Discussion

Specify `com.apple.ironwood.support` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

## Properties

- `Ironwood Allowed` (boolean): If `false`, disables dictation. Use `allowDictation` in Restrictions instead. Deprecated: macOS 10.13+
- `Profanity Allowed` (boolean): If `false`, suppresses profanity. Use `forceAssistantProfanityFilter` in Restrictions instead. Deprecated: macOS 10.13+

## See Also

- [object APN](apn.md)
  The payload that configures access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload that configures FileVault recovery key redirection.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload that configures media management.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontroldictationandprofanity)*