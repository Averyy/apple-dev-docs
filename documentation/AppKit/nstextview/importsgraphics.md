# importsGraphics

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to import files by dragging.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var importsGraphics: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) to allow the user to import files by dragging onto the text views sharing the receiver’s layout manager, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

Text views that are set to accept dragged files are also set to allow rich text. By default, text views don’t accept dragged files but do allow rich text.

## See Also

- [func insert(_ attrString: NSAttributedString, at loc: Int)](../Foundation/NSMutableAttributedString/insert(_:at:).md)
  Inserts the characters and attributes of the given attributed string into the receiver at the given index.
- [init(attachment: NSTextAttachment)](../Foundation/NSAttributedString/init(attachment:).md)
  Creates an attributed string with an attachment.
- [var textStorage: NSTextStorage?](nstextview/textstorage.md)
  The receiver’s text storage object.
- [var allowsUndo: Bool](nstextview/allowsundo.md)
  A Boolean value that indicates whether the receiver allows undo.
- [var isEditable: Bool](nstextview/iseditable.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to edit text.
- [var isSelectable: Bool](nstextview/isselectable.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to select text.
- [var isFieldEditor: Bool](nstextview/isfieldeditor.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager behave as field editors.
- [var isRichText: Bool](nstextview/isrichtext.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to apply attributes to specific ranges of text.
- [func setBaseWritingDirection(NSWritingDirection, range: NSRange)](nstextview/setbasewritingdirection(_:range:).md)
  Sets the base writing direction of a range of text.
- [var defaultParagraphStyle: NSParagraphStyle?](nstextview/defaultparagraphstyle.md)
  The receiver’s default paragraph style.
- [func outline(Any?)](nstextview/outline(_:).md)
  Adds the outline attribute to the selected text attributes if absent; removes the attribute if present.
- [var allowsImageEditing: Bool](nstextview/allowsimageediting.md)
  Indicates whether image attachments should permit editing of their images.
- [var isAutomaticQuoteSubstitutionEnabled: Bool](nstextview/isautomaticquotesubstitutionenabled.md)
  A Boolean value that enables and disables automatic quotation mark substitution.
- [func toggleAutomaticQuoteSubstitution(Any?)](nstextview/toggleautomaticquotesubstitution(_:).md)
  Changes the state of automatic quotation mark substitution from enabled to disabled and vice versa.
- [var isAutomaticLinkDetectionEnabled: Bool](nstextview/isautomaticlinkdetectionenabled.md)
  A Boolean value that enables or disables automatic link detection.
- [func toggleAutomaticLinkDetection(Any?)](nstextview/toggleautomaticlinkdetection(_:).md)
  Changes the state of automatic link detection from enabled to disabled and vice versa.
- [var displaysLinkToolTips: Bool](nstextview/displayslinktooltips.md)
  A Boolean value that indicates whether the text view automatically supplies the destination of a link as a tooltip for text that has a link attribute.
- [var isAutomaticTextCompletionEnabled: Bool](nstextview/isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text view supplies autocompletion suggestions as the user types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/importsgraphics)*