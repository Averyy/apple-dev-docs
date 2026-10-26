# userQuotesArray(forLanguage:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the default values for quote replacement.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func userQuotesArray(forLanguage language: String) -> [String]
```

```objc
- (NSArray<NSString *> *) userQuotesArrayForLanguage:(NSString *) language;
```

#### Return Value

An array of quote replacements used by the [`quotes`](./optionkey/quotes.md) key-value pair.

## Parameters

- `language`: The language for quote replacement.

## See Also

### Managing the Spell-Checking Process
- [class func uniqueSpellDocumentTag() -> Int](./uniquespelldocumenttag%28%29.md)
  Returns a guaranteed unique tag to use as the spell-document tag for a document.
- [func closeSpellDocument(withTag: Int)](./closespelldocument%28withtag%29.md)
  Notifies the receiver that the user has finished with the tagged document.
- [func ignoreWord(String, inSpellDocumentWithTag: Int)](./ignoreword%28_,inspelldocumentwithtag%29.md)
  Instructs the spell checker to ignore all future occurrences of `wordToIgnore` in the document identified by `tag`.
- [func ignoredWords(inSpellDocumentWithTag: Int) -> [String]?](./ignoredwords%28inspelldocumentwithtag%29.md)
  Returns the array of ignored words for a document identified by `tag`.
- [func setIgnoredWords([String], inSpellDocumentWithTag: Int)](./setignoredwords%28_,inspelldocumentwithtag%29.md)
  Initializes the ignored-words document (a dictionary identified by `tag` with `someWords`), an array of words to ignore.
- [func setWordFieldStringValue(String)](./setwordfieldstringvalue%28_%29.md)
  Sets the string that appears in the misspelled word field, using the string object `aString`.
- [func updateSpellingPanel(withMisspelledWord: String)](./updatespellingpanel%28withmisspelledword%29.md)
  Causes the spell checker to update the Spelling panel’s misspelled-word field to reflect `word`.
- [func completions(forPartialWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](./completions%28forpartialwordrange,in,language,inspelldocumentwithtag%29.md)
  Provides a list of complete words that the user might be trying to type based on a partial word in a given string.
- [func hasLearnedWord(String) -> Bool](./haslearnedword%28_%29.md)
  Indicates whether the spell checker has learned a given word.
- [func unlearnWord(String)](./unlearnword%28_%29.md)
  Tells the spell checker to unlearn a given word.
- [func learnWord(String)](./learnword%28_%29.md)
  Adds the word to the spell checker dictionary.
- [var userReplacementsDictionary: [String : String]](./userreplacementsdictionary.md)
  Returns the dictionary used when replacing words.
- [- forgetWord:](./forgetword_.md)
  Remove this word from the spelling dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/userquotesarray(forlanguage:))*