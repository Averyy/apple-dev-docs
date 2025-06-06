# isUppercase

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this character is considered uppercase.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isUppercase: Bool { get }
```

#### Discussion

Uppercase characters vary under case-conversion to lowercase, but not when converted to uppercase. The following characters are all uppercase:

- “É” (U+0045 LATIN CAPITAL LETTER E, U+0301 COMBINING ACUTE ACCENT)
- “И” (U+0418 CYRILLIC CAPITAL LETTER I)
- “Π” (U+03A0 GREEK CAPITAL LETTER PI)

## See Also

- [var isCased: Bool](character/iscased.md)
  A Boolean value indicating whether this character changes under any form of case conversion.
- [func uppercased() -> String](character/uppercased.md)
  Returns an uppercased version of this character.
- [var isLowercase: Bool](character/islowercase.md)
  A Boolean value indicating whether this character is considered lowercase.
- [func lowercased() -> String](character/lowercased.md)
  Returns a lowercased version of this character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/isuppercase)*