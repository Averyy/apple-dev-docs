# importsGraphics

**Framework**: AppKit  
**Kind**: property

A Boolean that controls whether the receiver allows the user to import files by dragging.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var importsGraphics: Bool { get set }
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/swift/true), the receiver allows the user to import files by dragging; if `flag` is [`false`](https://developer.apple.com/documentation/swift/false), it doesn’t.

If the receiver is set to accept dragged files, it’s also made a rich text object. Subclasses may or may not accept dragged files by default.

## See Also

- [var isEditable: Bool](nstext/iseditable.md)
  A Boolean that controls whether the receiver allows the user to edit its text.
- [var isSelectable: Bool](nstext/isselectable.md)
  A Boolean that controls whether the receiver allows the user to select its text.
- [var isFieldEditor: Bool](nstext/isfieldeditor.md)
  A Boolean that controls whether the receiver interprets Tab, Shift-Tab, and Return (Enter) as cues to end editing and possibly to change the first responder.
- [var isRichText: Bool](nstext/isrichtext.md)
  A Boolean that controls whether the receiver allows the user to apply attributes to specific ranges of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/importsgraphics)*