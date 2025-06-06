# CFStringTokenizerAdvanceToNextToken(_:)

**Framework**: Core Foundation  
**Kind**: func

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

#### Return Value

The type of the token if the tokenizer succeeded in finding a token and setting it as current token. Returns `kCFStringTokenizerTokenNone` if the tokenizer failed to find a token. For possible values, see [`CFStringTokenizerTokenType`](cfstringtokenizertokentype.md).

#### Discussion

If there is no preceding call to [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](cfstringtokenizergototokenatindex(_:_:).md) or [`CFStringTokenizerAdvanceToNextToken(_:)`](cfstringtokenizeradvancetonexttoken(_:).md), the function finds the first token in the range specified by the [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md). If there is a preceding, successful, call to [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](cfstringtokenizergototokenatindex(_:_:).md) or [`CFStringTokenizerAdvanceToNextToken(_:)`](cfstringtokenizeradvancetonexttoken(_:).md) and there is a current token, proceeds to the next token. If a token is found, it is set as the current token and the function returns `true`; otherwise the current token is invalidated and the function returns `false`.

You can obtain the range and attribute of the token calling [`CFStringTokenizerGetCurrentTokenRange(_:)`](cfstringtokenizergetcurrenttokenrange(_:).md) and [`CFStringTokenizerCopyCurrentTokenAttribute(_:_:)`](cfstringtokenizercopycurrenttokenattribute(_:_:).md). If the token is a compound (with type `kCFStringTokenizerTokenHasSubTokensMask` or `kCFStringTokenizerTokenHasDerivedSubTokensMask`), you can obtain its subtokens and (or) derived subtokens by calling [`CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)`](cfstringtokenizergetcurrentsubtokens(_:_:_:_:).md).

## Parameters

- `tokenizer`: A CFStringTokenizer object.

## See Also

- [func CFStringTokenizerGoToTokenAtIndex(CFStringTokenizer!, CFIndex) -> CFStringTokenizerTokenType](cfstringtokenizergototokenatindex(_:_:).md)
  Finds a token that includes the character at a given index, and set it as the current token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizeradvancetonexttoken(_:))*