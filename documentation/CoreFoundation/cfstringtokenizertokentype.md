# CFStringTokenizerTokenType

**Framework**: Core Foundation  
**Kind**: struct

Token types returned by [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](cfstringtokenizergototokenatindex(_:_:).md) and [`CFStringTokenizerAdvanceToNextToken(_:)`](cfstringtokenizeradvancetonexttoken(_:).md).

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
struct CFStringTokenizerTokenType
```

#### Overview

See [`http://www.unicode.org/reports/tr29/#Word_Boundaries`](https://developer.apple.comhttp://www.unicode.org/reports/tr29/#Word_Boundaries) for a detailed description of word boundaries.

## Topics

### Constants
- [static var normal: CFStringTokenizerTokenType](cfstringtokenizertokentype/normal.md)
  Has a normal token.
- [static var hasSubTokensMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hassubtokensmask.md)
  Compound token which may contain subtokens but with no derived subtokens.
- [static var hasDerivedSubTokensMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hasderivedsubtokensmask.md)
  Compound token which may contain derived subtokens.
- [static var hasHasNumbersMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hashasnumbersmask.md)
  Appears to contain a number.
- [static var hasNonLettersMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/hasnonlettersmask.md)
  Contains punctuation, symbols, and so on.
- [static var isCJWordMask: CFStringTokenizerTokenType](cfstringtokenizertokentype/iscjwordmask.md)
  Contains kana and/or ideographs.
### Initializers
- [init(rawValue: CFOptionFlags)](cfstringtokenizertokentype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Tokenization Modifiers](1588024-tokenization-modifiers.md)
  Tokenization options are used with [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) to specify how the string should be tokenized


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype)*