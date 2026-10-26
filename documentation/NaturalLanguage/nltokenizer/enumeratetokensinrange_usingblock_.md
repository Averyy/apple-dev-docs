# enumerateTokensInRange:usingBlock:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Enumerates over a given range of the string and calls the specified block for each token.

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
- (void) enumerateTokensInRange:(NSRange) range usingBlock:(void (^)(NSRange tokenRange, NLTokenizerAttributes flags, BOOL *stop)) block;
```

## Mentions

- [Tokenizing natural language text](../tokenizing-natural-language-text.md)

## Parameters

- `range`: The range of the string to tokenize.
- `block`: The closure to call after each token; return false if processing should stop.

## See Also

### Enumerating the tokens
- [- tokensForRange:](./tokensforrange_.md)
  Tokenizes the string within the provided range.
- [- tokenRangeAtIndex:](./tokenrangeatindex_.md)
  Finds the range of the token at the given index.
- [- tokenRangeForRange:](./tokenrangeforrange_.md)
  Finds the entire range of all tokens contained completely or partially within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/enumeratetokensinrange:usingblock:)*