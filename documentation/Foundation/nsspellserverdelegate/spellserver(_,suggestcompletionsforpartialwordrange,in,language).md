# spellServer(_:suggestCompletionsForPartialWordRange:in:language:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
optional func spellServer(_ sender: NSSpellServer, suggestCompletionsForPartialWordRange range: NSRange, in string: String, language: String) -> [String]?
```

```objc
- (NSArray<NSString *> *) spellServer:(NSSpellServer *) sender suggestCompletionsForPartialWordRange:(NSRange) range inString:(NSString *) string language:(NSString *) language;
```

#### Return Value

An array of `NSString` objects indicating possible completions.

## Parameters

- `sender`: The `NSSpellServer` object that sent this message.
- `range`: The range of the partially completed word.
- `string`: The string containing the partial word range.
- `language`: The language to use for the completion.

## See Also

### Related Documentation
- [func completions(forPartialWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](../../AppKit/nsspellchecker/completions%28forpartialwordrange,in,language,inspelldocumentwithtag%29.md)
  Provides a list of complete words that the user might be trying to type based on a partial word in a given string.
### Managing the Spelling Dictionary
- [func spellServer(NSSpellServer, didForgetWord: String, inLanguage: String)](./spellserver%28_,didforgetword,inlanguage%29.md)
  Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.
- [func spellServer(NSSpellServer, didLearnWord: String, inLanguage: String)](./spellserver%28_,didlearnword,inlanguage%29.md)
  Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.
- [func spellServer(NSSpellServer, recordResponse: Int, toCorrection: String, forWord: String, language: String)](./spellserver%28_,recordresponse,tocorrection,forword,language%29.md)
  Notifies the spell checker of the users’s response to a correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:suggestcompletionsforpartialwordrange:in:language:))*