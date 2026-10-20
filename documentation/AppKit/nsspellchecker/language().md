# language()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the current language used in spell checking.

**Availability**:
- macOS

## Declaration

```swift
func language() -> String
```

```objc
- (NSString *) language;
```

#### Return Value

The current spell checking language, as a string.

#### Discussion

The result string specifies the language using the language and regional designations described in [`NSLocale`](../../Foundation/nslocale.md).

## See Also

### Configuring Spell Checkers Languages
- [var availableLanguages: [String]](./availablelanguages.md)
  Provides a list of all available languages.
- [var userPreferredLanguages: [String]](./userpreferredlanguages.md)
  Provides a subset of the available languages to be used for spell checking.
- [var automaticallyIdentifiesLanguages: Bool](./automaticallyidentifieslanguages.md)
  Sets whether the spell checker will automatically identify languages.
- [func setLanguage(String) -> Bool](./setlanguage%28_%29.md)
  Returns whether the specified language is in the Spelling pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/language())*