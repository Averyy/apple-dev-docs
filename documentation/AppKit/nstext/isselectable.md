# isSelectable

**Framework**: AppKit  
**Kind**: property

A Boolean that controls whether the receiver allows the user to select its text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isSelectable: Bool { get set }
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/swift/true), the receiver allows the user to select text; if `flag` is [`false`](https://developer.apple.com/documentation/swift/false), it doesn’t.

You can set selections programmatically regardless of this setting. If the receiver is made not selectable, it’s also made not editable. `NSText` objects are by default editable and selectable.

## See Also

- [var isEditable: Bool](nstext/iseditable.md)
  A Boolean that controls whether the receiver allows the user to edit its text.
- [var isFieldEditor: Bool](nstext/isfieldeditor.md)
  A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.
- [var isRichText: Bool](nstext/isrichtext.md)
  A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.
- [var importsGraphics: Bool](nstext/importsgraphics.md)
  A Boolean that controls whether the receiver allows the user to import files by dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/isselectable)*