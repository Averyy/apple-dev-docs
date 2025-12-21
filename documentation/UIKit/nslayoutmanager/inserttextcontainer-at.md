# insertTextContainer(_:at:)

**Framework**: UIKit  
**Kind**: method

Inserts a text container at the specified index in the list of text containers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func insertTextContainer(_ container: NSTextContainer, at index: Int)
```

#### Discussion

This method invalidates layout for all subsequent `NSTextContainer` objects, and invalidates glyph information as needed.

## Parameters

- `container`: The text container to insert.
- `index`: The index in the series of text containers at which to insert  .

## See Also

- [var textContainers: [NSTextContainer]](nslayoutmanager/textcontainers.md)
  The current text containers of the layout manager.
- [func addTextContainer(NSTextContainer)](nslayoutmanager/addtextcontainer(_:).md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [func removeTextContainer(at: Int)](nslayoutmanager/removetextcontainer(at:).md)
  Removes the text container at the specified index and invalidates the layout as necessary.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/inserttextcontainer(_:at:))*