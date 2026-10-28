# attributedStringValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s value as an attributed string.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var attributedStringValue: NSAttributedString { get set }
```

```objc
@property (copy) NSAttributedString * attributedStringValue;
```

## Discussion

Use this property to get the value of the cell interpreted as an attributed string. The textual attributes included in the string are the default paragraph style, the cell’s font and alignment, and whether the cell is enabled and scrollable.

When setting the value of this property, if the cell has a formatter, but the formatter does not understand the attributed string, the formatter marks the cell’s object as invalid. If the receiver is not a text-type cell, it is converted to one before the value is set.

If you use a class that has an [`attributedStringValue`](./attributedstringvalue.md) property, the cell gets the string from that property instead of using the [`stringValue`](./stringvalue.md) property.

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
- [var allowsEditingTextAttributes: Bool](./allowseditingtextattributes.md)
  A Boolean value indicating whether the cell allows the editing of its content’s text attributes by the user.
- [var importsGraphics: Bool](./importsgraphics.md)
  A Boolean value indicating whether the cell supports the importation of images into its text.
- [func setUpFieldEditorAttributes(NSText) -> NSText](./setupfieldeditorattributes%28_%29.md)
  Configures the textual and background attributes of the receiver’s field editor.
- [var title: String](./title.md)
  The cell’s title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/attributedstringvalue)*