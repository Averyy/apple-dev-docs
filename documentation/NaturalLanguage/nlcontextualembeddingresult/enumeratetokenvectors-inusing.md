# enumerateTokenVectors(in:using:)

**Framework**: Natural Language  
**Kind**: method

Iterates over the embedding vectors for the range you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@nonobjc
func enumerateTokenVectors(in range: Range<String.Index>, using block: ([Double], Range<String.Index>) -> Bool)
```

## Parameters

- `range`: The range in the string to enumerate.
- `block`: A block that contains the token vectors and the token’s range.

## See Also

- [func tokenVector(at: String.Index) -> ([Double], Range<String.Index>)?](nlcontextualembeddingresult/tokenvector(at:).md)
  Gets a token vector at the index you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingresult/enumeratetokenvectors(in:using:))*