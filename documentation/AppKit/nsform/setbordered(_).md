# setBordered(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the receiver’s entries should display a border around their editable text fields.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func setBordered(_ flag: Bool)
```

```objc
- (void) setBordered:(BOOL) flag;
```

## Discussion

The border is drawn as a thin line around the editable text field. An entry can have a border or a bezel, but not both.

## Parameters

- `flag`: [`true`](../../Swift/true.md) to display a border around all entries; otherwise, [`false`](../../Swift/false.md) to show no border around all entries.

## See Also

### Related Documentation
- [var isBordered: Bool](../nscell/isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
### Changing the Appearance of All the Entries
- [func setBezeled(Bool)](./setbezeled%28_%29.md)
  Sets whether the receiver’s entries should display a bezel around their editable text.
- [func setEntryWidth(CGFloat)](./setentrywidth%28_%29.md)
  Sets the width of all the entries in the receiver.
- [func setFrameSize(NSSize)](./setframesize%28_%29.md)
  Sets the size of the receiver’s frame size to the specified value.
- [func setInterlineSpacing(CGFloat)](./setinterlinespacing%28_%29.md)
  Sets the spacing between entries
- [func setTitleAlignment(NSTextAlignment)](./settitlealignment%28_%29.md)
  Sets the alignment for all of the entry titles.
- [func setTitleBaseWritingDirection(NSWritingDirection)](./settitlebasewritingdirection%28_%29.md)
  Sets the writing direction for the title of every control embedded in the form.
- [func setTextAlignment(NSTextAlignment)](./settextalignment%28_%29.md)
  Sets the alignment for all of the receiver’s editable text.
- [func setTextBaseWritingDirection(NSWritingDirection)](./settextbasewritingdirection%28_%29.md)
  Sets the writing direction for the text content of every control embedded in the form.
- [func setTitleFont(NSFont)](./settitlefont%28_%29.md)
  Sets the font for all of the entry titles.
- [func setTextFont(NSFont)](./settextfont%28_%29.md)
  Sets the font for all of the receiver’s editable text fields


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/setbordered(_:))*