# lowerBaseline(_:)

**Framework**: AppKit  
**Kind**: method

Lowers the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func lowerBaseline(_ sender: Any?)
```

#### Discussion

As such, this method defines a more primitive operation than subscripting.

## Parameters

- `sender`: The control that sent the message; may be  .

## See Also

- [func unscript(Any?)](nstext/unscript(_:).md)
  This action method removes any superscripting or subscripting from selected text (or all text if the receiver is a plain text object).
- [func `subscript`(Any?)](nstext/subscript(_:).md)
  This action method applies a subscript attribute to selected text (or all text if the receiver is a plain text object), lowering its baseline offset by a predefined amount.
- [func alignJustified(Any?)](nstextview/alignjustified(_:).md)
  Applies full justification to selected paragraphs (or all text, if the receiver is a plain text object).
- [func changeAttributes(Any?)](nstextview/changeattributes(_:).md)
  Changes the attributes of the current selection.
- [func changeColor(Any?)](nstextview/changecolor(_:).md)
  Sets the color of the selected text.
- [func setAlignment(NSTextAlignment, range: NSRange)](nstextview/setalignment(_:range:).md)
  Sets the alignment of the paragraphs containing characters in the specified range.
- [var typingAttributes: [NSAttributedString.Key : Any]](nstextview/typingattributes.md)
  The receiver’s typing attributes.
- [func useStandardKerning(Any?)](nstextview/usestandardkerning(_:).md)
  Set the receiver to use pair kerning data for the glyphs in its selection, or for all glyphs if the receiver is a plain text view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/lowerbaseline(_:))*