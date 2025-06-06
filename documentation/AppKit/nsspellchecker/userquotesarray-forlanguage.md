# userQuotesArray(forLanguage:)

**Framework**: AppKit  
**Kind**: method

Returns the default values for quote replacement.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func userQuotesArray(forLanguage language: String) -> [String]
```

#### Return Value

An array of quote replacements used by the [`quotes`](nsspellchecker/optionkey/quotes.md) key-value pair.

## Parameters

- `language`: The language for quote replacement.

## See Also

- [class func uniqueSpellDocumentTag() -> Int](nsspellchecker/uniquespelldocumenttag.md)
  Returns a guaranteed unique tag to use as the spell-document tag for a document.
- [func closeSpellDocument(withTag: Int)](nsspellchecker/closespelldocument(withtag:).md)
  Notifies the receiver that the user has finished with the tagged document.
- [func ignoreWord(String, inSpellDocumentWithTag: Int)](nsspellchecker/ignoreword(_:inspelldocumentwithtag:).md)
  Instructs the spell checker to ignore all future occurrences of `wordToIgnore` in the document identified by `tag`.
- [func ignoredWords(inSpellDocumentWithTag: Int) -> [String]?](nsspellchecker/ignoredwords(inspelldocumentwithtag:).md)
  Returns the array of ignored words for a document identified by `tag`.
- [func setIgnoredWords([String], inSpellDocumentWithTag: Int)](nsspellchecker/setignoredwords(_:inspelldocumentwithtag:).md)
  Initializes the ignored-words document (a dictionary identified by `tag` with `someWords`), an array of words to ignore.
- [func setWordFieldStringValue(String)](nsspellchecker/setwordfieldstringvalue(_:).md)
  Sets the string that appears in the misspelled word field, using the string object `aString`.
- [func updateSpellingPanel(withMisspelledWord: String)](nsspellchecker/updatespellingpanel(withmisspelledword:).md)
  Causes the spell checker to update the Spelling panel’s misspelled-word field to reflect `word`.
- [func completions(forPartialWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](nsspellchecker/completions(forpartialwordrange:in:language:inspelldocumentwithtag:).md)
  Provides a list of complete words that the user might be trying to type based on a partial word in a given string.
- [func hasLearnedWord(String) -> Bool](nsspellchecker/haslearnedword(_:).md)
  Indicates whether the spell checker has learned a given word.
- [func unlearnWord(String)](nsspellchecker/unlearnword(_:).md)
  Tells the spell checker to unlearn a given word.
- [func learnWord(String)](nsspellchecker/learnword(_:).md)
  Adds the word to the spell checker dictionary.
- [var userReplacementsDictionary: [String : String]](nsspellchecker/userreplacementsdictionary.md)
  Returns the dictionary used when replacing words.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/userquotesarray(forlanguage:))*