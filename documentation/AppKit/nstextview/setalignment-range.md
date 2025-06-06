# setAlignment(_:range:)

**Framework**: AppKit  
**Kind**: method

Sets the alignment of the paragraphs containing characters in the specified range.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setAlignment(_ alignment: NSTextAlignment, range: NSRange)
```

#### Discussion

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](nstextview/shouldchangetext(inranges:replacementstrings:).md) or [`shouldChangeText(in:replacementString:)`](nstextview/shouldchangetext(in:replacementstring:).md) to include this method in an undoable action.

## Parameters

- `alignment`: The new alignment.
- `range`: The range of characters whose paragraphs will have their alignment set.

## See Also

- [var rangeForUserParagraphAttributeChange: NSRange](nstextview/rangeforuserparagraphattributechange.md)
  The range of characters affected by an action method that changes paragraph (not character) attributes.
- [func alignJustified(Any?)](nstextview/alignjustified(_:).md)
  Applies full justification to selected paragraphs (or all text, if the receiver is a plain text object).
- [func changeAttributes(Any?)](nstextview/changeattributes(_:).md)
  Changes the attributes of the current selection.
- [func changeColor(Any?)](nstextview/changecolor(_:).md)
  Sets the color of the selected text.
- [var typingAttributes: [NSAttributedString.Key : Any]](nstextview/typingattributes.md)
  The receiver’s typing attributes.
- [func useStandardKerning(Any?)](nstextview/usestandardkerning(_:).md)
  Set the receiver to use pair kerning data for the glyphs in its selection, or for all glyphs if the receiver is a plain text view.
- [func lowerBaseline(Any?)](nstextview/lowerbaseline(_:).md)
  Lowers the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
- [func raiseBaseline(Any?)](nstextview/raisebaseline(_:).md)
  Raises the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
- [func turnOffKerning(Any?)](nstextview/turnoffkerning(_:).md)
  Sets the receiver to use nominal glyph spacing for the glyphs in its selection, or for all glyphs if the receiver is a plain text view.
- [func loosenKerning(Any?)](nstextview/loosenkerning(_:).md)
  Increases the space between glyphs in the receiver’s selection, or in all text if the receiver is a plain text view.
- [func tightenKerning(Any?)](nstextview/tightenkerning(_:).md)
  Decreases the space between glyphs in the receiver’s selection, or for all glyphs if the receiver is a plain text view.
- [func useStandardLigatures(Any?)](nstextview/usestandardligatures(_:).md)
  Sets the receiver to use the standard ligatures available for the fonts and languages used when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.
- [func turnOffLigatures(Any?)](nstextview/turnoffligatures(_:).md)
  Sets the receiver to use only required ligatures when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.
- [func useAllLigatures(Any?)](nstextview/useallligatures(_:).md)
  Sets the receiver to use all ligatures available for the fonts and languages used when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.
- [func toggleTraditionalCharacterShape(Any?)](nstextview/toggletraditionalcharactershape(_:).md)
  Toggles the `NSCharacterShapeAttributeName` attribute at the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setalignment(_:range:))*