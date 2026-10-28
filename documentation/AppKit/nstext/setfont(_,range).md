# setFont(_:range:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the font of characters within `aRange` to `aFont`.

**Availability**:
- macOS

## Declaration

```swift
func setFont(_ font: NSFont, range: NSRange)
```

```objc
- (void) setFont:(NSFont *) font range:(NSRange) range;
```

## Discussion

This method applies only to a rich text object.

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](../nstextview/shouldchangetext%28inranges,replacementstrings%29.md) or [`shouldChangeText(in:replacementString:)`](../nstextview/shouldchangetext%28in,replacementstring%29.md) to include this method in an undoable action.

## See Also

### Changing the font
- [func changeFont(Any?)](./changefont%28_%29.md)
  This action method changes the font of the selection for a rich text object, or of all text for a plain text object.
- [var font: NSFont?](./font.md)
  The font of all the receiver’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/setfont(_:range:))*