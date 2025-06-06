# tokenVector(at:)

**Framework**: Natural Language  
**Kind**: method

Gets a token vector at the index you specify.

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
func tokenVector(at index: String.Index) -> ([Double], Range<String.Index>)?
```

## Parameters

- `index`: The index to get the token vector at.

## See Also

- [func enumerateTokenVectors(in: Range<String.Index>, using: ([Double], Range<String.Index>) -> Bool)](nlcontextualembeddingresult/enumeratetokenvectors(in:using:).md)
  Iterates over the embedding vectors for the range you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingresult/tokenvector(at:))*