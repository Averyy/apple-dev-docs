# isSelectable

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell’s text can be selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isSelectable: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the cell’s text is selectable. Setting the value of this property to [`false`](https://developer.apple.com/documentation/Swift/false) also sets the [`isEditable`](nscell/iseditable.md) property to [`false`](https://developer.apple.com/documentation/Swift/false). If the value of this cell is [`true`](https://developer.apple.com/documentation/Swift/true), the value in the [`isEditable`](nscell/iseditable.md) property is not affected.

## See Also

- [var isEditable: Bool](nscell/iseditable.md)
  A Boolean value indicating whether the cell is editable.
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
- [var allowsEditingTextAttributes: Bool](nscell/allowseditingtextattributes.md)
  A Boolean value indicating whether the cell allows the editing of its content’s text attributes by the user.
- [var importsGraphics: Bool](nscell/importsgraphics.md)
  A Boolean value indicating whether the cell supports the importation of images into its text.
- [func setUpFieldEditorAttributes(NSText) -> NSText](nscell/setupfieldeditorattributes(_:).md)
  Configures the textual and background attributes of the receiver’s field editor.
- [var title: String](nscell/title.md)
  The cell’s title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isselectable)*