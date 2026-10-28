# tokens(for:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Tokenizes the string within the provided range.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@nonobjc
func tokens(for range: Range<String.Index>) -> [Range<String.Index>]
```

## Return Value

Returns the ranges corresponding to the tokens for the tokenizer’s unit that intersect the given range.

## Parameters

- `range`: The range within the string that should be tokenzied.

## See Also

### Enumerating the tokens
- [func enumerateTokens(in: Range<String.Index>, using: (Range<String.Index>, NLTokenizer.Attributes) -> Bool)](./enumeratetokens%28in,using%29.md)
  Enumerates over a given range of the string and calls the specified block for each token.
- [func tokenRange(at: String.Index) -> Range<String.Index>](./tokenrange%28at%29.md)
  Finds the range of the token at the given index.
- [func tokenRange(for: Range<String.Index>) -> Range<String.Index>](./tokenrange%28for%29.md)
  Finds the entire range of all tokens contained completely or partially within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/tokens(for:))*