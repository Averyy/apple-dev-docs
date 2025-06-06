# setLanguage(_:range:)

**Framework**: Natural Language  
**Kind**: method

Sets the language for a range of text within the tagger’s string.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@nonobjc
func setLanguage(_ language: NLLanguage, range: Range<String.Index>)
```

## Parameters

- `language`: The language of the text range.
- `range`: The range of the string that is being assigned a language.

## See Also

- [var dominantLanguage: NLLanguage?](nltagger/dominantlanguage.md)
  The dominant language of the string set for the linguistic tagger.
- [func setOrthography(NSOrthography, range: Range<String.Index>)](nltagger/setorthography(_:range:).md)
  Sets the orthography for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/setlanguage(_:range:))*