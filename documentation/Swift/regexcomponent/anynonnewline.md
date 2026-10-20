# anyNonNewline

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

A character class that matches any element that isn’t a newline.

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
static var anyNonNewline: CharacterClass { get }
```

Available when `Self` is `CharacterClass`.

#### Discussion

This character class is unaffected by the `dotMatchesNewlines()` method. To match any character, including newlines, see [`any`](./any.md).

This character class is equivalent to the regex syntax “dot” metacharacter with single-line mode disabled: `(?-s:.)`.

## See Also

### Matching substring sequences
- [static func anyOf<S>(S) -> CharacterClass](./anyof%28_%29-3pexl.md)
  Returns a character class that matches any Unicode scalar in the given sequence.
- [static func anyOf<S>(S) -> CharacterClass](./anyof%28_%29-4xgea.md)
  Returns a character class that matches any character in the given string or sequence.
- [static var any: CharacterClass](./any.md)
  A character class that matches any element.
- [static var anyGraphemeCluster: CharacterClass](./anygraphemecluster.md)
  A character class that matches any single `Character`, or extended grapheme cluster, regardless of the current semantic level.
- [static var digit: CharacterClass](./digit.md)
  A character class that matches any digit.
- [static var hexDigit: CharacterClass](./hexdigit.md)
  A character class that matches any hexadecimal digit.
- [static var word: CharacterClass](./word.md)
  A character class that matches any element that is a “word character”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/anynonnewline)*