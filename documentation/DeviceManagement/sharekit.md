# ShareKit

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures ShareKit.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object ShareKit
```

#### Discussion

Specify `com.apple.ShareKitHelper` as the payload type.

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

- `SHKAllowedShareServices` ([string]): The list of plugin IDs that show up in the user’s Share menu. If this array exists, only these items are permitted. Deprecated: macOS 10.12+
- `SHKDeniedShareServices` ([string]): The list of plugin IDs that won’t show up in the user’s Share menu. This key is used only if there’s no `SHKAllowedShareServices` key. Deprecated: macOS 10.12+

## See Also

- [object APN](apn.md)
  The payload that configures access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload that configures FileVault recovery key redirection.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload that configures media management.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/sharekit)*