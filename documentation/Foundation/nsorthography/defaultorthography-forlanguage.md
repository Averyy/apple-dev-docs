# defaultOrthography(forLanguage:)

**Framework**: Foundation  
**Kind**: method

Creates and returns an orthography object with the default language map for the specified language.

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
class func defaultOrthography(forLanguage language: String) -> Self
```

#### Discussion

This method automatically determines the script for the specified language. For example, the default orthography for the Hindi language has a language map with a single key, `"Deva"` (the ISO 15924 script code for Devanagari), that has a corresponding value of an array containing the element `"hi"` (the BCP-47 identifier for Hindi).

## Parameters

- `language`: A BCP-47 tag identifying the language.

## See Also

- [init(dominantScript: String, languageMap: [String : [String]])](nsorthography/init(dominantscript:languagemap:).md)
  Creates an orthography object with the specified dominant script and language map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorthography/defaultorthography(forlanguage:))*