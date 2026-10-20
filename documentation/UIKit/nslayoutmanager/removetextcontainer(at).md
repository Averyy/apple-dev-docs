# removeTextContainer(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the text container at the specified index and invalidates the layout as necessary.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeTextContainer(at index: Int)
```

```objc
- (void) removeTextContainerAtIndex:(NSUInteger) index;
```

#### Discussion

This method invalidates glyph information as needed.

## Parameters

- `index`: The index of the text container to remove.

## See Also

### Related Documentation
- [func invalidateGlyphs(forCharacterRange: NSRange, changeInLength: Int, actualCharacterRange: NSRangePointer?)](./invalidateglyphs%28forcharacterrange,changeinlength,actualcharacterrange%29.md)
  Invalidates and adjusts the glyphs in the specified character range.
- [func invalidateLayout(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?)](./invalidatelayout%28forcharacterrange,actualcharacterrange%29.md)
  Invalidates the layout information for the glyphs that map to the specified character range.
### Managing the text containers
- [var textContainers: [NSTextContainer]](./textcontainers.md)
  The current text containers of the layout manager.
- [func addTextContainer(NSTextContainer)](./addtextcontainer%28_%29.md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [func insertTextContainer(NSTextContainer, at: Int)](./inserttextcontainer%28_,at%29.md)
  Inserts a text container at the specified index in the list of text containers.
- [func setTextContainer(NSTextContainer, forGlyphRange: NSRange)](./settextcontainer%28_,forglyphrange%29.md)
  Associates a text container with the specified range of glyphs.
- [func textContainerChangedGeometry(NSTextContainer)](./textcontainerchangedgeometry%28_%29.md)
  Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [func textContainerChangedTextView(NSTextContainer)](../../AppKit/nslayoutmanager/textcontainerchangedtextview%28_%29.md)
  Updates the information necessary to manage text view objects for the specified text container.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSTextContainer?](./textcontainer%28forglyphat,effectiverange%29.md)
  Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSTextContainer?](./textcontainer%28forglyphat,effectiverange,withoutadditionallayout%29.md)
  Returns the text container that manages the layout for the specified glyph.
- [func usedRect(for: NSTextContainer) -> CGRect](./usedrect%28for%29.md)
  Returns the bounding rectangle for the glyphs in the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/removetextcontainer(at:))*