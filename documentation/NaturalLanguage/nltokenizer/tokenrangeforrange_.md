# tokenRangeForRange:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Finds the entire range of all tokens contained completely or partially within the specified range.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
- (NSRange) tokenRangeForRange:(NSRange) range;
```

## Return Value

The smallest possible range that contains all of the tokens within the range specified in `range`. This result includes a token’s entire range if any part of that token is included within `range`. If the length of `range` is 0, this return value is equivalent to [`tokenRangeAtIndex:`](./tokenrangeatindex_.md).

## Parameters

- `range`: The range within the string to search for tokens.

## See Also

### Enumerating the tokens
- [- enumerateTokensInRange:usingBlock:](./enumeratetokensinrange_usingblock_.md)
  Enumerates over a given range of the string and calls the specified block for each token.
- [- tokensForRange:](./tokensforrange_.md)
  Tokenizes the string within the provided range.
- [- tokenRangeAtIndex:](./tokenrangeatindex_.md)
  Finds the range of the token at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/tokenrangeforrange:)*