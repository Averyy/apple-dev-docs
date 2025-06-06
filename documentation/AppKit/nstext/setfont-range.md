# setFont(_:range:)

**Framework**: AppKit  
**Kind**: method

Sets the font of characters within `aRange` to `aFont`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setFont(_ font: NSFont, range: NSRange)
```

#### Discussion

This method applies only to a rich text object.

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](nstextview/shouldchangetext(inranges:replacementstrings:).md) or [`shouldChangeText(in:replacementString:)`](nstextview/shouldchangetext(in:replacementstring:).md) to include this method in an undoable action.

## See Also

- [func changeFont(Any?)](nstext/changefont(_:).md)
  This action method changes the font of the selection for a rich text object, or of all text for a plain text object.
- [var font: NSFont?](nstext/font.md)
  The font of all the receiver’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/setfont(_:range:))*