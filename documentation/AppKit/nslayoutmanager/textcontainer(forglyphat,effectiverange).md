# textContainer(forGlyphAt:effectiveRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func textContainer(forGlyphAt glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?) -> NSTextContainer?
```

```objc
- (NSTextContainer *) textContainerForGlyphAtIndex:(NSUInteger) glyphIndex effectiveRange:(NSRangePointer) effectiveGlyphRange;
```

## Return Value

The text container in which the glyph at `glyphIndex` is laid out.

## Discussion

This method causes glyph generation and layout for the line fragment containing the specified glyph, or if noncontiguous layout is not enabled, up to and including that line fragment. If noncontiguous layout is not enabled and `effectiveGlyphRange` is not `NULL`, this method additionally causes glyph generation and layout for the entire text container containing the specified glyph.

Overriding this method is not recommended. Any changes to the returned glyph range should be done at the typesetter level.

## Parameters

- `glyphIndex`: Index of a glyph in the returned container.
- `effectiveGlyphRange`: If not `NULL`, on output, points to the whole range of glyphs that are in the returned container.

## See Also

### Managing the text containers
- [var textContainers: [NSTextContainer]](./textcontainers.md)
  The current text containers of the layout manager.
- [func addTextContainer(NSTextContainer)](./addtextcontainer%28_%29.md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [func insertTextContainer(NSTextContainer, at: Int)](./inserttextcontainer%28_,at%29.md)
  Inserts a text container at the specified index in the list of text containers.
- [func removeTextContainer(at: Int)](./removetextcontainer%28at%29.md)
  Removes the text container at the specified index and invalidates the layout as necessary.
- [func setTextContainer(NSTextContainer, forGlyphRange: NSRange)](./settextcontainer%28_,forglyphrange%29.md)
  Associates a text container with the specified range of glyphs.
- [func textContainerChangedGeometry(NSTextContainer)](./textcontainerchangedgeometry%28_%29.md)
  Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [func textContainerChangedTextView(NSTextContainer)](./textcontainerchangedtextview%28_%29.md)
  Updates the information necessary to manage text view objects for the specified text container.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSTextContainer?](./textcontainer%28forglyphat,effectiverange,withoutadditionallayout%29.md)
  Returns the text container that manages the layout for the specified glyph.
- [func usedRect(for: NSTextContainer) -> NSRect](./usedrect%28for%29.md)
  Returns the bounding rectangle for the glyphs in the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/textcontainer(forglyphat:effectiverange:))*