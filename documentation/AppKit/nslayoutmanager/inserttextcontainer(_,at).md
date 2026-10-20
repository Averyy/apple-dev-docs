# insertTextContainer(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts a text container at the specified index in the list of text containers.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func insertTextContainer(_ container: NSTextContainer, at index: Int)
```

```objc
- (void) insertTextContainer:(NSTextContainer *) container atIndex:(NSUInteger) index;
```

#### Discussion

This method invalidates layout for all subsequent `NSTextContainer` objects, and invalidates glyph information as needed.

## Parameters

- `container`: The text container to insert.
- `index`: The index in the series of text containers at which to insert `aTextContainer`.

## See Also

### Managing the text containers
- [var textContainers: [NSTextContainer]](./textcontainers.md)
  The current text containers of the layout manager.
- [func addTextContainer(NSTextContainer)](./addtextcontainer%28_%29.md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [func removeTextContainer(at: Int)](./removetextcontainer%28at%29.md)
  Removes the text container at the specified index and invalidates the layout as necessary.
- [func setTextContainer(NSTextContainer, forGlyphRange: NSRange)](./settextcontainer%28_,forglyphrange%29.md)
  Associates a text container with the specified range of glyphs.
- [func textContainerChangedGeometry(NSTextContainer)](./textcontainerchangedgeometry%28_%29.md)
  Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [func textContainerChangedTextView(NSTextContainer)](./textcontainerchangedtextview%28_%29.md)
  Updates the information necessary to manage text view objects for the specified text container.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSTextContainer?](./textcontainer%28forglyphat,effectiverange%29.md)
  Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSTextContainer?](./textcontainer%28forglyphat,effectiverange,withoutadditionallayout%29.md)
  Returns the text container that manages the layout for the specified glyph.
- [func usedRect(for: NSTextContainer) -> NSRect](./usedrect%28for%29.md)
  Returns the bounding rectangle for the glyphs in the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/inserttextcontainer(_:at:))*