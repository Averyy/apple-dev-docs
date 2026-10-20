# hasSubTokensMask

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Compound token which may contain subtokens but with no derived subtokens.

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
static var hasSubTokensMask: CFStringTokenizerTokenType { get }
```

```c
kCFStringTokenizerTokenHasSubTokensMask
```

#### Discussion

You can obtain subtokens by calling [`CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)`](../cfstringtokenizergetcurrentsubtokens%28_,_,_,_%29.md).

## See Also

### Constants
- [static var normal: CFStringTokenizerTokenType](./normal.md)
  Has a normal token.
- [static var hasDerivedSubTokensMask: CFStringTokenizerTokenType](./hasderivedsubtokensmask.md)
  Compound token which may contain derived subtokens.
- [static var hasHasNumbersMask: CFStringTokenizerTokenType](./hashasnumbersmask.md)
  Appears to contain a number.
- [static var hasNonLettersMask: CFStringTokenizerTokenType](./hasnonlettersmask.md)
  Contains punctuation, symbols, and so on.
- [static var isCJWordMask: CFStringTokenizerTokenType](./iscjwordmask.md)
  Contains kana and/or ideographs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/hassubtokensmask)*