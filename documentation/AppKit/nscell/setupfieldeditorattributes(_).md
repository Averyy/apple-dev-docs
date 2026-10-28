# setUpFieldEditorAttributes(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Configures the textual and background attributes of the receiver’s field editor.

**Availability**:
- macOS

## Declaration

```swift
func setUpFieldEditorAttributes(_ textObj: NSText) -> NSText
```

```objc
- (NSText *) setUpFieldEditorAttributes:(NSText *) textObj;
```

## Return Value

The configured field editor.

## Discussion

If the receiver is disabled, this method sets the text color to dark gray; otherwise the method sets it to the default color. If the receiver has a bezeled border, this method sets the background to the default color for text backgrounds; otherwise, the method sets it to the color of the receiver’s `NSControl` object.

You should not use this method to substitute a new field editor. [`setUpFieldEditorAttributes(_:)`](./setupfieldeditorattributes%28_%29.md) is intended to modify the attributes of the text object (that is, the field editor) passed into it and return that text object. If you want to substitute your own field editor, use the [`fieldEditor(_:for:)`](../nswindow/fieldeditor%28_,for%29.md) method or the [`windowWillReturnFieldEditor(_:to:)`](../nswindowdelegate/windowwillreturnfieldeditor%28_,to%29.md) delegate method of `NSWindow`.

## Parameters

- `textObj`: The field editor to configure.

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
- [var importsGraphics: Bool](./importsgraphics.md)
  A Boolean value indicating whether the cell supports the importation of images into its text.
- [var title: String](./title.md)
  The cell’s title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/setupfieldeditorattributes(_:))*