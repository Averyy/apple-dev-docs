# attributedStringValue

**Framework**: AppKit  
**Kind**: property

The cell’s value as an attributed string.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var attributedStringValue: NSAttributedString { get set }
```

#### Discussion

Use this property to get the value of the cell interpreted as an attributed string. The textual attributes included in the string are the default paragraph style, the cell’s font and alignment, and whether the cell is enabled and scrollable.

When setting the value of this property, if the cell has a formatter, but the formatter does not understand the attributed string, the formatter marks the cell’s object as invalid. If the receiver is not a text-type cell, it is converted to one before the value is set.

If you use a class that has an [`attributedStringValue`](nscell/attributedstringvalue.md) property, the cell gets the string from that property instead of using the [`stringValue`](nscell/stringvalue.md) property.

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
- [var allowsEditingTextAttributes: Bool](nscell/allowseditingtextattributes.md)
  A Boolean value indicating whether the cell allows the editing of its content’s text attributes by the user.
- [var importsGraphics: Bool](nscell/importsgraphics.md)
  A Boolean value indicating whether the cell supports the importation of images into its text.
- [func setUpFieldEditorAttributes(NSText) -> NSText](nscell/setupfieldeditorattributes(_:).md)
  Configures the textual and background attributes of the receiver’s field editor.
- [var title: String](nscell/title.md)
  The cell’s title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/attributedstringvalue)*