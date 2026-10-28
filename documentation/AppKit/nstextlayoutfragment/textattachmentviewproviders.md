# textAttachmentViewProviders

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The attachment view provider associated with the text layout fragment.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var textAttachmentViewProviders: [NSTextAttachmentViewProvider] { get }
```

```objc
@property (copy, readonly) NSArray<NSTextAttachmentViewProvider *> * textAttachmentViewProviders;
```

## Discussion

The property contents are only valid with [`NSTextLayoutFragment.State.layoutAvailable`](./state-swift.enum/layoutavailable.md).

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
- [func frameForTextAttachment(at: any NSTextLocation) -> CGRect](./framefortextattachment%28at%29.md)
  Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/textattachmentviewproviders)*