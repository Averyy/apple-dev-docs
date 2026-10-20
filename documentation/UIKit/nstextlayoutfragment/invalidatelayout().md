# invalidateLayout()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Invalidates any layout information associated with the text layout fragment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func invalidateLayout()
```

```objc
- (void) invalidateLayout;
```

## See Also

### Drawing the fragment and attachments
- [var layoutFragmentFrame: CGRect](./layoutfragmentframe.md)
  The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [var renderingSurfaceBounds: CGRect](./renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func draw(at: CGPoint, in: CGContext)](./draw%28at,in%29.md)
  Renders the visual representation of this element in the specified graphics context.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](./textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](./framefortextattachment%28at%29.md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/invalidatelayout())*