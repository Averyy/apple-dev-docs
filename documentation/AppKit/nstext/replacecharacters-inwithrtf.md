# replaceCharacters(in:withRTF:)

**Framework**: AppKit  
**Kind**: method

Replaces the characters in the given range with RTF text interpreted from the given RTF data.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func replaceCharacters(in range: NSRange, withRTF rtfData: Data)
```

#### Discussion

This method applies only to rich text objects.

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](nstextview/shouldchangetext(inranges:replacementstrings:).md) or [`shouldChangeText(in:replacementString:)`](nstextview/shouldchangetext(in:replacementstring:).md) to include this method in an undoable action.

This method is designed for transferring text from out-of-process sources such as the pasteboard. In most cases, programmatic modification of the text is best done by operating on the text storage directly, using the general methods of [`NSMutableAttributedString`](https://developer.apple.com/documentation/Foundation/NSMutableAttributedString).

## Parameters

- `range`: The range of characters to be replaced.
- `rtfData`: The RTF data from which to derive the replacement string.

## See Also

- [func replaceCharacters(in: NSRange, withRTFD: Data)](nstext/replacecharacters(in:withrtfd:).md)
  Replaces the characters in the given range with RTFD text interpreted from the given RTFD data.
- [func replaceCharacters(in: NSRange, with: String)](nstext/replacecharacters(in:with:).md)
  Replaces the characters in the given range with those in the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/replacecharacters(in:withrtf:))*