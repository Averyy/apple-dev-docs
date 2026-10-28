# tokenRangeAtIndex:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Finds the range of the token at the given index.

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
- (NSRange) tokenRangeAtIndex:(NSUInteger) characterIndex;
```

## Return Value

The range of the token at the given location.

## Parameters

- `characterIndex`: The location in the string that is of interest.

## See Also

### Enumerating the tokens
- [- enumerateTokensInRange:usingBlock:](./enumeratetokensinrange_usingblock_.md)
  Enumerates over a given range of the string and calls the specified block for each token.
- [- tokensForRange:](./tokensforrange_.md)
  Tokenizes the string within the provided range.
- [- tokenRangeForRange:](./tokenrangeforrange_.md)
  Finds the entire range of all tokens contained completely or partially within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/tokenrangeatindex:)*