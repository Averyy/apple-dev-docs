# replaceCharacters(in:with:)

**Framework**: AppKit  
**Kind**: method

Replaces the text in the specified range with the new string.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func replaceCharacters(in range: NSRange, with string: String)
```

#### Discussion

See [`NSTextFinder`](nstextfinder.md) for a complete description.

## Parameters

- `range`: The specified range of the text to replace.
- `string`: The replacement string.

## See Also

- [func shouldReplaceCharacters(inRanges: [NSValue], with: [String]) -> Bool](nstextfinderclient/shouldreplacecharacters(inranges:with:).md)
  Returns whether the specified strings should be replaced.
- [func didReplaceCharacters()](nstextfinderclient/didreplacecharacters.md)
  Specifies whether text characters were replaced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/replacecharacters(in:with:))*