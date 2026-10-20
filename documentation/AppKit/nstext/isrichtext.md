# isRichText

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.

**Availability**:
- macOS

## Declaration

```swift
var isRichText: Bool { get set }
```

```objc
@property (getter=isRichText) BOOL richText;
```

#### Discussion

If `flag` is [`true`](../../Swift/true.md) the receiver allows the user to apply attributes to specific ranges of the text; if `flag` is [`false`](../../Swift/false.md) it doesn’t.

## See Also

### Setting behavioral attributes
- [var isEditable: Bool](./iseditable.md)
  A Boolean that controls whether the receiver allows the user to edit its text.
- [var isSelectable: Bool](./isselectable.md)
  A Boolean that controls whether the receiver allows the user to select its text.
- [var isFieldEditor: Bool](./isfieldeditor.md)
  A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.
- [var importsGraphics: Bool](./importsgraphics.md)
  A Boolean that controls whether the receiver allows the user to import files by dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/isrichtext)*