# isLowercase

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this character is considered lowercase.

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
var isLowercase: Bool { get }
```

#### Discussion

Lowercase characters change when converted to uppercase, but not when converted to lowercase. The following characters are all lowercase:

- “é” (U+0065 LATIN SMALL LETTER E, U+0301 COMBINING ACUTE ACCENT)
- “и” (U+0438 CYRILLIC SMALL LETTER I)
- “π” (U+03C0 GREEK SMALL LETTER PI)

## See Also

- [var isCased: Bool](character/iscased.md)
  A Boolean value indicating whether this character changes under any form of case conversion.
- [var isUppercase: Bool](character/isuppercase.md)
  A Boolean value indicating whether this character is considered uppercase.
- [func uppercased() -> String](character/uppercased.md)
  Returns an uppercased version of this character.
- [func lowercased() -> String](character/lowercased.md)
  Returns a lowercased version of this character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/islowercase)*