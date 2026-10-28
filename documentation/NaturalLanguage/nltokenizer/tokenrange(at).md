# tokenRange(at:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Finds the range of the token at the given index.

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
func tokenRange(at index: String.Index) -> Range<String.Index>
```

## Return Value

The range of the token at the given location.

## Parameters

- `index`: The location in the string that is of interest.

## See Also

### Enumerating the tokens
- [func enumerateTokens(in: Range<String.Index>, using: (Range<String.Index>, NLTokenizer.Attributes) -> Bool)](./enumeratetokens%28in,using%29.md)
  Enumerates over a given range of the string and calls the specified block for each token.
- [func tokens(for: Range<String.Index>) -> [Range<String.Index>]](./tokens%28for%29.md)
  Tokenizes the string within the provided range.
- [func tokenRange(for: Range<String.Index>) -> Range<String.Index>](./tokenrange%28for%29.md)
  Finds the entire range of all tokens contained completely or partially within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenizer/tokenrange(at:))*