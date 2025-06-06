# completions(forPartialWordRange:in:language:inSpellDocumentWithTag:)

**Framework**: AppKit  
**Kind**: method

Provides a list of complete words that the user might be trying to type based on a partial word in a given string.

**Availability**:
- macOS ?+

## Declaration

```swift
func completions(forPartialWordRange range: NSRange, in string: String, language: String?, inSpellDocumentWithTag tag: Int) -> [String]?
```

#### Return Value

List of complete words from the spell checker dictionary in the order they should be presented to the user.

## Parameters

- `range`: Range that identifies a partial word in  .
- `string`: String with the partial word from which to generate the result.
- `language`: Language to used in  . When  , this method uses the language selected in the Spelling panel.
- `tag`: Identifies the spell document with ignored words to use.

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
- [func hasLearnedWord(String) -> Bool](nsspellchecker/haslearnedword(_:).md)
  Indicates whether the spell checker has learned a given word.
- [func unlearnWord(String)](nsspellchecker/unlearnword(_:).md)
  Tells the spell checker to unlearn a given word.
- [func learnWord(String)](nsspellchecker/learnword(_:).md)
  Adds the word to the spell checker dictionary.
- [func userQuotesArray(forLanguage: String) -> [String]](nsspellchecker/userquotesarray(forlanguage:).md)
  Returns the default values for quote replacement.
- [var userReplacementsDictionary: [String : String]](nsspellchecker/userreplacementsdictionary.md)
  Returns the dictionary used when replacing words.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/completions(forpartialwordrange:in:language:inspelldocumentwithtag:))*