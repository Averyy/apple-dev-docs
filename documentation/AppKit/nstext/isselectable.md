# isSelectable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that controls whether the receiver allows the user to select its text.

**Availability**:
- macOS

## Declaration

```swift
var isSelectable: Bool { get set }
```

```objc
@property (getter=isSelectable) BOOL selectable;
```

#### Discussion

If `flag` is [`true`](../../Swift/true.md), the receiver allows the user to select text; if `flag` is [`false`](../../Swift/false.md), it doesn’t.

You can set selections programmatically regardless of this setting. If the receiver is made not selectable, it’s also made not editable. `NSText` objects are by default editable and selectable.

## See Also

### Setting behavioral attributes
- [var isEditable: Bool](./iseditable.md)
  A Boolean that controls whether the receiver allows the user to edit its text.
- [var isFieldEditor: Bool](./isfieldeditor.md)
  A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.
- [var isRichText: Bool](./isrichtext.md)
  A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.
- [var importsGraphics: Bool](./importsgraphics.md)
  A Boolean that controls whether the receiver allows the user to import files by dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/isselectable)*