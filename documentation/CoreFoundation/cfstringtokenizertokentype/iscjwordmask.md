# isCJWordMask

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Contains kana and/or ideographs.

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
static var isCJWordMask: CFStringTokenizerTokenType { get }
```

```c
kCFStringTokenizerTokenIsCJWordMask
```

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
- [static var hasNonLettersMask: CFStringTokenizerTokenType](./hasnonlettersmask.md)
  Contains punctuation, symbols, and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/iscjwordmask)*