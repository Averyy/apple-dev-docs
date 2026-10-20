# frameForTextAttachment(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func frameForTextAttachment(at location: any NSTextLocation) -> CGRect
```

```objc
- (CGRect) frameForTextAttachmentAtLocation:(id<NSTextLocation>) location;
```

#### Return Value

The frame rectangle that describes the text layout fragment.

#### Discussion

Returns [`CGRectZero`](../../CoreGraphics/cgrectzero.md) if `location` isn’t with any attachment or the state isn’t [`NSTextLayoutFragment.State.layoutAvailable`](./state-swift.enum/layoutavailable.md).

## Parameters

- `location`: The [`NSTextLocation`](../nstextlocation.md) that describes the location in the text layout fragment.

## See Also

### Drawing the fragment and attachments
- [var layoutFragmentFrame: CGRect](./layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [var renderingSurfaceBounds: CGRect](./renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func draw(at: CGPoint, in: CGContext)](./draw%28at,in%29.md)
  Renders the visual representation of this element in the specified graphics context.
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Invalidates any layout information associated with the text layout fragment.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](./textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/framefortextattachment(at:))*