# replaceCharacters(in:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces the characters in the given range with those in the given string.

**Availability**:
- macOS

## Declaration

```swift
func replaceCharacters(in range: NSRange, with string: String)
```

```objc
- (void) replaceCharactersInRange:(NSRange) range withString:(NSString *) string;
```

#### Discussion

For a rich text object, the text of `aString` is assigned the formatting attributes of the first character of the text it replaces, or of the character immediately before `aRange` if the range’s length is 0. If the range’s location is 0, the formatting attributes of the first character in the receiver are used.

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](../nstextview/shouldchangetext%28inranges,replacementstrings%29.md) or [`shouldChangeText(in:replacementString:)`](../nstextview/shouldchangetext%28in,replacementstring%29.md) to include this method in an undoable action.

In most cases, programmatic modification of the text is best done by operating on the text storage directly, using the general methods of [`NSMutableAttributedString`](../../Foundation/nsmutableattributedstring.md).

## Parameters

- `range`: The range of characters to be replaced.
- `string`: The replacement string.

## See Also

### Replacing text
- [func replaceCharacters(in: NSRange, withRTF: Data)](./replacecharacters%28in,withrtf%29.md)
  Replaces the characters in the given range with RTF text interpreted from the given RTF data.
- [func replaceCharacters(in: NSRange, withRTFD: Data)](./replacecharacters%28in,withrtfd%29.md)
  Replaces the characters in the given range with RTFD text interpreted from the given RTFD data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/replacecharacters(in:with:))*