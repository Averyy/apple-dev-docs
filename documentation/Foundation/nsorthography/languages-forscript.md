# languages(forScript:)

**Framework**: Foundation  
**Kind**: method

Returns the list of languages for the specified script.

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
func languages(forScript script: String) -> [String]?
```

#### Discussion

The value of this property is an array of BCP-47 language tags, such as `"en"` or `"fr"`, that identify the languages.

## Parameters

- `script`: The specified script.

## See Also

- [var languageMap: [String : [String]]](nsorthography/languagemap.md)
  A dictionary that maps script tags to arrays of language tags.
- [var dominantLanguage: String](nsorthography/dominantlanguage.md)
  The first language in the list of languages for the dominant script.
- [var dominantScript: String](nsorthography/dominantscript.md)
  The dominant script for the text.
- [func dominantLanguage(forScript: String) -> String?](nsorthography/dominantlanguage(forscript:).md)
  Returns the dominant language for the specified script.
- [var allScripts: [String]](nsorthography/allscripts.md)
  The scripts appearing as keys in the language map.
- [var allLanguages: [String]](nsorthography/alllanguages.md)
  The languages appearing in values of the language map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorthography/languages(forscript:))*