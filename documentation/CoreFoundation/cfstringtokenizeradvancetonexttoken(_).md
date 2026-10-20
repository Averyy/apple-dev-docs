# CFStringTokenizerAdvanceToNextToken(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Advances the tokenizer to the next token and sets that as the current token.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFStringTokenizerAdvanceToNextToken(_ tokenizer: CFStringTokenizer!) -> CFStringTokenizerTokenType
```

```c
extern CFStringTokenizerTokenType CFStringTokenizerAdvanceToNextToken(CFStringTokenizerRef tokenizer);
```

#### Return Value

The type of the token if the tokenizer succeeded in finding a token and setting it as current token. Returns `kCFStringTokenizerTokenNone` if the tokenizer failed to find a token. For possible values, see [`CFStringTokenizerTokenType`](./cfstringtokenizertokentype.md).

#### Discussion

If there is no preceding call to [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](./cfstringtokenizergototokenatindex%28_,_%29.md) or [`CFStringTokenizerAdvanceToNextToken(_:)`](./cfstringtokenizeradvancetonexttoken%28_%29.md), the function finds the first token in the range specified by the [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md). If there is a preceding, successful, call to [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](./cfstringtokenizergototokenatindex%28_,_%29.md) or [`CFStringTokenizerAdvanceToNextToken(_:)`](./cfstringtokenizeradvancetonexttoken%28_%29.md) and there is a current token, proceeds to the next token. If a token is found, it is set as the current token and the function returns `true`; otherwise the current token is invalidated and the function returns `false`.

You can obtain the range and attribute of the token calling [`CFStringTokenizerGetCurrentTokenRange(_:)`](./cfstringtokenizergetcurrenttokenrange%28_%29.md) and [`CFStringTokenizerCopyCurrentTokenAttribute(_:_:)`](./cfstringtokenizercopycurrenttokenattribute%28_,_%29.md). If the token is a compound (with type `kCFStringTokenizerTokenHasSubTokensMask` or `kCFStringTokenizerTokenHasDerivedSubTokensMask`), you can obtain its subtokens and (or) derived subtokens by calling [`CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)`](./cfstringtokenizergetcurrentsubtokens%28_,_,_,_%29.md).

## Parameters

- `tokenizer`: A CFStringTokenizer object.

## See Also

### Changing the Location
- [func CFStringTokenizerGoToTokenAtIndex(CFStringTokenizer!, CFIndex) -> CFStringTokenizerTokenType](./cfstringtokenizergototokenatindex%28_,_%29.md)
  Finds a token that includes the character at a given index, and set it as the current token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizeradvancetonexttoken(_:))*