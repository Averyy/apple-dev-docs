# setOrthography(_:range:)

**Framework**: Natural Language  
**Kind**: method

Sets the orthography for the specified range.

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
func setOrthography(_ orthography: NSOrthography, range: Range<String.Index>)
```

#### Discussion

If the orthography of the linguistic tagger is not set, it will determine it automatically from the contents of the text. You should call this method only if you know the orthography of the text by some other means.

## Parameters

- `orthography`: The orthography for the given range.
- `range`: The range of the string that is being assigned an orthography.

## See Also

- [var dominantLanguage: NLLanguage?](nltagger/dominantlanguage.md)
  The dominant language of the string set for the linguistic tagger.
- [func setLanguage(NLLanguage, range: Range<String.Index>)](nltagger/setlanguage(_:range:).md)
  Sets the language for a range of text within the tagger’s string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/setorthography(_:range:))*