# textContainer(forGlyphAt:effectiveRange:)

**Framework**: AppKit  
**Kind**: method

Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func textContainer(forGlyphAt glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?) -> NSTextContainer?
```

#### Return Value

The text container in which the glyph at `glyphIndex` is laid out.

#### Discussion

This method causes glyph generation and layout for the line fragment containing the specified glyph, or if noncontiguous layout is not enabled, up to and including that line fragment. If noncontiguous layout is not enabled and `effectiveGlyphRange` is not `NULL`, this method additionally causes glyph generation and layout for the entire text container containing the specified glyph.

Overriding this method is not recommended. Any changes to the returned glyph range should be done at the typesetter level.

## Parameters

- `glyphIndex`: Index of a glyph in the returned container.
- `effectiveGlyphRange`: If not  , on output, points to the whole range of glyphs that are in the returned container.

## See Also

- [var textContainers: [NSTextContainer]](nslayoutmanager/textcontainers.md)
  The current text containers of the layout manager.
- [func addTextContainer(NSTextContainer)](nslayoutmanager/addtextcontainer(_:).md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [func insertTextContainer(NSTextContainer, at: Int)](nslayoutmanager/inserttextcontainer(_:at:).md)
  Inserts a text container at the specified index in the list of text containers.
- [func removeTextContainer(at: Int)](nslayoutmanager/removetextcontainer(at:).md)
  Removes the text container at the specified index and invalidates the layout as necessary.
- [func setTextContainer(NSTextContainer, forGlyphRange: NSRange)](nslayoutmanager/settextcontainer(_:forglyphrange:).md)
  Associates a text container with the specified range of glyphs.
- [func textContainerChangedGeometry(NSTextContainer)](nslayoutmanager/textcontainerchangedgeometry(_:).md)
  Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [func textContainerChangedTextView(NSTextContainer)](nslayoutmanager/textcontainerchangedtextview(_:).md)
  Updates the information necessary to manage text view objects for the specified text container.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSTextContainer?](nslayoutmanager/textcontainer(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the text container that manages the layout for the specified glyph.
- [func usedRect(for: NSTextContainer) -> NSRect](nslayoutmanager/usedrect(for:).md)
  Returns the bounding rectangle for the glyphs in the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/textcontainer(forglyphat:effectiverange:))*