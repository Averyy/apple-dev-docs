# Passcode.CustomRegex

**Framework**: Device Management  
**Kind**: dictionary

The regex defining the passcode policy.

**Availability**:
- macOS 14.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Passcode.CustomRegex
```

## Topics

### Objects
- [object Passcode.CustomRegex.PasswordContentDescription](passcode/customregex-data.dictionary/passwordcontentdescription-data.dictionary.md)
  Descriptions of the policy, localized to supported locales.

## Properties

- `passwordContentDescription` (Passcode.CustomRegex.PasswordContentDescription): Contains a dictionary of keys for supported OS language IDs (for example, “en-US”), and whose values represent a localized description of the policy enforced by the regular expression. Use the special `default` key can for languages that aren’t contained in the dictionary.
- `passwordContentRegex` (string) *(required)*: A regular expression string that the system matches against the password to determine whether it complies with a policy. The regular expression uses the ICU syntax ([`https://unicode-org.github.io/icu/userguide/strings/regexp.html`](https://developer.apple.comhttps://unicode-org.github.io/icu/userguide/strings/regexp.html)). The string must not exceed 2048 characters in length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/passcode/customregex-data.dictionary)*