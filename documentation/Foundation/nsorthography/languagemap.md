# languageMap

**Framework**: Foundation  
**Kind**: property

A dictionary that maps script tags to arrays of language tags.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var languageMap: [String : [String]] { get }
```

#### Discussion

The dictionary’s keys are ISO 15924 script codes (such as `"Latn"` or `"Cyrl"`) and its values are arrays of BCP-47 language tags (such as `"en"`, `"fr"`, or `"de"`).

## See Also

- [var dominantLanguage: String](nsorthography/dominantlanguage.md)
  The first language in the list of languages for the dominant script.
- [var dominantScript: String](nsorthography/dominantscript.md)
  The dominant script for the text.
- [func dominantLanguage(forScript: String) -> String?](nsorthography/dominantlanguage(forscript:).md)
  Returns the dominant language for the specified script.
- [func languages(forScript: String) -> [String]?](nsorthography/languages(forscript:).md)
  Returns the list of languages for the specified script.
- [var allScripts: [String]](nsorthography/allscripts.md)
  The scripts appearing as keys in the language map.
- [var allLanguages: [String]](nsorthography/alllanguages.md)
  The languages appearing in values of the language map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorthography/languagemap)*