# language()

**Framework**: AppKit  
**Kind**: method

Returns the current language used in spell checking.

**Availability**:
- macOS ?+

## Declaration

```swift
func language() -> String
```

#### Return Value

The current spell checking language, as a string.

#### Discussion

The result string specifies the language using the language and regional designations described in Language and Locale Designations in [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

## See Also

- [var availableLanguages: [String]](nsspellchecker/availablelanguages.md)
  Provides a list of all available languages.
- [var userPreferredLanguages: [String]](nsspellchecker/userpreferredlanguages.md)
  Provides a subset of the available languages to be used for spell checking.
- [var automaticallyIdentifiesLanguages: Bool](nsspellchecker/automaticallyidentifieslanguages.md)
  Sets whether the spell checker will automatically identify languages.
- [func setLanguage(String) -> Bool](nsspellchecker/setlanguage(_:).md)
  Returns whether the specified language is in the Spelling pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/language())*