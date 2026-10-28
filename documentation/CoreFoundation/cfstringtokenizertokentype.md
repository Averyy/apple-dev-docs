# CFStringTokenizerTokenType

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Token types returned by [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](./cfstringtokenizergototokenatindex%28_,_%29.md) and [`CFStringTokenizerAdvanceToNextToken(_:)`](./cfstringtokenizeradvancetonexttoken%28_%29.md).

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
struct CFStringTokenizerTokenType
```

```c
enum CFStringTokenizerTokenType : CFOptionFlags;
```

## Overview

See [http://www.unicode.org/reports/tr29/#Word_Boundaries](http://www.unicode.org/reports/tr29/#Word_Boundaries) for a detailed description of word boundaries.

## Topics

### Constants
- [static var normal: CFStringTokenizerTokenType](./cfstringtokenizertokentype/normal.md)
  Has a normal token.
- [static var hasSubTokensMask: CFStringTokenizerTokenType](./cfstringtokenizertokentype/hassubtokensmask.md)
  Compound token which may contain subtokens but with no derived subtokens.
- [static var hasDerivedSubTokensMask: CFStringTokenizerTokenType](./cfstringtokenizertokentype/hasderivedsubtokensmask.md)
  Compound token which may contain derived subtokens.
- [static var hasHasNumbersMask: CFStringTokenizerTokenType](./cfstringtokenizertokentype/hashasnumbersmask.md)
  Appears to contain a number.
- [static var hasNonLettersMask: CFStringTokenizerTokenType](./cfstringtokenizertokentype/hasnonlettersmask.md)
  Contains punctuation, symbols, and so on.
- [static var isCJWordMask: CFStringTokenizerTokenType](./cfstringtokenizertokentype/iscjwordmask.md)
  Contains kana and/or ideographs.
- [kCFStringTokenizerTokenNone](./cfstringtokenizertokentype/kcfstringtokenizertokennone.md)
  Has no token.
### Initializers
- [init(rawValue: CFOptionFlags)](./cfstringtokenizertokentype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [Tokenization Modifiers](./api-1588024-tokenization-modifiers.md)
  Tokenization options are used with [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md) to specify how the string should be tokenized


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype)*