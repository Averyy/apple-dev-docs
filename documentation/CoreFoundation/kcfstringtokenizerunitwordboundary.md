# kCFStringTokenizerUnitWordBoundary

**Framework**: Core Foundation  
**Kind**: var

Specifies that a string should be tokenized by locale-sensitive word boundary.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kCFStringTokenizerUnitWordBoundary: CFOptionFlags { get }
```

#### Discussion

You can use this constant in double-click range detection and whole word search. It is locale-sensitive. If the locale is `en_US_POSIX`, a colon (U+003A) is treated as a word separator. If the `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is `NULL`, the locale from the global `AppleTextBreakLocale` preference is used if it is available; otherwise the locale defaults to the first locale in `AppleLanguages`.

`kCFStringTokenizerUnitWordBoundary` also returns space between words as a token.

## See Also

- [var kCFStringTokenizerUnitWord: CFOptionFlags](kcfstringtokenizerunitword.md)
  Specifies that a string should be tokenized by word. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is ignored.
- [var kCFStringTokenizerUnitSentence: CFOptionFlags](kcfstringtokenizerunitsentence.md)
  Specifies that a string should be tokenized by sentence. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is ignored.
- [var kCFStringTokenizerUnitParagraph: CFOptionFlags](kcfstringtokenizerunitparagraph.md)
  Specifies that a string should be tokenized by paragraph. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is ignored.
- [var kCFStringTokenizerUnitLineBreak: CFOptionFlags](kcfstringtokenizerunitlinebreak.md)
  Specifies that a string should be tokenized by line break. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is ignored.
- [var kCFStringTokenizerAttributeLatinTranscription: CFOptionFlags](kcfstringtokenizerattributelatintranscription.md)
  Used with `kCFStringTokenizerUnitWord`, tells the tokenizer to prepare the Latin transcription when it tokenizes the string.
- [var kCFStringTokenizerAttributeLanguage: CFOptionFlags](kcfstringtokenizerattributelanguage.md)
  Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerunitwordboundary)*