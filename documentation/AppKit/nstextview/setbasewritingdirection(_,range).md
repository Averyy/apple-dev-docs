# setBaseWritingDirection(_:range:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the base writing direction of a range of text.

**Availability**:
- macOS

## Declaration

```swift
func setBaseWritingDirection(_ writingDirection: NSWritingDirection, range: NSRange)
```

```objc
- (void) setBaseWritingDirection:(NSWritingDirection) writingDirection range:(NSRange) range;
```

#### Discussion

Invoke this method to change the base writing direction from left-to-right to right-to-left for languages like Hebrew and Arabic, for example.

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](./shouldchangetext%28inranges,replacementstrings%29.md) or [`shouldChangeText(in:replacementString:)`](./shouldchangetext%28in,replacementstring%29.md) to include this method in an undoable action.

## Parameters

- `writingDirection`: The new writing direction for the text in `range`.
- `range`: The range of text that will have the new writing direction.

## See Also

### Setting behavioral attributes
- [var allowsUndo: Bool](./allowsundo.md)
  A Boolean value that indicates whether the receiver allows undo.
- [var isEditable: Bool](./iseditable.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to edit text.
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to select text.
- [var isFieldEditor: Bool](./isfieldeditor.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager behave as field editors.
- [var isRichText: Bool](./isrichtext.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to apply attributes to specific ranges of text.
- [var importsGraphics: Bool](./importsgraphics.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager allow the user to import files by dragging.
- [var defaultParagraphStyle: NSParagraphStyle?](./defaultparagraphstyle.md)
  The receiver’s default paragraph style.
- [func outline(Any?)](./outline%28_%29.md)
  Adds the outline attribute to the selected text attributes if absent; removes the attribute if present.
- [var allowsImageEditing: Bool](./allowsimageediting.md)
  Indicates whether image attachments should permit editing of their images.
- [var isAutomaticQuoteSubstitutionEnabled: Bool](./isautomaticquotesubstitutionenabled.md)
  A Boolean value that enables and disables automatic quotation mark substitution.
- [func toggleAutomaticQuoteSubstitution(Any?)](./toggleautomaticquotesubstitution%28_%29.md)
  Changes the state of automatic quotation mark substitution from enabled to disabled and vice versa.
- [var isAutomaticLinkDetectionEnabled: Bool](./isautomaticlinkdetectionenabled.md)
  A Boolean value that enables or disables automatic link detection.
- [func toggleAutomaticLinkDetection(Any?)](./toggleautomaticlinkdetection%28_%29.md)
  Changes the state of automatic link detection from enabled to disabled and vice versa.
- [var displaysLinkToolTips: Bool](./displayslinktooltips.md)
  A Boolean value that indicates whether the text view automatically supplies the destination of a link as a tooltip for text that has a link attribute.
- [var isAutomaticTextCompletionEnabled: Bool](./isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text view supplies autocompletion suggestions as the user types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setbasewritingdirection(_:range:))*