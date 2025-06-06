# init(dominantScript:languageMap:)

**Framework**: Foundation  
**Kind**: init

Creates an orthography object with the specified dominant script and language map.

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
init(dominantScript script: String, languageMap map: [String : [String]])
```

#### Return Value

An orthography object initialized with the specified script and language map.

#### Discussion

You typically use the [`defaultOrthography(forLanguage:)`](nsorthography/defaultorthography(forlanguage:).md) method to create orthography objects with automatic language mapping. Use this initializer only if you need to override the script associated with one or more languages.

## Parameters

- `script`: The dominant script.
- `map`: A dictionary mapping ISO 15924 script codes to arrays of BCP-47 language tags.

## See Also

- [class func defaultOrthography(forLanguage: String) -> Self](nsorthography/defaultorthography(forlanguage:).md)
  Creates and returns an orthography object with the default language map for the specified language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorthography/init(dominantscript:languagemap:))*