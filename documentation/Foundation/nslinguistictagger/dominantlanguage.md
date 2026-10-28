# dominantLanguage

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the dominant language of the string set for the linguistic tagger.

**Availability**:
- iOS 11.0+ - Deprecated in 27.2
- iPadOS 11.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.13+ - Deprecated in 27.2
- tvOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 4.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
var dominantLanguage: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * dominantLanguage;
```

## Return Value

The BCP-47 tag identifying the dominant language of the string, or the tag “und” if a specific language cannot be determined.

## Discussion

If you want to know the dominant language of a string that you’re analyzing with a linguistic tagger (for example, identifying part of speech for each word), specify the [`language`](../nslinguistictagscheme/language.md) tag scheme in the initializer. After you set the [`string`](./string.md) property of the linguistic tagger, the dominant language can be determined with the [`dominantLanguage`](./dominantlanguage.md) property, as shown in this example:

```swift
let text = "Die Kleinen haben friedlich zusammen gespielt."
let tagger = NSLinguisticTagger(tagSchemes: [.language], options: 0)
tagger.string = text
tagger.dominantLanguage // "de"
```

In the example, the BCP-47 language tag “de” is returned as the dominant language, indicating that the text is in German.

## See Also

### Determining the Dominant Language and Orthography
- [class func dominantLanguage(for: String) -> String?](./dominantlanguage%28for%29.md)
  Returns the dominant language for the specified string.
- [func orthography(at: Int, effectiveRange: NSRangePointer?) -> NSOrthography?](./orthography%28at,effectiverange%29.md)
  Returns the orthography at the index and also returns the effective range.
- [func setOrthography(NSOrthography?, range: NSRange)](./setorthography%28_,range%29.md)
  Sets the orthography for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/dominantlanguage)*