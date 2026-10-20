# textContainerChangedGeometry(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func textContainerChangedGeometry(_ container: NSTextContainer)
```

```objc
- (void) textContainerChangedGeometry:(NSTextContainer *) container;
```

#### Discussion

This method is invoked automatically by other components of the text system; you should rarely need to invoke it directly. Subclasses of `NSTextContainer`, however, must invoke this method any time their size of shape changes (a text container that dynamically adjusts its shape to wrap text around placed graphics, for example, must do so when a graphic is added, moved, or removed).

## Parameters

- `container`: The text container whose layout is invalidated.

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
- [func textContainerChangedTextView(NSTextContainer)](./textcontainerchangedtextview%28_%29.md)
  Updates the information necessary to manage text view objects for the specified text container.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSTextContainer?](./textcontainer%28forglyphat,effectiverange%29.md)
  Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSTextContainer?](./textcontainer%28forglyphat,effectiverange,withoutadditionallayout%29.md)
  Returns the text container that manages the layout for the specified glyph.
- [func usedRect(for: NSTextContainer) -> NSRect](./usedrect%28for%29.md)
  Returns the bounding rectangle for the glyphs in the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/textcontainerchangedgeometry(_:))*