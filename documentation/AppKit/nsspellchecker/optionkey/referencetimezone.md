# referenceTimeZone

**Framework**: AppKit  
**Kind**: property

An NSTimeZone to be associated with the document, used as a reference for dates without time zones; if not specified, the current time zone will be used.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let referenceTimeZone: NSSpellChecker.OptionKey
```

## See Also

- [static let documentAuthor: NSSpellChecker.OptionKey](nsspellchecker/optionkey/documentauthor.md)
  An NSString containing the name of an author to be associated with the document
- [static let documentTitle: NSSpellChecker.OptionKey](nsspellchecker/optionkey/documenttitle.md)
  An NSString containing the title to be associated with the document.
- [static let documentURL: NSSpellChecker.OptionKey](nsspellchecker/optionkey/documenturl.md)
  An NSURL to be associated with the document.
- [static let orthography: NSSpellChecker.OptionKey](nsspellchecker/optionkey/orthography.md)
  An [`NSOrthography`](https://developer.apple.com/documentation/Foundation/NSOrthography) instance indicating an orthography to be used as a starting point for orthography checking, or as the orthography if orthography checking is not enabled.
- [static let quotes: NSSpellChecker.OptionKey](nsspellchecker/optionkey/quotes.md)
  An NSArray containing four strings to be used with doc://com.apple.documentation/documentation/foundation/nstextcheckingresult/checkingtype/1411424-quote (opening double quote, closing double quote, opening single quote, and closing single quote in that order); if not specified, values will be taken from user’s preferences.
- [static let referenceDate: NSSpellChecker.OptionKey](nsspellchecker/optionkey/referencedate.md)
  An NSDate to be associated with the document, used as a referent for relative dates; if not specified, the current date will be used.
- [static let regularExpressions: NSSpellChecker.OptionKey](nsspellchecker/optionkey/regularexpressions.md)
- [static let replacements: NSSpellChecker.OptionKey](nsspellchecker/optionkey/replacements.md)
  An NSDictionary containing replacements to be used with NSTextCheckingTypeReplacement; if not specified, values will be taken from user’s preferences.
- [static let selectedRange: NSSpellChecker.OptionKey](nsspellchecker/optionkey/selectedrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/optionkey/referencetimezone)*