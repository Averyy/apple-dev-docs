# tokenRange(for:)

**Framework**: Natural Language  
**Kind**: method

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

```swift
@nonobjc
func tokenRange(for range: Range<String.Index>) -> Range<String.Index>
```

#### Return Value

The smallest possible range that contains all of the tokens within the range specified in `range`. This result includes a token’s entire range if any part of that token is included within `range`. If the length of `range` is 0, this return value is equivalent to [`tokenRange(at:)`](nltokenizer/tokenrange(at:).md).

## Parameters

- `range`: The range within the string to search for tokens.

## See Also

- [func enumerateTokens(in: Range<String.Index>, using: (Range<String.Index>, NLTokenizer.Attributes) -> Bool)](nltokenizer/enumeratetokens(in:using:).md)
  Enumerates over a given range of the string and calls the specified block for each token.
- [func tokens(for: Range<String.Index>) -> [Range<String.Index>]](nltokenizer/tokens(for:).md)
  Tokenizes the string within the provided range.
- [func tokenRange(at: String.Index) -> Range<String.Index>](nltokenizer/tokenrange(at:).md)
  Finds the range of the token at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/tokenrange(for:))*