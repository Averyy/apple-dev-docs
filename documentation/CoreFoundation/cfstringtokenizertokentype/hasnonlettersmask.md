# hasNonLettersMask

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Contains punctuation, symbols, and so on.

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
static var hasNonLettersMask: CFStringTokenizerTokenType { get }
```

```c
kCFStringTokenizerTokenHasNonLettersMask
```

#### Discussion

Given the way Unicode word break works, this means it is a standalone punctuation or symbol character, or a string of such.

## See Also

### Constants
- [static var normal: CFStringTokenizerTokenType](./normal.md)
  Has a normal token.
- [static var hasSubTokensMask: CFStringTokenizerTokenType](./hassubtokensmask.md)
  Compound token which may contain subtokens but with no derived subtokens.
- [static var hasDerivedSubTokensMask: CFStringTokenizerTokenType](./hasderivedsubtokensmask.md)
  Compound token which may contain derived subtokens.
- [static var hasHasNumbersMask: CFStringTokenizerTokenType](./hashasnumbersmask.md)
  Appears to contain a number.
- [static var isCJWordMask: CFStringTokenizerTokenType](./iscjwordmask.md)
  Contains kana and/or ideographs.
- [kCFStringTokenizerTokenNone](./kcfstringtokenizertokennone.md)
  Has no token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/hasnonlettersmask)*