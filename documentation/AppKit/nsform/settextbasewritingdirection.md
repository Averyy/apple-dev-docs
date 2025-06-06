# setTextBaseWritingDirection(_:)

**Framework**: AppKit  
**Kind**: method

Sets the writing direction for the text content of every control embedded in the form.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func setTextBaseWritingDirection(_ writingDirection: NSWritingDirection)
```

## Parameters

- `writingDirection`: This value can be one of the following constants:  ,  , or  .

## See Also

- [var baseWritingDirection: NSWritingDirection](nscontrol/basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.
- [func setBezeled(Bool)](nsform/setbezeled(_:).md)
  Sets whether the receiver’s entries should display a bezel around their editable text.
- [func setBordered(Bool)](nsform/setbordered(_:).md)
  Sets whether the receiver’s entries should display a border around their editable text fields.
- [func setEntryWidth(CGFloat)](nsform/setentrywidth(_:).md)
  Sets the width of all the entries in the receiver.
- [func setFrameSize(NSSize)](nsform/setframesize(_:).md)
  Sets the size of the receiver’s frame size to the specified value.
- [func setInterlineSpacing(CGFloat)](nsform/setinterlinespacing(_:).md)
  Sets the spacing between entries
- [func setTitleAlignment(NSTextAlignment)](nsform/settitlealignment(_:).md)
  Sets the alignment for all of the entry titles.
- [func setTitleBaseWritingDirection(NSWritingDirection)](nsform/settitlebasewritingdirection(_:).md)
  Sets the writing direction for the title of every control embedded in the form.
- [func setTextAlignment(NSTextAlignment)](nsform/settextalignment(_:).md)
  Sets the alignment for all of the receiver’s editable text.
- [func setTitleFont(NSFont)](nsform/settitlefont(_:).md)
  Sets the font for all of the entry titles.
- [func setTextFont(NSFont)](nsform/settextfont(_:).md)
  Sets the font for all of the receiver’s editable text fields


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/settextbasewritingdirection(_:))*