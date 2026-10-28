# tokensForRange:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Tokenizes the string within the provided range.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```objc
- (NSArray<NSValue *> *) tokensForRange:(NSRange) range;
```

## Return Value

Returns the ranges corresponding to the tokens for the tokenizer’s unit that intersect the given range.

## Parameters

- `range`: The range within the string that should be tokenzied.

## See Also

### Enumerating the tokens
- [- enumerateTokensInRange:usingBlock:](./enumeratetokensinrange_usingblock_.md)
  Enumerates over a given range of the string and calls the specified block for each token.
- [- tokenRangeAtIndex:](./tokenrangeatindex_.md)
  Finds the range of the token at the given index.
- [- tokenRangeForRange:](./tokenrangeforrange_.md)
  Finds the entire range of all tokens contained completely or partially within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/tokensforrange:)*