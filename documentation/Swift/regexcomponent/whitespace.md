# whitespace

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

A character class that matches any element that is classified as whitespace.

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
static var whitespace: CharacterClass { get }
```

Available when `Self` is `CharacterClass`.

#### Discussion

This character class is equivalent to `\s` in regex syntax.

## See Also

### Matching whitespace and line endings
- [static var horizontalWhitespace: CharacterClass](./horizontalwhitespace.md)
  A character class that matches any element that is classified as horizontal whitespace.
- [static var newlineSequence: CharacterClass](./newlinesequence.md)
  A character class that matches any newline sequence.
- [static var verticalWhitespace: CharacterClass](./verticalwhitespace.md)
  A character class that matches any element that is classified as vertical whitespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/whitespace)*