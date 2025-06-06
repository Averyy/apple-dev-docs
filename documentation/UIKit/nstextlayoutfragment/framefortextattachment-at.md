# frameForTextAttachment(at:)

**Framework**: UIKit  
**Kind**: method

Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func frameForTextAttachment(at location: any NSTextLocation) -> CGRect
```

#### Return Value

The frame rectangle that describes the text layout fragment.

#### Discussion

Returns [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) if `location` isn’t with any attachment or the state isn’t [`NSTextLayoutFragment.State.layoutAvailable`](nstextlayoutfragment/state-swift.enum/layoutavailable.md).

## Parameters

- `location`: The   that describes the location in the text layout fragment.

## See Also

- [var layoutFragmentFrame: CGRect](nstextlayoutfragment/layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [var renderingSurfaceBounds: CGRect](nstextlayoutfragment/renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func draw(at: CGPoint, in: CGContext)](nstextlayoutfragment/draw(at:in:).md)
  Renders the visual representation of this element in the specified graphics context.
- [func invalidateLayout()](nstextlayoutfragment/invalidatelayout.md)
  Invalidates any layout information associated with the text layout fragment.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](nstextlayoutfragment/textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/framefortextattachment(at:))*