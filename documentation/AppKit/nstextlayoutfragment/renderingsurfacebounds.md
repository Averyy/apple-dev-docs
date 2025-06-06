# renderingSurfaceBounds

**Framework**: AppKit  
**Kind**: property

The bounds defining the area required for rendering the contents.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var renderingSurfaceBounds: CGRect { get }
```

#### Discussion

The coordinate system is vertically flipped from the `layoutFragmentFrame` origin ({`0`,`0`} is at the upper-left corner). The size should be larger than `layoutFragmentFrame.size`. The origin could be in the negative coordinate since the rendering could stretch out of `layoutFragmentFrame`. Only valid when `state` greater than [`NSTextLayoutFragment.State.estimatedUsageBounds`](nstextlayoutfragment/state-swift.enum/estimatedusagebounds.md).

## See Also

- [var layoutFragmentFrame: CGRect](nstextlayoutfragment/layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [func draw(at: CGPoint, in: CGContext)](nstextlayoutfragment/draw(at:in:).md)
  Renders the visual representation of this element in the specified graphics context.
- [func invalidateLayout()](nstextlayoutfragment/invalidatelayout.md)
  Invalidates any layout information associated with the text layout fragment.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](nstextlayoutfragment/textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](nstextlayoutfragment/framefortextattachment(at:).md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/renderingsurfacebounds)*