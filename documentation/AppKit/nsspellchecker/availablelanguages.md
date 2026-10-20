# availableLanguages

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Provides a list of all available languages.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var availableLanguages: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * availableLanguages;
```

#### Return Value

An array containing all the available spell checking languages. The languages are ordered in the user’s preferred order as set in the system preferences.

#### Discussion

If [`automaticallyIdentifiesLanguages`](./automaticallyidentifieslanguages.md) is [`true`](../../Swift/true.md), then text checking will automatically use this method as appropriate; otherwise, it will use the language set by [`setLanguage(_:)`](./setlanguage%28_%29.md).

The older [`checkSpelling(of:startingAt:language:wrap:inSpellDocumentWithTag:wordCount:)`](./checkspelling%28of,startingat,language,wrap,inspelldocumentwithtag,wordcount%29.md) and [`checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)`](./checkgrammar%28of,startingat,language,wrap,inspelldocumentwithtag,details%29.md). methods will use the language set by [`setLanguage(_:)`](./setlanguage%28_%29.md), if they are called with a `nil` language argument.

## See Also

### Configuring Spell Checkers Languages
- [var userPreferredLanguages: [String]](./userpreferredlanguages.md)
  Provides a subset of the available languages to be used for spell checking.
- [var automaticallyIdentifiesLanguages: Bool](./automaticallyidentifieslanguages.md)
  Sets whether the spell checker will automatically identify languages.
- [func language() -> String](./language%28%29.md)
  Returns the current language used in spell checking.
- [func setLanguage(String) -> Bool](./setlanguage%28_%29.md)
  Returns whether the specified language is in the Spelling pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/availablelanguages)*