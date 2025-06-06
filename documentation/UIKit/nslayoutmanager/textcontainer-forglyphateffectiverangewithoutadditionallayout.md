# textContainer(forGlyphAt:effectiveRange:withoutAdditionalLayout:)

**Framework**: UIKit  
**Kind**: method

Returns the text container that manages the layout for the specified glyph.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func textContainer(forGlyphAt glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?, withoutAdditionalLayout flag: Bool) -> NSTextContainer?
```

#### Return Value

The text container in which the glyph at `glyphIndex` is laid out.

#### Discussion

This method is primarily for use from within `NSTypesetter`, after layout is complete for the range in question, but before the layout manager’s call to `NSTypesetter` has returned. In that case glyph and layout holes have not yet been recalculated, so the layout manager does not yet know that layout is complete for that range, and this variant must be used.

Overriding this method is not recommended. Any changes to the returned glyph range should be done at the typesetter level.

## Parameters

- `glyphIndex`: Index of a glyph in the returned container.
- `effectiveGlyphRange`: If not  , on output, points to the whole range of glyphs that are in the returned container.
- `flag`: If  , glyph generation and layout are not performed, so this option should not be used unless layout is known to be complete for the range in question, or unless noncontiguous layout is enabled; if  , both are performed as needed.

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
- [func textContainerChangedTextView(_ container: NSTextContainer)](../AppKit/NSLayoutManager/textContainerChangedTextView(_:).md)
  Updates the information necessary to manage text view objects for the specified text container.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSTextContainer?](nslayoutmanager/textcontainer(forglyphat:effectiverange:).md)
  Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [func usedRect(for: NSTextContainer) -> CGRect](nslayoutmanager/usedrect(for:).md)
  Returns the bounding rectangle for the glyphs in the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/textcontainer(forglyphat:effectiverange:withoutadditionallayout:))*