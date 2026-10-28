# addTextContainer(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Appends the specified text container to the series of text containers where the layout manager arranges text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func addTextContainer(_ container: NSTextContainer)
```

```objc
- (void) addTextContainer:(NSTextContainer *) container;
```

## Discussion

Invalidates glyphs and layout as needed, but doesn’t perform glyph generation or layout.

## Parameters

- `container`: The text container to append.

## See Also

### Managing the text containers
- [var textContainers: [NSTextContainer]](./textcontainers.md)
  The current text containers of the layout manager.
- [func insertTextContainer(NSTextContainer, at: Int)](./inserttextcontainer%28_,at%29.md)
  Inserts a text container at the specified index in the list of text containers.
- [func removeTextContainer(at: Int)](./removetextcontainer%28at%29.md)
  Removes the text container at the specified index and invalidates the layout as necessary.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/addtextcontainer(_:))*