# draw(at:in:)

**Framework**: AppKit  
**Kind**: method

Renders the visual representation of this element in the specified graphics context.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func draw(at point: CGPoint, in context: CGContext)
```

## Parameters

- `point`: The origin as a  .
- `context`: The rendering context.

## See Also

- [var layoutFragmentFrame: CGRect](nstextlayoutfragment/layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [var renderingSurfaceBounds: CGRect](nstextlayoutfragment/renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func invalidateLayout()](nstextlayoutfragment/invalidatelayout.md)
  Invalidates any layout information associated with the text layout fragment.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](nstextlayoutfragment/textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](nstextlayoutfragment/framefortextattachment(at:).md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/draw(at:in:))*