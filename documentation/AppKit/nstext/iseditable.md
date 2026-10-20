# isEditable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that controls whether the receiver allows the user to edit its text.

**Availability**:
- macOS

## Declaration

```swift
var isEditable: Bool { get set }
```

```objc
@property (getter=isEditable) BOOL editable;
```

#### Discussion

If `flag` is [`true`](../../Swift/true.md), the receiver allows the user to edit text and attributes; if `flag` is [`false`](../../Swift/false.md), it doesn’t.

You can change the receiver’s text programmatically regardless of this setting. If the receiver is made editable, it’s also made selectable. `NSText` objects are by default editable.

## See Also

### Setting behavioral attributes
- [var isSelectable: Bool](./isselectable.md)
  A Boolean that controls whether the receiver allows the user to select its text.
- [var isFieldEditor: Bool](./isfieldeditor.md)
  A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.
- [var isRichText: Bool](./isrichtext.md)
  A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.
- [var importsGraphics: Bool](./importsgraphics.md)
  A Boolean that controls whether the receiver allows the user to import files by dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/iseditable)*