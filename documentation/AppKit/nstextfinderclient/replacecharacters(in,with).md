# replaceCharacters(in:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces the text in the specified range with the new string.

**Availability**:
- macOS

## Declaration

```swift
optional func replaceCharacters(in range: NSRange, with string: String)
```

```objc
- (void) replaceCharactersInRange:(NSRange) range withString:(NSString *) string;
```

## Discussion

See [`NSTextFinder`](../nstextfinder.md) for a complete description.

## Parameters

- `range`: The specified range of the text to replace.
- `string`: The replacement string.

## See Also

### Replacing Text
- [func shouldReplaceCharacters(inRanges: [NSValue], with: [String]) -> Bool](./shouldreplacecharacters%28inranges,with%29.md)
  Returns whether the specified strings should be replaced.
- [func didReplaceCharacters()](./didreplacecharacters%28%29.md)
  Specifies whether text characters were replaced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/replacecharacters(in:with:))*