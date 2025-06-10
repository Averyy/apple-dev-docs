# toggleAutomaticLinkDetection(_:)

**Framework**: AppKit  
**Kind**: method

Changes the state of automatic link detection from enabled to disabled and vice versa.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func toggleAutomaticLinkDetection(_ sender: Any?)
```

#### Discussion

Automatic link detection causes strings representing URLs typed in the view to be automatically made into links to those URLs.

## Parameters

- `sender`: The control sending the message; may be  .

## See Also

- [func url(at location: Int, effectiveRange: NSRangePointer) -> URL?](../Foundation/NSAttributedString/url(at:effectiveRange:).md)
  Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.
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
- [var importsGraphics: Bool](nstextview/importsgraphics.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to import files by dragging.
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
- [var displaysLinkToolTips: Bool](nstextview/displayslinktooltips.md)
  A Boolean value that indicates whether the text view automatically supplies the destination of a link as a tooltip for text that has a link attribute.
- [var isAutomaticTextCompletionEnabled: Bool](nstextview/isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text view supplies autocompletion suggestions as the user types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/toggleautomaticlinkdetection(_:))*