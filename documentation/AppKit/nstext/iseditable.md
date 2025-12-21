# isEditable

**Framework**: AppKit  
**Kind**: property

A Boolean that controls whether the receiver allows the user to edit its text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isEditable: Bool { get set }
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true), the receiver allows the user to edit text and attributes; if `flag` is [`false`](https://developer.apple.com/documentation/Swift/false), it doesn’t.

You can change the receiver’s text programmatically regardless of this setting. If the receiver is made editable, it’s also made selectable. `NSText` objects are by default editable.

## See Also

- [var isSelectable: Bool](nstext/isselectable.md)
  A Boolean that controls whether the receiver allows the user to select its text.
- [var isFieldEditor: Bool](nstext/isfieldeditor.md)
  A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.
- [var isRichText: Bool](nstext/isrichtext.md)
  A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.
- [var importsGraphics: Bool](nstext/importsgraphics.md)
  A Boolean that controls whether the receiver allows the user to import files by dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/iseditable)*