# kCFStringTokenizerAttributeLanguage

**Framework**: Core Foundation  
**Kind**: var  
**Role**: Global Variable

Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var kCFStringTokenizerAttributeLanguage: CFOptionFlags { get }
```

```c
kCFStringTokenizerAttributeLanguage
```

#### Discussion

Used with [`kCFStringTokenizerUnitSentence`](./kcfstringtokenizerunitsentence.md) or [`kCFStringTokenizerUnitParagraph`](./kcfstringtokenizerunitparagraph.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerattributelanguage)*