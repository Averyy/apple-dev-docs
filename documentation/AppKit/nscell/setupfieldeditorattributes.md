# setUpFieldEditorAttributes(_:)

**Framework**: AppKit  
**Kind**: method

Configures the textual and background attributes of the receiver’s field editor.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setUpFieldEditorAttributes(_ textObj: NSText) -> NSText
```

#### Return Value

The configured field editor.

#### Discussion

If the receiver is disabled, this method sets the text color to dark gray; otherwise the method sets it to the default color. If the receiver has a bezeled border, this method sets the background to the default color for text backgrounds; otherwise, the method sets it to the color of the receiver’s `NSControl` object.

You should not use this method to substitute a new field editor. [`setUpFieldEditorAttributes(_:)`](nscell/setupfieldeditorattributes(_:).md) is intended to modify the attributes of the text object (that is, the field editor) passed into it and return that text object. If you want to substitute your own field editor, use the [`fieldEditor(_:for:)`](nswindow/fieldeditor(_:for:).md) method or the [`windowWillReturnFieldEditor(_:to:)`](nswindowdelegate/windowwillreturnfieldeditor(_:to:).md) delegate method of `NSWindow`.

## Parameters

- `textObj`: The field editor to configure.

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
- [var allowsEditingTextAttributes: Bool](nscell/allowseditingtextattributes.md)
  A Boolean value indicating whether the cell allows the editing of its content’s text attributes by the user.
- [var importsGraphics: Bool](nscell/importsgraphics.md)
  A Boolean value indicating whether the cell supports the importation of images into its text.
- [var title: String](nscell/title.md)
  The cell’s title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/setupfieldeditorattributes(_:))*