# setOrthography(_:range:)

**Framework**: Foundation  
**Kind**: method

Sets the orthography for the specified range.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setOrthography(_ orthography: NSOrthography?, range: NSRange)
```

#### Discussion

If the orthography of the linguistic tagger is not set, it will determine it automatically from the contents of the text.  You should call this method only if you  know the orthography of the text by some other means.

## Parameters

- `orthography`: The orthography.
- `range`: The range.

## See Also

- [class func dominantLanguage(for: String) -> String?](nslinguistictagger/dominantlanguage(for:).md)
  Returns the dominant language for the specified string.
- [var dominantLanguage: String?](nslinguistictagger/dominantlanguage.md)
  Returns the dominant language of the string set for the linguistic tagger.
- [func orthography(at: Int, effectiveRange: NSRangePointer?) -> NSOrthography?](nslinguistictagger/orthography(at:effectiverange:).md)
  Returns the orthography at the index and also returns the effective range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/setorthography(_:range:))*