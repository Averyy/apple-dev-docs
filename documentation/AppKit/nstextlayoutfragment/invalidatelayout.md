# invalidateLayout()

**Framework**: AppKit  
**Kind**: method

Invalidates any layout information associated with the text layout fragment.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func invalidateLayout()
```

## See Also

- [var layoutFragmentFrame: CGRect](nstextlayoutfragment/layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [var renderingSurfaceBounds: CGRect](nstextlayoutfragment/renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func draw(at: CGPoint, in: CGContext)](nstextlayoutfragment/draw(at:in:).md)
  Renders the visual representation of this element in the specified graphics context.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](nstextlayoutfragment/textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](nstextlayoutfragment/framefortextattachment(at:).md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/invalidatelayout())*