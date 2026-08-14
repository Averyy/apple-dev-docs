# userPreferredLanguages

**Framework**: AppKit  
**Kind**: property

Provides a subset of the available languages to be used for spell checking.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var userPreferredLanguages: [String] { get }
```

#### Return Value

An array containing the user’s preferred languages for spell checking. The order is set in the system preferences.

#### Discussion

If [`automaticallyIdentifiesLanguages`](nsspellchecker/automaticallyidentifieslanguages.md) is [`true`](https://developer.apple.com/documentation/swift/true), then text checking will automatically use this method as appropriate; otherwise, it will use the language set by [`setLanguage(_:)`](nsspellchecker/setlanguage(_:).md).

The older [`checkSpelling(of:startingAt:language:wrap:inSpellDocumentWithTag:wordCount:)`](nsspellchecker/checkspelling(of:startingat:language:wrap:inspelldocumentwithtag:wordcount:).md) and [`checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)`](nsspellchecker/checkgrammar(of:startingat:language:wrap:inspelldocumentwithtag:details:).md). methods will use the language set by [`setLanguage(_:)`](nsspellchecker/setlanguage(_:).md), if they are called with a `nil` language argument.

## See Also

- [var availableLanguages: [String]](nsspellchecker/availablelanguages.md)
  Provides a list of all available languages.
- [var automaticallyIdentifiesLanguages: Bool](nsspellchecker/automaticallyidentifieslanguages.md)
  Sets whether the spell checker will automatically identify languages.
- [func language() -> String](nsspellchecker/language.md)
  Returns the current language used in spell checking.
- [func setLanguage(String) -> Bool](nsspellchecker/setlanguage(_:).md)
  Returns whether the specified language is in the Spelling pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/userpreferredlanguages)*