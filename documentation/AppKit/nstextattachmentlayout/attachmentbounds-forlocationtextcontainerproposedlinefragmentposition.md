# attachmentBounds(for:location:textContainer:proposedLineFragment:position:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the layout bounds of the attachment you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func attachmentBounds(for attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect
```

#### Return Value

Returns a [`CGRect`](https://developer.apple.com/documentation/corefoundation/cgrect) that describes the boundaries of the attachment, or `CGRectZero.`

#### Discussion

The framework interprets the bounds origin to match `position` inside `proposedLineFragment`. The default [`NSTextAttachment`](nstextattachment.md) implementation returns bounds if the value isn’t equivalent to [`CGRectZero`](https://developer.apple.com/documentation/coregraphics/cgrectzero); otherwise, it derives the bounds value from `image.size`. Conforming objects can implement more sophisticated logic for negotiating the frame size based on the available container space and proposed line fragment rectangle.

## Parameters

- `attributes`: A dictionary of [`NSAttributedString.Key`](https://developer.apple.com/documentation/foundation/nsattributedstring/key) attributes.
- `location`: An [`NSTextLocation`](nstextlocation.md) that indicates that start of the string.
- `textContainer`: The [`NSTextContainer`](nstextcontainer.md) that contains the source text.
- `proposedLineFragment`: A [`CGRect`](https://developer.apple.com/documentation/corefoundation/cgrect) that describes the boundaries of the line fragment.
- `position`: A [`CGPoint`](https://developer.apple.com/documentation/corefoundation/cgpoint) inside `proposedLineFragment`.

## See Also

- [func image(for: CGRect, attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?) -> NSImage?](nstextattachmentlayout/image(for:attributes:location:textcontainer:).md)
  Returns the image object rendered at the bounds and inside the text container you specify.
- [func viewProvider(for: NSView?, location: any NSTextLocation, textContainer: NSTextContainer?) -> NSTextAttachmentViewProvider?](nstextattachmentlayout/viewprovider(for:location:textcontainer:).md)
  Returns the text attachment view provider corresponding to the file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentlayout/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:))*