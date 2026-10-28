# importsGraphics

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell supports the importation of images into its text.

**Availability**:
- macOS

## Declaration

```swift
var importsGraphics: Bool { get set }
```

```objc
@property BOOL importsGraphics;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the cell can import images into its text and support the RTFD text format.

## See Also

### Modifying Textual Attributes
- [var isEditable: Bool](./iseditable.md)
  A Boolean value indicating whether the cell is editable.
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value indicating whether the cell’s text can be selected.
- [var isScrollable: Bool](./isscrollable.md)
  A Boolean value indicating whether excess text scrolls past the cell’s bounds.
- [var alignment: NSTextAlignment](./alignment.md)
  The alignment of the cell’s text.
- [var font: NSFont?](./font.md)
  The font that the cell uses to display text.
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The line break mode to use when drawing text in the cell.
- [var truncatesLastVisibleLine: Bool](./truncateslastvisibleline.md)
  A Boolean value indicating whether the cell truncates text that does not fit within the cell’s bounds.
- [var wraps: Bool](./wraps.md)
  A Boolean value indicating whether the cell wraps text whose length that exceeds the cell’s frame.
- [var baseWritingDirection: NSWritingDirection](./basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.
- [var attributedStringValue: NSAttributedString](./attributedstringvalue.md)
  The cell’s value as an attributed string.
- [var allowsEditingTextAttributes: Bool](./allowseditingtextattributes.md)
  A Boolean value indicating whether the cell allows the editing of its content’s text attributes by the user.
- [func setUpFieldEditorAttributes(NSText) -> NSText](./setupfieldeditorattributes%28_%29.md)
  Configures the textual and background attributes of the receiver’s field editor.
- [var title: String](./title.md)
  The cell’s title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/importsgraphics)*