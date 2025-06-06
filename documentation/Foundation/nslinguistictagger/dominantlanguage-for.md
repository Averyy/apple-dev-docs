# dominantLanguage(for:)

**Framework**: Foundation  
**Kind**: method

Returns the dominant language for the specified string.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func dominantLanguage(for string: String) -> String?
```

#### Return Value

The BCP-47 tag identifying the dominant language of the string, or the tag “und” if a specific language cannot be determined.

#### Discussion

The [`dominantLanguage(for:)`](nslinguistictagger/dominantlanguage(for:).md) method is a convenience method for creating a new linguistic tagger, setting the [`string`](nslinguistictagger/string.md) property, and getting the [`dominantLanguage`](nslinguistictagger/dominantlanguage.md) property. If you analyze the same string more than once, create a linguistic tagger object instead of calling the method, as shown in this example:

```swift
let text = "Die Kleinen haben friedlich zusammen gespielt."
NSLinguisticTagger.dominantLanguage(for: text) // "de"
```

In the example, the BCP-47 language tag “de” is returned as the dominant language, indicating that the text is in German.

## Parameters

- `string`: The string for which the dominant language is determined.

## See Also

- [var dominantLanguage: String?](nslinguistictagger/dominantlanguage.md)
  Returns the dominant language of the string set for the linguistic tagger.
- [func orthography(at: Int, effectiveRange: NSRangePointer?) -> NSOrthography?](nslinguistictagger/orthography(at:effectiverange:).md)
  Returns the orthography at the index and also returns the effective range.
- [func setOrthography(NSOrthography?, range: NSRange)](nslinguistictagger/setorthography(_:range:).md)
  Sets the orthography for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/dominantlanguage(for:))*