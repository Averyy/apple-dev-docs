# shouldReplaceCharacters(inRanges:with:)

**Framework**: AppKit  
**Kind**: method

Returns whether the specified strings should be replaced.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func shouldReplaceCharacters(inRanges ranges: [NSValue], with strings: [String]) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the replacement should occur; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

See [`NSTextFinder`](nstextfinder.md) for a complete description.

## Parameters

- `ranges`: The ranges of the strings to replace.
- `strings`: The replacement strings.

## See Also

- [func replaceCharacters(in: NSRange, with: String)](nstextfinderclient/replacecharacters(in:with:).md)
  Replaces the text in the specified range with the new string.
- [func didReplaceCharacters()](nstextfinderclient/didreplacecharacters.md)
  Specifies whether text characters were replaced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/shouldreplacecharacters(inranges:with:))*