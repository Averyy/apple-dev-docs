# alignJustified(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Applies full justification to selected paragraphs (or all text, if the receiver is a plain text object).

**Availability**:
- macOS

## Declaration

```swift
func alignJustified(_ sender: Any?)
```

```objc
- (void) alignJustified:(id) sender;
```

## Parameters

- `sender`: The control that sent the message; may be `nil`.

## See Also

### Related Documentation
- [func alignRight(Any?)](../nstext/alignright%28_%29.md)
  This action method applies right alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [func alignLeft(Any?)](../nstext/alignleft%28_%29.md)
  This action method applies left alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [func alignCenter(Any?)](../nstext/aligncenter%28_%29.md)
  This action method applies center alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [var alignment: NSTextAlignment](../nstext/alignment.md)
  The alignment of all the receiver’s text.
### Setting text attributes
- [func changeAttributes(Any?)](./changeattributes%28_%29.md)
  Changes the attributes of the current selection.
- [func changeColor(Any?)](./changecolor%28_%29.md)
  Sets the color of the selected text.
- [func setAlignment(NSTextAlignment, range: NSRange)](./setalignment%28_,range%29.md)
  Sets the alignment of the paragraphs containing characters in the specified range.
- [var typingAttributes: [NSAttributedString.Key : Any]](./typingattributes.md)
  The receiver’s typing attributes.
- [func useStandardKerning(Any?)](./usestandardkerning%28_%29.md)
  Set the receiver to use pair kerning data for the glyphs in its selection, or for all glyphs if the receiver is a plain text view.
- [func lowerBaseline(Any?)](./lowerbaseline%28_%29.md)
  Lowers the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
- [func raiseBaseline(Any?)](./raisebaseline%28_%29.md)
  Raises the baseline offset of selected text by 1 point, or of all text if the receiver is a plain text view.
- [func turnOffKerning(Any?)](./turnoffkerning%28_%29.md)
  Sets the receiver to use nominal glyph spacing for the glyphs in its selection, or for all glyphs if the receiver is a plain text view.
- [func loosenKerning(Any?)](./loosenkerning%28_%29.md)
  Increases the space between glyphs in the receiver’s selection, or in all text if the receiver is a plain text view.
- [func tightenKerning(Any?)](./tightenkerning%28_%29.md)
  Decreases the space between glyphs in the receiver’s selection, or for all glyphs if the receiver is a plain text view.
- [func useStandardLigatures(Any?)](./usestandardligatures%28_%29.md)
  Sets the receiver to use the standard ligatures available for the fonts and languages used when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.
- [func turnOffLigatures(Any?)](./turnoffligatures%28_%29.md)
  Sets the receiver to use only required ligatures when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.
- [func useAllLigatures(Any?)](./useallligatures%28_%29.md)
  Sets the receiver to use all ligatures available for the fonts and languages used when setting text, for the glyphs in the selection if the receiver is a rich text view, or for all glyphs if it’s a plain text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/alignjustified(_:))*