# APN

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures access point names.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+

## Declaration

```swift
object APN
```

#### Discussion

Specify `com.apple.apn.managed` as the payload type.

This profile is deprecated. Use the [`Cellular`](cellular.md) profile instead.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | N/A |
| Allow manual install | iOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

## Topics

### Objects
- [object APN.DefaultsData](apn/defaultsdata-data.dictionary.md)
  An array of access point name dictionaries.

## Properties

- `DefaultsData` (APN.DefaultsData) *(required)*: The list of access point names (APNs). Deprecated: iOS 7+ | iPadOS 7+
- `DefaultsDomainName` (string) *(required)*: The domain name. Deprecated: iOS 7+ | iPadOS 7+

## See Also

- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload that configures FileVault recovery key redirection.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload that configures media management.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apn)*