# newlineSequence

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

A character class that matches any newline sequence.

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
static var newlineSequence: CharacterClass { get }
```

Available when `Self` is `CharacterClass`.

## Discussion

This character class is equivalent to `\R` or `\n` in regex syntax.

## See Also

### Matching whitespace and line endings
- [static var horizontalWhitespace: CharacterClass](./horizontalwhitespace.md)
  A character class that matches any element that is classified as horizontal whitespace.
- [static var verticalWhitespace: CharacterClass](./verticalwhitespace.md)
  A character class that matches any element that is classified as vertical whitespace.
- [static var whitespace: CharacterClass](./whitespace.md)
  A character class that matches any element that is classified as whitespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/newlinesequence)*