# automaticallyIdentifiesLanguages

**Framework**: AppKit  
**Kind**: property

Sets whether the spell checker will automatically identify languages.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var automaticallyIdentifiesLanguages: Bool { get set }
```

## Parameters

- `flag`:   if languages should be automatically identified, otherwise  .

## See Also

- [var availableLanguages: [String]](nsspellchecker/availablelanguages.md)
  Provides a list of all available languages.
- [var userPreferredLanguages: [String]](nsspellchecker/userpreferredlanguages.md)
  Provides a subset of the available languages to be used for spell checking.
- [func language() -> String](nsspellchecker/language.md)
  Returns the current language used in spell checking.
- [func setLanguage(String) -> Bool](nsspellchecker/setlanguage(_:).md)
  Returns whether the specified language is in the Spelling pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/automaticallyidentifieslanguages)*