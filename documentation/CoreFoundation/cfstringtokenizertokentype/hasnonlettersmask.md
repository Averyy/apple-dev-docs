# hasNonLettersMask

**Framework**: Core Foundation  
**Kind**: property

Contains punctuation, symbols, and so on.

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
static var hasNonLettersMask: CFStringTokenizerTokenType { get }
```

#### Discussion

Given the way Unicode word break works, this means it is a standalone punctuation or symbol character, or a string of such.

## See Also

- [static var normal: CFStringTokenizerTokenType](cfstringtokenizertokentype/normal.md)
  Has a normal token.
- [static var hasSubTokensMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hassubtokensmask.md)
  Compound token which may contain subtokens but with no derived subtokens.
- [static var hasDerivedSubTokensMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hasderivedsubtokensmask.md)
  Compound token which may contain derived subtokens.
- [static var hasHasNumbersMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hashasnumbersmask.md)
  Appears to contain a number.
- [static var isCJWordMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/iscjwordmask.md)
  Contains kana and/or ideographs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/hasnonlettersmask)*