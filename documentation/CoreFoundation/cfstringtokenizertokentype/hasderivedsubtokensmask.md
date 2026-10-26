# hasDerivedSubTokensMask

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Compound token which may contain derived subtokens.

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
static var hasDerivedSubTokensMask: CFStringTokenizerTokenType { get }
```

```c
kCFStringTokenizerTokenHasDerivedSubTokensMask
```

#### Discussion

You can obtain subtokens and derived subtokens by calling [`CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)`](../cfstringtokenizergetcurrentsubtokens%28_,_,_,_%29.md).

## See Also

### Constants
- [static var normal: CFStringTokenizerTokenType](./normal.md)
  Has a normal token.
- [static var hasSubTokensMask: CFStringTokenizerTokenType](./hassubtokensmask.md)
  Compound token which may contain subtokens but with no derived subtokens.
- [static var hasHasNumbersMask: CFStringTokenizerTokenType](./hashasnumbersmask.md)
  Appears to contain a number.
- [static var hasNonLettersMask: CFStringTokenizerTokenType](./hasnonlettersmask.md)
  Contains punctuation, symbols, and so on.
- [static var isCJWordMask: CFStringTokenizerTokenType](./iscjwordmask.md)
  Contains kana and/or ideographs.
- [kCFStringTokenizerTokenNone](./kcfstringtokenizertokennone.md)
  Has no token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/hasderivedsubtokensmask)*