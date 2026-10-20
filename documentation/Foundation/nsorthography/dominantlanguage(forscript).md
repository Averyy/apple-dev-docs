# dominantLanguage(forScript:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the dominant language for the specified script.

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
func dominantLanguage(forScript script: String) -> String?
```

```objc
- (NSString *) dominantLanguageForScript:(NSString *) script;
```

#### Discussion

The value of this property is a BCP-47 language tag, such as `"en"` or `"fr"`, that identifies the dominant language.

## Parameters

- `script`: The specified script.

## See Also

### Determining Correspondences Between Languages and Scripts
- [var languageMap: [String : [String]]](./languagemap.md)
  A dictionary that maps script tags to arrays of language tags.
- [var dominantLanguage: String](./dominantlanguage.md)
  The first language in the list of languages for the dominant script.
- [var dominantScript: String](./dominantscript.md)
  The dominant script for the text.
- [func languages(forScript: String) -> [String]?](./languages%28forscript%29.md)
  Returns the list of languages for the specified script.
- [var allScripts: [String]](./allscripts.md)
  The scripts appearing as keys in the language map.
- [var allLanguages: [String]](./alllanguages.md)
  The languages appearing in values of the language map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorthography/dominantlanguage(forscript:))*