# shouldReplaceCharacters(inRanges:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the specified strings should be replaced.

**Availability**:
- macOS

## Declaration

```swift
optional func shouldReplaceCharacters(inRanges ranges: [NSValue], with strings: [String]) -> Bool
```

```objc
- (BOOL) shouldReplaceCharactersInRanges:(NSArray<NSValue *> *) ranges withStrings:(NSArray<NSString *> *) strings;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the replacement should occur; otherwise [`false`](../../Swift/false.md).

## Discussion

See [`NSTextFinder`](../nstextfinder.md) for a complete description.

## Parameters

- `ranges`: The ranges of the strings to replace.
- `strings`: The replacement strings.

## See Also

### Replacing Text
- [func replaceCharacters(in: NSRange, with: String)](./replacecharacters%28in,with%29.md)
  Replaces the text in the specified range with the new string.
- [func didReplaceCharacters()](./didreplacecharacters%28%29.md)
  Specifies whether text characters were replaced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/shouldreplacecharacters(inranges:with:))*