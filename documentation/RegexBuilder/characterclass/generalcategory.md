# generalCategory(_:)

**Framework**: RegexBuilder  
**Kind**: method

Returns a character class that matches any element with the given Unicode general category.

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
static func generalCategory(_ category: Unicode.GeneralCategory) -> CharacterClass
```

#### Discussion

For example, when passed `.uppercaseLetter`, this method is equivalent to `/\p{Uppercase_Letter}/` or `/\p{Lu}/`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/characterclass/generalcategory(_:))*