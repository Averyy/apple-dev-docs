# anyOf(_:)

**Framework**: RegexBuilder  
**Kind**: method

Returns a character class that matches any character in the given string or sequence.

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
static func anyOf<S>(_ s: S) -> CharacterClass where S : Sequence, S.Element == Character
```

#### Discussion

Calling this method with a group of characters is equivalent to listing those characters in a custom character class in regex syntax. For example, the two regexes in this example are equivalent:

```swift
let regex1 = /[abcd]+/
let regex2 = OneOrMore(.anyOf("abcd"))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/characterclass/anyof(_:)-1s0kt)*