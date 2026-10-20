# NSSpellChecker.OptionKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that define options for text checking.

**Availability**:
- macOS

## Declaration

```swift
struct OptionKey
```

```c
typedef NSString * NSTextCheckingOptionKey;
```

#### Overview

The constants are optional keys that can be used in the options dictionary parameter of the [`check(_:range:types:options:inSpellDocumentWithTag:orthography:wordCount:)`](./check%28_,range,types,options,inspelldocumentwithtag,orthography,wordcount%29.md), [`requestChecking(of:range:types:options:inSpellDocumentWithTag:completionHandler:)`](./requestchecking%28of,range,types,options,inspelldocumentwithtag,completionhandler%29.md), and [`menu(for:string:options:atLocation:in:)`](./menu%28for,string,options,atlocation,in%29.md) methods.

## Topics

### Spell Checker Options
- [static let documentAuthor: NSSpellChecker.OptionKey](./optionkey/documentauthor.md)
  An NSString containing the name of an author to be associated with the document
- [static let documentTitle: NSSpellChecker.OptionKey](./optionkey/documenttitle.md)
  An NSString containing the title to be associated with the document.
- [static let documentURL: NSSpellChecker.OptionKey](./optionkey/documenturl.md)
  An NSURL to be associated with the document.
- [static let orthography: NSSpellChecker.OptionKey](./optionkey/orthography.md)
  An `NSOrthography` instance indicating an orthography to be used as a starting point for orthography checking, or as the orthography if orthography checking is not enabled.
- [static let quotes: NSSpellChecker.OptionKey](./optionkey/quotes.md)
  An `NSArray` containing four strings to be used with `quoteCheckingResult(range:replacementString:)` (opening double quote, closing double quote, opening single quote, and closing single quote in that order).
- [static let referenceDate: NSSpellChecker.OptionKey](./optionkey/referencedate.md)
  An NSDate to be associated with the document, used as a referent for relative dates; if not specified, the current date will be used.
- [static let referenceTimeZone: NSSpellChecker.OptionKey](./optionkey/referencetimezone.md)
  An NSTimeZone to be associated with the document, used as a reference for dates without time zones; if not specified, the current time zone will be used.
- [static let regularExpressions: NSSpellChecker.OptionKey](./optionkey/regularexpressions.md)
- [static let replacements: NSSpellChecker.OptionKey](./optionkey/replacements.md)
  An NSDictionary containing replacements to be used with NSTextCheckingTypeReplacement; if not specified, values will be taken from user’s preferences.
- [static let selectedRange: NSSpellChecker.OptionKey](./optionkey/selectedrange.md)
### Initializers
- [init(rawValue: String)](./optionkey/init%28rawvalue%29.md)
### Getting additional option values
- [static let generateInlinePredictionsKey: NSSpellChecker.OptionKey](./optionkey/generateinlinepredictionskey.md)
- [static let automaticCapitalizationEnabledKey: NSSpellChecker.OptionKey](./optionkey/automaticcapitalizationenabledkey.md)
- [static let waitForAllGrammarCheckingResultsKey: NSSpellChecker.OptionKey](./optionkey/waitforallgrammarcheckingresultskey.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Data Detector Interaction
- [func menu(for: NSTextCheckingResult, string: String, options: [NSSpellChecker.OptionKey : Any]?, atLocation: NSPoint, in: NSView) -> NSMenu?](./menu%28for,string,options,atlocation,in%29.md)
  Provides a menu containing contextual menu items suitable for certain kinds of detected results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/optionkey)*