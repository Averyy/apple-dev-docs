# any

**Framework**: RegexBuilder  
**Kind**: property

A character class that matches any element.

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
static var any: CharacterClass { get }
```

#### Discussion

This character class is unaffected by the `dotMatchesNewlines()` method. To match any character that isn’t a newline, see [`anyNonNewline`](characterclass/anynonnewline.md).

This character class is equivalent to the regex syntax “dot” metacharacter in single-line mode: `(?s:.)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/characterclass/any)*