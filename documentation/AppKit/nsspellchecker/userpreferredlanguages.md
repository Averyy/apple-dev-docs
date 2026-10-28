# userPreferredLanguages

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Provides a subset of the available languages to be used for spell checking.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var userPreferredLanguages: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * userPreferredLanguages;
```

## Return Value

An array containing the user’s preferred languages for spell checking. The order is set in the system preferences.

## Discussion

If [`automaticallyIdentifiesLanguages`](./automaticallyidentifieslanguages.md) is [`true`](../../Swift/true.md), then text checking will automatically use this method as appropriate; otherwise, it will use the language set by [`setLanguage(_:)`](./setlanguage%28_%29.md).

The older [`checkSpelling(of:startingAt:language:wrap:inSpellDocumentWithTag:wordCount:)`](./checkspelling%28of,startingat,language,wrap,inspelldocumentwithtag,wordcount%29.md) and [`checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)`](./checkgrammar%28of,startingat,language,wrap,inspelldocumentwithtag,details%29.md). methods will use the language set by [`setLanguage(_:)`](./setlanguage%28_%29.md), if they are called with a `nil` language argument.

## See Also

### Configuring Spell Checkers Languages
- [var availableLanguages: [String]](./availablelanguages.md)
  Provides a list of all available languages.
- [var automaticallyIdentifiesLanguages: Bool](./automaticallyidentifieslanguages.md)
  Sets whether the spell checker will automatically identify languages.
- [func language() -> String](./language%28%29.md)
  Returns the current language used in spell checking.
- [func setLanguage(String) -> Bool](./setlanguage%28_%29.md)
  Returns whether the specified language is in the Spelling pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/userpreferredlanguages)*