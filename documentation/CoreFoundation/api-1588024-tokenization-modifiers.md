# Tokenization Modifiers

**Framework**: Core Foundation  
**Role**: API Collection

Tokenization options are used with [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md) to specify how the string should be tokenized

#### Overview

You use the tokenization unit options with [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md) to specify how a string should be tokenized.

You use the modifiers together with a tokenization unit to modify the way the string is tokenized.

You use the attribute specifiers to tell the tokenizer to prepare the specified attribute when it tokenizes the given string. You can retrieve the attribute value by calling [`CFStringTokenizerCopyCurrentTokenAttribute(_:_:)`](./cfstringtokenizercopycurrenttokenattribute%28_,_%29.md) with one of the attribute options.

The locale sensitivity of the tokenization unit options may change in a future release.

## Topics

### Constants
- [var kCFStringTokenizerUnitWord: CFOptionFlags](./kcfstringtokenizerunitword.md)
  Specifies that a string should be tokenized by word. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md) is ignored.
- [var kCFStringTokenizerUnitSentence: CFOptionFlags](./kcfstringtokenizerunitsentence.md)
  Specifies that a string should be tokenized by sentence. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md) is ignored.
- [var kCFStringTokenizerUnitParagraph: CFOptionFlags](./kcfstringtokenizerunitparagraph.md)
  Specifies that a string should be tokenized by paragraph. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md) is ignored.
- [var kCFStringTokenizerUnitLineBreak: CFOptionFlags](./kcfstringtokenizerunitlinebreak.md)
  Specifies that a string should be tokenized by line break. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md) is ignored.
- [var kCFStringTokenizerUnitWordBoundary: CFOptionFlags](./kcfstringtokenizerunitwordboundary.md)
  Specifies that a string should be tokenized by locale-sensitive word boundary.
- [var kCFStringTokenizerAttributeLatinTranscription: CFOptionFlags](./kcfstringtokenizerattributelatintranscription.md)
  Used with `kCFStringTokenizerUnitWord`, tells the tokenizer to prepare the Latin transcription when it tokenizes the string.
- [var kCFStringTokenizerAttributeLanguage: CFOptionFlags](./kcfstringtokenizerattributelanguage.md)
  Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.

## See Also

### Constants
- [struct CFStringTokenizerTokenType](./cfstringtokenizertokentype.md)
  Token types returned by [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](./cfstringtokenizergototokenatindex%28_,_%29.md) and [`CFStringTokenizerAdvanceToNextToken(_:)`](./cfstringtokenizeradvancetonexttoken%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/1588024-tokenization-modifiers)*