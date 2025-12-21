# removeTextContainer(at:)

**Framework**: UIKit  
**Kind**: method

Removes the text container at the specified index and invalidates the layout as necessary.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func removeTextContainer(at index: Int)
```

#### Discussion

This method invalidates glyph information as needed.

## Parameters

- `index`: The index of the text container to remove.

## See Also

- [func invalidateGlyphs(forCharacterRange: NSRange, changeInLength: Int, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidateglyphs(forcharacterrange:changeinlength:actualcharacterrange:).md)
  Invalidates and adjusts the glyphs in the specified character range.
- [func invalidateLayout(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidatelayout(forcharacterrange:actualcharacterrange:).md)
  Invalidates the layout information for the glyphs that map to the specified character range.
- [var textContainers: [NSTextContainer]](nslayoutmanager/textcontainers.md)
  The current text containers of the layout manager.
- [func addTextContainer(NSTextContainer)](nslayoutmanager/addtextcontainer(_:).md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [func insertTextContainer(NSTextContainer, at: Int)](nslayoutmanager/inserttextcontainer(_:at:).md)
  Inserts a text container at the specified index in the list of text containers.
- [func setTextContainer(NSTextContainer, forGlyphRange: NSRange)](nslayoutmanager/settextcontainer(_:forglyphrange:).md)
  Associates a text container with the specified range of glyphs.
- [func textContainerChangedGeometry(NSTextContainer)](nslayoutmanager/textcontainerchangedgeometry(_:).md)
  Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [func textContainerChangedTextView(NSTextContainer)](../AppKit/NSLayoutManager/textContainerChangedTextView(_:).md)
  Updates the information necessary to manage text view objects for the specified text container.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSTextContainer?](nslayoutmanager/textcontainer(forglyphat:effectiverange:).md)
  Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSTextContainer?](nslayoutmanager/textcontainer(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the text container that manages the layout for the specified glyph.
- [func usedRect(for: NSTextContainer) -> CGRect](nslayoutmanager/usedrect(for:).md)
  Returns the bounding rectangle for the glyphs in the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/removetextcontainer(at:))*