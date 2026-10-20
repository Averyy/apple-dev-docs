# draw(at:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Renders the visual representation of this element in the specified graphics context.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func draw(at point: CGPoint, in context: CGContext)
```

```objc
- (void) drawAtPoint:(CGPoint) point inContext:(CGContextRef) context;
```

## Parameters

- `point`: The origin as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- `context`: The rendering context.

## See Also

### Drawing the fragment and attachments
- [var layoutFragmentFrame: CGRect](./layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [var renderingSurfaceBounds: CGRect](./renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Invalidates any layout information associated with the text layout fragment.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](./textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](./framefortextattachment%28at%29.md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/draw(at:in:))*