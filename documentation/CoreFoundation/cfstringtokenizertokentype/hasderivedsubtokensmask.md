# hasDerivedSubTokensMask

**Framework**: Core Foundation  
**Kind**: property

Compound token which may contain derived subtokens.

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
static var hasDerivedSubTokensMask: CFStringTokenizerTokenType { get }
```

#### Discussion

You can obtain subtokens and derived subtokens by calling [`CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)`](cfstringtokenizergetcurrentsubtokens(_:_:_:_:).md).

## See Also

- [static var normal: CFStringTokenizerTokenType](cfstringtokenizertokentype/normal.md)
  Has a normal token.
- [static var hasSubTokensMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hassubtokensmask.md)
  Compound token which may contain subtokens but with no derived subtokens.
- [static var hasHasNumbersMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hashasnumbersmask.md)
  Appears to contain a number.
- [static var hasNonLettersMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hasnonlettersmask.md)
  Contains punctuation, symbols, and so on.
- [static var isCJWordMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/iscjwordmask.md)
  Contains kana and/or ideographs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/hasderivedsubtokensmask)*