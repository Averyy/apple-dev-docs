# digit

**Framework**: Swift  
**Kind**: property

A character class that matches any digit.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var digit: CharacterClass { get }
```

#### Discussion

This character class is equivalent to `\d` in regex syntax.

## See Also

- [static func anyOf<S>(S) -> CharacterClass](regexcomponent/anyof(_:)-3pexl.md)
  Returns a character class that matches any Unicode scalar in the given sequence.
- [static func anyOf<S>(S) -> CharacterClass](regexcomponent/anyof(_:)-4xgea.md)
  Returns a character class that matches any character in the given string or sequence.
- [static var any: CharacterClass](regexcomponent/any.md)
  A character class that matches any element.
- [static var anyGraphemeCluster: CharacterClass](regexcomponent/anygraphemecluster.md)
  A character class that matches any single `Character`, or extended grapheme cluster, regardless of the current semantic level.
- [static var anyNonNewline: CharacterClass](regexcomponent/anynonnewline.md)
  A character class that matches any element that isn’t a newline.
- [static var hexDigit: CharacterClass](regexcomponent/hexdigit.md)
  A character class that matches any hexadecimal digit.
- [static var word: CharacterClass](regexcomponent/word.md)
  A character class that matches any element that is a “word character”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/digit)*