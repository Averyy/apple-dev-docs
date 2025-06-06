# hexDigit

**Framework**: RegexBuilder  
**Kind**: property

A character class that matches any hexadecimal digit.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static var hexDigit: CharacterClass { get }
```

#### Discussion

`hexDigit` matches the ASCII characters `0` through `9`, and upper- or lowercase `a` through `f`. The corresponding characters in the “Halfwidth and Fullwidth Forms” Unicode block are not matched by this character class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/characterclass/hexdigit)*