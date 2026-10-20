# layoutFragmentFrame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var layoutFragmentFrame: CGRect { get }
```

```objc
@property (readonly) CGRect layoutFragmentFrame;
```

## See Also

### Drawing the fragment and attachments
- [var renderingSurfaceBounds: CGRect](./renderingsurfacebounds.md)
  The bounds defining the area required for rendering the contents.
- [func draw(at: CGPoint, in: CGContext)](./draw%28at,in%29.md)
  Renders the visual representation of this element in the specified graphics context.
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Invalidates any layout information associated with the text layout fragment.
- [var textAttachmentViewProviders: [NSTextAttachmentViewProvider]](./textattachmentviewproviders.md)
  The attachment view provider associated with the text layout fragment.
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](./framefortextattachment%28at%29.md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/layoutfragmentframe)*