# dominantLanguage

**Framework**: Foundation  
**Kind**: property

Returns the dominant language of the string set for the linguistic tagger.

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
var dominantLanguage: String? { get }
```

#### Return Value

The BCP-47 tag identifying the dominant language of the string, or the tag “und” if a specific language cannot be determined.

#### Discussion

If you want to know the dominant language of a string that you’re analyzing with a linguistic tagger (for example, identifying part of speech for each word), specify the [`language`](nslinguistictagscheme/language.md) tag scheme in the initializer. After you set the [`string`](nslinguistictagger/string.md) property of the linguistic tagger, the dominant language can be determined with the [`dominantLanguage`](nslinguistictagger/dominantlanguage.md) property, as shown in this example:

```swift
let text = "Die Kleinen haben friedlich zusammen gespielt."
let tagger = NSLinguisticTagger(tagSchemes: [.language], options: 0)
tagger.string = text
tagger.dominantLanguage // "de"
```

In the example, the BCP-47 language tag “de” is returned as the dominant language, indicating that the text is in German.

## See Also

- [class func dominantLanguage(for: String) -> String?](nslinguistictagger/dominantlanguage(for:).md)
  Returns the dominant language for the specified string.
- [func orthography(at: Int, effectiveRange: NSRangePointer?) -> NSOrthography?](nslinguistictagger/orthography(at:effectiverange:).md)
  Returns the orthography at the index and also returns the effective range.
- [func setOrthography(NSOrthography?, range: NSRange)](nslinguistictagger/setorthography(_:range:).md)
  Sets the orthography for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/dominantlanguage)*