# replaceCharacters(in:withRTFD:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces the characters in the given range with RTFD text interpreted from the given RTFD data.

**Availability**:
- macOS

## Declaration

```swift
func replaceCharacters(in range: NSRange, withRTFD rtfdData: Data)
```

```objc
- (void) replaceCharactersInRange:(NSRange) range withRTFD:(NSData *) rtfdData;
```

## Discussion

This method applies only to rich text objects.

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](../nstextview/shouldchangetext%28inranges,replacementstrings%29.md) or [`shouldChangeText(in:replacementString:)`](../nstextview/shouldchangetext%28in,replacementstring%29.md) to include this method in an undoable action.

This method is designed for transferring text from out-of-process sources such as the pasteboard. In most cases, programmatic modification of the text is best done by operating on the text storage directly, using the general methods of [`NSMutableAttributedString`](../../Foundation/nsmutableattributedstring.md).

## Parameters

- `range`: The range of characters to be replaced.
- `rtfdData`: The RTFD data from which to derive the replacement string.

## See Also

### Replacing text
- [func replaceCharacters(in: NSRange, withRTF: Data)](./replacecharacters%28in,withrtf%29.md)
  Replaces the characters in the given range with RTF text interpreted from the given RTF data.
- [func replaceCharacters(in: NSRange, with: String)](./replacecharacters%28in,with%29.md)
  Replaces the characters in the given range with those in the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/replacecharacters(in:withrtfd:))*