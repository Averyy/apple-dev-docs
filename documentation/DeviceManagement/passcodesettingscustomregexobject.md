# PasscodeSettingsCustomRegexObject

**Framework**: Device Management  
**Kind**: dictionary

A regular expression and its description to enforce password compliance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- visionOS 2.0+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object PasscodeSettingsCustomRegexObject
```

#### Discussion

Use the simpler passcode settings whenever possible, and rely on regular expression matching only when necessary. Mistakes in regular expressions can lead to frustrating user experiences, such as unsatisfiable passcode policies, or policy descriptions that don’t match the enforced policy.

## See Also

- [object PasscodeSettingsCustomRegex_DescriptionObject](passcodesettingscustomregex_descriptionobject.md)
  A dictionary that contains supported OS language IDs for the keys and values that represent a localized description of the policy that the regular expression enforces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/passcodesettingscustomregexobject)*