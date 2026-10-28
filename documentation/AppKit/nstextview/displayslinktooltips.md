# displaysLinkToolTips

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the text view automatically supplies the destination of a link as a tooltip for text that has a link attribute.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var displaysLinkToolTips: Bool { get set }
```

```objc
@property BOOL displaysLinkToolTips;
```

## Discussion

[`true`](../../Swift/true.md) if link tooltips are automatically displayed; otherwise, [`false`](../../Swift/false.md).

The default value for this feature is [`true`](../../Swift/true.md); clients who do not wish tooltips to be displayed automatically must explicitly disable it.

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
- [func setBaseWritingDirection(NSWritingDirection, range: NSRange)](./setbasewritingdirection%28_,range%29.md)
  Sets the base writing direction of a range of text.
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
- [var isAutomaticTextCompletionEnabled: Bool](./isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text view supplies autocompletion suggestions as the user types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/displayslinktooltips)*