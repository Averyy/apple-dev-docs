# enumerateTokens(in:using:)

**Framework**: Natural Language  
**Kind**: method

Enumerates over a given range of the string and calls the specified block for each token.

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
func enumerateTokens(in range: Range<String.Index>, using block: (Range<String.Index>, NLTokenizer.Attributes) -> Bool)
```

## Parameters

- `range`: The range of the string to tokenize.
- `block`: The closure to call after each token; return false if processing should stop.

## See Also

- [func tokens(for: Range<String.Index>) -> [Range<String.Index>]](nltokenizer/tokens(for:).md)
  Tokenizes the string within the provided range.
- [func tokenRange(at: String.Index) -> Range<String.Index>](nltokenizer/tokenrange(at:).md)
  Finds the range of the token at the given index.
- [func tokenRange(for: Range<String.Index>) -> Range<String.Index>](nltokenizer/tokenrange(for:).md)
  Finds the entire range of all tokens contained completely or partially within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/enumeratetokens(in:using:))*