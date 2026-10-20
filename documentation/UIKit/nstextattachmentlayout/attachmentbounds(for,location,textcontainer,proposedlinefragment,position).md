# attachmentBounds(for:location:textContainer:proposedLineFragment:position:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the layout bounds of the attachment you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func attachmentBounds(for attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect
```

```objc
- (CGRect) attachmentBoundsForAttributes:(NSDictionary<NSString *,id> *) attributes location:(id<NSTextLocation>) location textContainer:(NSTextContainer *) textContainer proposedLineFragment:(CGRect) proposedLineFragment position:(CGPoint) position;
```

#### Return Value

Returns a [`CGRect`](../../CoreFoundation/cgrect.md) that describes the boundaries of the attachment, or `CGRectZero.`

#### Discussion

The framework interprets the bounds origin to match `position` inside `proposedLineFragment`. The default [`NSTextAttachment`](../nstextattachment.md) implementation returns bounds if the value isn’t equivalent to [`CGRectZero`](../../CoreGraphics/cgrectzero.md); otherwise, it derives the bounds value from `image.size`. Conforming objects can implement more sophisticated logic for negotiating the frame size based on the available container space and proposed line fragment rectangle.

## Parameters

- `attributes`: A dictionary of [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md) attributes.
- `location`: An [`NSTextLocation`](../nstextlocation.md) that indicates that start of the string.
- `textContainer`: The [`NSTextContainer`](../nstextcontainer.md) that contains the source text.
- `proposedLineFragment`: A [`CGRect`](../../CoreFoundation/cgrect.md) that describes the boundaries of the line fragment.
- `position`: A [`CGPoint`](../../CoreFoundation/cgpoint.md) inside `proposedLineFragment`.

## See Also

### Determining the characteristics of an attachment
- [func image(for: CGRect, attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?) -> UIImage?](./image%28for,attributes,location,textcontainer%29.md)
  Returns the image object rendered at the bounds and inside the text container you specify.
- [func viewProvider(for: UIView?, location: any NSTextLocation, textContainer: NSTextContainer?) -> NSTextAttachmentViewProvider?](./viewprovider%28for,location,textcontainer%29.md)
  Returns the text attachment view provider corresponding to the file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentlayout/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:))*