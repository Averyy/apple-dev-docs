# kCFStringTokenizerUnitParagraph

**Framework**: Core Foundation  
**Kind**: var

Specifies that a string should be tokenized by paragraph. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is ignored.

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
var kCFStringTokenizerUnitParagraph: CFOptionFlags { get }
```

## See Also

- [var kCFStringTokenizerUnitWord: CFOptionFlags](kcfstringtokenizerunitword.md)
  Specifies that a string should be tokenized by word. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is ignored.
- [var kCFStringTokenizerUnitSentence: CFOptionFlags](kcfstringtokenizerunitsentence.md)
  Specifies that a string should be tokenized by sentence. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is ignored.
- [var kCFStringTokenizerUnitLineBreak: CFOptionFlags](kcfstringtokenizerunitlinebreak.md)
  Specifies that a string should be tokenized by line break. The `locale` parameter of [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) is ignored.
- [var kCFStringTokenizerUnitWordBoundary: CFOptionFlags](kcfstringtokenizerunitwordboundary.md)
  Specifies that a string should be tokenized by locale-sensitive word boundary.
- [var kCFStringTokenizerAttributeLatinTranscription: CFOptionFlags](kcfstringtokenizerattributelatintranscription.md)
  Used with `kCFStringTokenizerUnitWord`, tells the tokenizer to prepare the Latin transcription when it tokenizes the string.
- [var kCFStringTokenizerAttributeLanguage: CFOptionFlags](kcfstringtokenizerattributelanguage.md)
  Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerunitparagraph)*