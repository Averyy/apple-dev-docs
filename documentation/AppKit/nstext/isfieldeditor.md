# isFieldEditor

**Framework**: AppKit  
**Kind**: property

A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isFieldEditor: Bool { get set }
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true), the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder; if `flag` is [`false`](https://developer.apple.com/documentation/Swift/false), it doesn’t, instead accepting these characters as text input.

See the [`NSWindow`](nswindow.md) class specification for more information on field editors. By default, `NSText` objects don’t behave as field editors.

## See Also

- [var isEditable: Bool](nstext/iseditable.md)
  A Boolean that controls whether the receiver allows the user to edit its text.
- [var isSelectable: Bool](nstext/isselectable.md)
  A Boolean that controls whether the receiver allows the user to select its text.
- [var isRichText: Bool](nstext/isrichtext.md)
  A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.
- [var importsGraphics: Bool](nstext/importsgraphics.md)
  A Boolean that controls whether the receiver allows the user to import files by dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/isfieldeditor)*