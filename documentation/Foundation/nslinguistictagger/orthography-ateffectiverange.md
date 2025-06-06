# orthography(at:effectiveRange:)

**Framework**: Foundation  
**Kind**: method

Returns the orthography at the index and also returns the effective range.

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
func orthography(at charIndex: Int, effectiveRange: NSRangePointer?) -> NSOrthography?
```

#### Return Value

The orthography for the location.

## Parameters

- `charIndex`: The character index to begin examination.
- `effectiveRange`: An NSRangePointer that, upon completion, contains the range of the orthography containing  .

## See Also

- [class func dominantLanguage(for: String) -> String?](nslinguistictagger/dominantlanguage(for:).md)
  Returns the dominant language for the specified string.
- [var dominantLanguage: String?](nslinguistictagger/dominantlanguage.md)
  Returns the dominant language of the string set for the linguistic tagger.
- [func setOrthography(NSOrthography?, range: NSRange)](nslinguistictagger/setorthography(_:range:).md)
  Sets the orthography for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/orthography(at:effectiverange:))*