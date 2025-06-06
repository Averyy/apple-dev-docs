# anyOf(_:)

**Framework**: RegexBuilder  
**Kind**: method

Returns a character class that matches any Unicode scalar in the given sequence.

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
static func anyOf<S>(_ s: S) -> CharacterClass where S : Sequence, S.Element == Unicode.Scalar
```

#### Discussion

Calling this method with a group of Unicode scalars is equivalent to listing them in a custom character class in regex syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/characterclass/anyof(_:)-zvpp)*