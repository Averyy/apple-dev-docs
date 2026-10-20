# automaticallyIdentifiesLanguages

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets whether the spell checker will automatically identify languages.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var automaticallyIdentifiesLanguages: Bool { get set }
```

```objc
@property BOOL automaticallyIdentifiesLanguages;
```

## Parameters

- `flag`: [`true`](../../Swift/true.md) if languages should be automatically identified, otherwise [`false`](../../Swift/false.md).

## See Also

### Configuring Spell Checkers Languages
- [var availableLanguages: [String]](./availablelanguages.md)
  Provides a list of all available languages.
- [var userPreferredLanguages: [String]](./userpreferredlanguages.md)
  Provides a subset of the available languages to be used for spell checking.
- [func language() -> String](./language%28%29.md)
  Returns the current language used in spell checking.
- [func setLanguage(String) -> Bool](./setlanguage%28_%29.md)
  Returns whether the specified language is in the Spelling pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/automaticallyidentifieslanguages)*