# NSSpellChecker.OptionKey

**Framework**: AppKit  
**Kind**: struct

Constants that define options for text checking.

**Availability**:
- macOS ?+

## Declaration

```swift
struct OptionKey
```

#### Overview

The constants are optional keys that can be used in the options dictionary parameter of the [`check(_:range:types:options:inSpellDocumentWithTag:orthography:wordCount:)`](nsspellchecker/check(_:range:types:options:inspelldocumentwithtag:orthography:wordcount:).md), [`requestChecking(of:range:types:options:inSpellDocumentWithTag:completionHandler:)`](nsspellchecker/requestchecking(of:range:types:options:inspelldocumentwithtag:completionhandler:).md), and [`menu(for:string:options:atLocation:in:)`](nsspellchecker/menu(for:string:options:atlocation:in:).md) methods.

## Topics

### Spell Checker Options
- [static let documentAuthor: NSSpellChecker.OptionKey](nsspellchecker/optionkey/documentauthor.md)
  An NSString containing the name of an author to be associated with the document
- [static let documentTitle: NSSpellChecker.OptionKey](nsspellchecker/optionkey/documenttitle.md)
  An NSString containing the title to be associated with the document.
- [static let documentURL: NSSpellChecker.OptionKey](nsspellchecker/optionkey/documenturl.md)
  An NSURL to be associated with the document.
- [static let orthography: NSSpellChecker.OptionKey](nsspellchecker/optionkey/orthography.md)
  An `NSOrthography` instance indicating an orthography to be used as a starting point for orthography checking, or as the orthography if orthography checking is not enabled.
- [static let quotes: NSSpellChecker.OptionKey](nsspellchecker/optionkey/quotes.md)
  An `NSArray` containing four strings to be used with `quoteCheckingResult(range:replacementString:)` (opening double quote, closing double quote, opening single quote, and closing single quote in that order).
- [static let referenceDate: NSSpellChecker.OptionKey](nsspellchecker/optionkey/referencedate.md)
  An NSDate to be associated with the document, used as a referent for relative dates; if not specified, the current date will be used.
- [static let referenceTimeZone: NSSpellChecker.OptionKey](nsspellchecker/optionkey/referencetimezone.md)
  An NSTimeZone to be associated with the document, used as a reference for dates without time zones; if not specified, the current time zone will be used.
- [static let regularExpressions: NSSpellChecker.OptionKey](nsspellchecker/optionkey/regularexpressions.md)
- [static let replacements: NSSpellChecker.OptionKey](nsspellchecker/optionkey/replacements.md)
  An NSDictionary containing replacements to be used with NSTextCheckingTypeReplacement; if not specified, values will be taken from user’s preferences.
- [static let selectedRange: NSSpellChecker.OptionKey](nsspellchecker/optionkey/selectedrange.md)
### Initializers
- [init(rawValue: String)](nsspellchecker/optionkey/init(rawvalue:).md)
### Type Properties
- [static let generateInlinePredictionsKey: NSSpellChecker.OptionKey](nsspellchecker/optionkey/generateinlinepredictionskey.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func menu(for: NSTextCheckingResult, string: String, options: [NSSpellChecker.OptionKey : Any]?, atLocation: NSPoint, in: NSView) -> NSMenu?](nsspellchecker/menu(for:string:options:atlocation:in:).md)
  Provides a menu containing contextual menu items suitable for certain kinds of detected results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/optionkey)*