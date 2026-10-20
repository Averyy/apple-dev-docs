# isFieldEditor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.

**Availability**:
- macOS

## Declaration

```swift
var isFieldEditor: Bool { get set }
```

```objc
@property (getter=isFieldEditor) BOOL fieldEditor;
```

#### Discussion

If `flag` is [`true`](../../Swift/true.md), the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder; if `flag` is [`false`](../../Swift/false.md), it doesn’t, instead accepting these characters as text input.

See the [`NSWindow`](../nswindow.md) class specification for more information on field editors. By default, `NSText` objects don’t behave as field editors.

## See Also

### Setting behavioral attributes
- [var isEditable: Bool](./iseditable.md)
  A Boolean that controls whether the receiver allows the user to edit its text.
- [var isSelectable: Bool](./isselectable.md)
  A Boolean that controls whether the receiver allows the user to select its text.
- [var isRichText: Bool](./isrichtext.md)
  A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.
- [var importsGraphics: Bool](./importsgraphics.md)
  A Boolean that controls whether the receiver allows the user to import files by dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/isfieldeditor)*