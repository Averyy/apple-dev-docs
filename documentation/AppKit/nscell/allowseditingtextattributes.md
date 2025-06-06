# allowsEditingTextAttributes

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell allows the editing of its content’s text attributes by the user.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsEditingTextAttributes: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the user can modify the font and other textual attributes of the cell. When the value is [`false`](https://developer.apple.com/documentation/swift/false), the user cannot edit the text or import graphics, which effectively means the cell cannot support RTFD text.

## See Also

- [var isEditable: Bool](nscell/iseditable.md)
  A Boolean value indicating whether the cell is editable.
- [var isSelectable: Bool](nscell/isselectable.md)
  A Boolean value indicating whether the cell’s text can be selected.
- [var isScrollable: Bool](nscell/isscrollable.md)
  A Boolean value indicating whether excess text scrolls past the cell’s bounds.
- [var alignment: NSTextAlignment](nscell/alignment.md)
  The alignment of the cell’s text.
- [var font: NSFont?](nscell/font.md)
  The font that the cell uses to display text.
- [var lineBreakMode: NSLineBreakMode](nscell/linebreakmode.md)
  The line break mode to use when drawing text in the cell.
- [var truncatesLastVisibleLine: Bool](nscell/truncateslastvisibleline.md)
  A Boolean value indicating whether the cell truncates text that does not fit within the cell’s bounds.
- [var wraps: Bool](nscell/wraps.md)
  A Boolean value indicating whether the cell wraps text whose length that exceeds the cell’s frame.
- [var baseWritingDirection: NSWritingDirection](nscell/basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.
- [var attributedStringValue: NSAttributedString](nscell/attributedstringvalue.md)
  The cell’s value as an attributed string.
- [var importsGraphics: Bool](nscell/importsgraphics.md)
  A Boolean value indicating whether the cell supports the importation of images into its text.
- [func setUpFieldEditorAttributes(NSText) -> NSText](nscell/setupfieldeditorattributes(_:).md)
  Configures the textual and background attributes of the receiver’s field editor.
- [var title: String](nscell/title.md)
  The cell’s title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/allowseditingtextattributes)*