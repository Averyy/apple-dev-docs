# textAttachmentViewProviders

**Framework**: AppKit  
**Kind**: property

The attachment view provider associated with the text layout fragment.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var textAttachmentViewProviders: [NSTextAttachmentViewProvider] { get }
```

#### Discussion

The property contents are only valid with [`NSTextLayoutFragment.State.layoutAvailable`](nstextlayoutfragment/state-swift.enum/layoutavailable.md).

## See Also

- [var layoutFragmentFrame: CGRect](nstextlayoutfragment/layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [var renderingSurfaceBounds: CGRect](nstextlayoutfragment/renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func draw(at: CGPoint, in: CGContext)](nstextlayoutfragment/draw(at:in:).md)
  Renders the visual representation of this element in the specified graphics context.
- [func invalidateLayout()](nstextlayoutfragment/invalidatelayout.md)
  Invalidates any layout information associated with the text layout fragment.
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](nstextlayoutfragment/framefortextattachment(at:).md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/textattachmentviewproviders)*