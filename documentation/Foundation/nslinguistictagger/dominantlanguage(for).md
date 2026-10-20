# dominantLanguage(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the dominant language for the specified string.

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
class func dominantLanguage(for string: String) -> String?
```

```objc
+ (NSString *) dominantLanguageForString:(NSString *) string;
```

#### Return Value

The BCP-47 tag identifying the dominant language of the string, or the tag “und” if a specific language cannot be determined.

#### Discussion

The [`dominantLanguage(for:)`](./dominantlanguage%28for%29.md) method is a convenience method for creating a new linguistic tagger, setting the [`string`](./string.md) property, and getting the [`dominantLanguage`](./dominantlanguage.md) property. If you analyze the same string more than once, create a linguistic tagger object instead of calling the method, as shown in this example:

```swift
let text = "Die Kleinen haben friedlich zusammen gespielt."
NSLinguisticTagger.dominantLanguage(for: text) // "de"
```

In the example, the BCP-47 language tag “de” is returned as the dominant language, indicating that the text is in German.

## Parameters

- `string`: The string for which the dominant language is determined.

## See Also

### Determining the Dominant Language and Orthography
- [var dominantLanguage: String?](./dominantlanguage.md)
  Returns the dominant language of the string set for the linguistic tagger.
- [func orthography(at: Int, effectiveRange: NSRangePointer?) -> NSOrthography?](./orthography%28at,effectiverange%29.md)
  Returns the orthography at the index and also returns the effective range.
- [func setOrthography(NSOrthography?, range: NSRange)](./setorthography%28_,range%29.md)
  Sets the orthography for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/dominantlanguage(for:))*